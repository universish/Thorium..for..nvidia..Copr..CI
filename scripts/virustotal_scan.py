#!/usr/bin/env python3
"""Best-effort VirusTotal scan after mandatory local checks have passed.

Exit 1 only for a positive malware result. API errors, quota exhaustion, and
unknown samples are reported as warnings so they cannot masquerade as a clean
VirusTotal verdict.
"""

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from urllib.parse import urlparse

API = "https://www.virustotal.com/api/v3"
DIRECT_LIMIT = 32 * 1024 * 1024
UPLOAD_LIMIT = 650 * 1024 * 1024


class Unavailable(Exception):
    pass


class Malicious(Exception):
    pass


def warn(message):
    print(f"::warning title=VirusTotal unavailable::{message}", flush=True)


def request(key, method, url, path=None):
    command = ["curl", "--silent", "--show-error", "--max-time", "120", "--retry", "2",
               "--write-out", "\n%{http_code}", "-H", f"x-apikey: {key}"]
    if method == "POST":
        command += ["-X", "POST", "-F", f"file=@{path}"]
    command.append(url)
    try:
        response = subprocess.run(command, capture_output=True, text=True, timeout=400)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise Unavailable(f"VirusTotal request failed: {exc}") from exc
    if response.returncode:
        raise Unavailable(f"VirusTotal request failed (curl exit {response.returncode})")
    try:
        body, status = response.stdout.rsplit("\n", 1)
        parsed = json.loads(body)
        if not isinstance(parsed, dict):
            raise ValueError("expected a JSON object")
        return int(status), parsed
    except (ValueError, json.JSONDecodeError) as exc:
        raise Unavailable("VirusTotal returned an invalid response") from exc


def digest(path):
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def assess(stats, label):
    if not isinstance(stats, dict):
        raise Unavailable(f"{label}: missing VirusTotal analysis statistics")
    count = stats.get("malicious")
    if isinstance(count, int) and not isinstance(count, bool) and count > 0:
        raise Malicious(f"{label}: {count} VirusTotal engines reported malware")
    categories = ("malicious", "suspicious", "harmless", "undetected")
    if any(
        not isinstance(stats.get(name, 0), int)
        or isinstance(stats.get(name, 0), bool)
        or stats.get(name, 0) < 0
        for name in categories
    ) or count is None:
        raise Unavailable(f"{label}: missing VirusTotal analysis statistics")
    if not sum(stats.get(name, 0) for name in categories):
        raise Unavailable(f"{label}: VirusTotal report has no completed engine results")
    print(f"VirusTotal: {label}: malicious={count}", flush=True)


def object_field(value, key, label):
    if not isinstance(value, dict) or not isinstance(value.get(key), dict):
        raise Unavailable(f"{label}: malformed VirusTotal response ({key})")
    return value[key]


def compressed_retry(key, path, label):
    with tempfile.TemporaryDirectory(prefix="vt-") as directory:
        compressed = Path(directory) / (path.name + ".gz")
        with path.open("rb") as source, gzip.open(compressed, "wb", compresslevel=6) as target:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                target.write(chunk)
        if compressed.stat().st_size > UPLOAD_LIMIT:
            raise Unavailable(f"{label}: file and compressed copy exceed the upload limit")
        print(f"VirusTotal: uploading compressed copy of {label}; this is a separate sample", flush=True)
        upload(key, compressed, label + " (compressed)", allow_compress=False)
        print(f"::warning title=VirusTotal partial coverage::{label}: only the compressed copy received a new analysis", flush=True)


def upload(key, path, label, allow_compress=True):
    size = path.stat().st_size
    if size > UPLOAD_LIMIT:
        if allow_compress:
            return compressed_retry(key, path, label)
        raise Unavailable(f"{label}: compressed copy exceeds the upload limit")
    url = API + "/files"
    if size > DIRECT_LIMIT:
        try:
            status, body = request(key, "GET", API + "/files/upload_url")
        except Unavailable:
            if allow_compress:
                return compressed_retry(key, path, label)
            raise
        if status in {401, 403, 429}:
            raise Unavailable(f"{label}: upload URL request returned HTTP {status}")
        if status != 200 or not isinstance(body.get("data"), str):
            if allow_compress:
                return compressed_retry(key, path, label)
            raise Unavailable(f"{label}: upload URL request returned HTTP {status}")
        url = body["data"]
        parsed = urlparse(url)
        if parsed.hostname not in {"www.virustotal.com", "virustotal.com"} or parsed.scheme not in {"http", "https"}:
            raise Unavailable(f"{label}: invalid VirusTotal upload URL")
        # VT's documented upload URL example uses HTTP. Send the API key only via TLS.
        if parsed.scheme == "http":
            url = parsed._replace(scheme="https").geturl()
    try:
        status, body = request(key, "POST", url, path)
    except Unavailable:
        if allow_compress:
            return compressed_retry(key, path, label)
        raise
    if status in {401, 403, 429}:
        raise Unavailable(f"{label}: upload returned HTTP {status}")
    if status not in {200, 201}:
        if allow_compress:
            return compressed_retry(key, path, label)
        raise Unavailable(f"{label}: upload returned HTTP {status}")
    analysis_id = object_field(body, "data", label).get("id")
    if not isinstance(analysis_id, str) or not analysis_id:
        raise Unavailable(f"{label}: upload returned no analysis ID")
    for attempt in range(18):
        time.sleep(20)
        status, body = request(key, "GET", API + "/analyses/" + analysis_id)
        if status != 200:
            raise Unavailable(f"{label}: analysis returned HTTP {status}")
        attributes = object_field(object_field(body, "data", label), "attributes", label)
        if attributes.get("status") == "completed":
            assess(attributes.get("stats"), label)
            return
    raise Unavailable(f"{label}: analysis timed out")


def scan(key, path, seen):
    sha256 = digest(path)
    if sha256 in seen:
        return
    label = str(path)
    status, body = request(key, "GET", API + "/files/" + sha256)
    if status == 200:
        attributes = object_field(object_field(body, "data", label), "attributes", label)
        assess(attributes.get("last_analysis_stats"), label)
    elif status == 404:
        upload(key, path, label)
    else:
        raise Unavailable(f"{label}: hash lookup returned HTTP {status}")
    seen.add(sha256)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("payload", type=Path)
    parser.add_argument("main_binary", type=Path)
    args = parser.parse_args()
    key = os.environ.get("VT_API_KEY")
    if not key:
        warn("VIRUSTOTAL_API_KEY is missing; continuing after mandatory local scans")
        return 0
    paths = [args.archive, args.main_binary]
    paths.extend(sorted(path for path in args.payload.rglob("*") if path.is_file() and not path.is_symlink()))
    seen = set()
    try:
        for path in paths:
            scan(key, path, seen)
    except Malicious as exc:
        print(f"::error title=VirusTotal malware detection::{exc}", file=sys.stderr)
        return 1
    except (Unavailable, OSError) as exc:
        warn(str(exc) + f"; {len(seen)} distinct hashes queried; remaining VirusTotal checks skipped")
        return 0
    print(f"VirusTotal queried {len(seen)} distinct SHA-256 samples", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
