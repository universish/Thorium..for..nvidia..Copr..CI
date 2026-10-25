import importlib.util
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


MODULE = Path(__file__).resolve().parents[1] / "scripts" / "virustotal_scan.py"
SPEC = importlib.util.spec_from_file_location("virustotal_scan", MODULE)
vt = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(vt)


class VirusTotalTests(unittest.TestCase):
    def test_existing_hash_with_detection_blocks(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "sample"
            sample.write_bytes(b"sample")
            report = {"data": {"attributes": {"last_analysis_stats": {"malicious": 1}}}}
            with mock.patch.object(vt, "request", return_value=(200, report)):
                with self.assertRaises(vt.Malicious):
                    vt.scan("key", sample, set())

    def test_empty_engine_report_is_unavailable(self):
        with self.assertRaises(vt.Unavailable):
            vt.assess({"malicious": 0, "harmless": 0, "undetected": 0}, "sample")

    def test_malicious_count_blocks_even_if_other_stats_are_malformed(self):
        with self.assertRaises(vt.Malicious):
            vt.assess({"malicious": 1, "harmless": "broken"}, "sample")

    def test_unknown_hash_uploads_original(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "sample"
            sample.write_bytes(b"sample")
            with mock.patch.object(vt, "request", return_value=(404, {})):
                with mock.patch.object(vt, "upload") as upload:
                    vt.scan("key", sample, set())
            upload.assert_called_once_with("key", sample, str(sample))

    def test_upload_error_retries_compressed_sample(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "sample"
            sample.write_bytes(b"sample")
            with mock.patch.object(vt, "request", return_value=(413, {})):
                with mock.patch.object(vt, "compressed_retry") as retry:
                    vt.upload("key", sample, "sample")
            retry.assert_called_once_with("key", sample, "sample")

    def test_oversized_sample_compresses_and_scans_without_treating_it_as_original(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "sample"
            sample.write_bytes(b"a" * 1000)
            uploaded = []

            def reply(_key, method, url, path=None):
                if method == "POST":
                    uploaded.append(path)
                    self.assertEqual(path.suffix, ".gz")
                    return 200, {"data": {"id": "analysis-1"}}
                return 200, {"data": {"attributes": {"status": "completed", "stats": {"malicious": 0, "harmless": 1}}}}

            with mock.patch.object(vt, "UPLOAD_LIMIT", 50), mock.patch.object(vt, "request", side_effect=reply), mock.patch.object(vt.time, "sleep"):
                vt.upload("key", sample, "sample")
            self.assertEqual(len(uploaded), 1)

    def test_quota_error_does_not_retry_upload_as_compressed_sample(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "sample"
            sample.write_bytes(b"sample")
            with mock.patch.object(vt, "request", return_value=(429, {})), mock.patch.object(vt, "compressed_retry") as retry:
                with self.assertRaises(vt.Unavailable):
                    vt.upload("key", sample, "sample")
            retry.assert_not_called()

    def test_hash_queries_prioritize_archive_and_main_binary(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / "upstream.rpm"
            archive.write_bytes(b"archive")
            payload = Path(directory) / "payload"
            payload.mkdir()
            other = payload / "000-first"
            other.write_bytes(b"other")
            main_binary = payload / "thorium"
            main_binary.write_bytes(b"main")
            queried = []

            def reply(_key, _method, url, _path=None):
                queried.append(url.rsplit("/", 1)[-1])
                return 200, {"data": {"attributes": {"last_analysis_stats": {"malicious": 0, "harmless": 1}}}}

            with mock.patch.dict("os.environ", {"VT_API_KEY": "key"}):
                with mock.patch.object(sys, "argv", ["vt", str(archive), str(payload), str(main_binary)]):
                    with mock.patch.object(vt, "request", side_effect=reply):
                        self.assertEqual(vt.main(), 0)
            self.assertEqual(queried, [hashlib.sha256(data).hexdigest() for data in (b"archive", b"main", b"other")])

    def test_api_error_warns_and_allows_local_gate_to_publish(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / "upstream.rpm"
            archive.write_bytes(b"sample")
            payload = Path(directory) / "payload"
            payload.mkdir()
            main_binary = payload / "thorium"
            main_binary.write_bytes(b"main")
            with mock.patch.dict("os.environ", {"VT_API_KEY": "key"}):
                with mock.patch.object(sys, "argv", ["vt", str(archive), str(payload), str(main_binary)]):
                    with mock.patch.object(vt, "scan", side_effect=vt.Unavailable("HTTP 429")):
                        with mock.patch.object(vt, "warn") as warning:
                            self.assertEqual(vt.main(), 0)
            warning.assert_called_once()

    def test_malware_result_blocks_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / "upstream.rpm"
            archive.write_bytes(b"sample")
            payload = Path(directory) / "payload"
            payload.mkdir()
            main_binary = payload / "thorium"
            main_binary.write_bytes(b"main")
            with mock.patch.dict("os.environ", {"VT_API_KEY": "key"}):
                with mock.patch.object(sys, "argv", ["vt", str(archive), str(payload), str(main_binary)]):
                    with mock.patch.object(vt, "scan", side_effect=vt.Malicious("detected")):
                        self.assertEqual(vt.main(), 1)


if __name__ == "__main__":
    unittest.main()
