# Thorium Browser (AVX2 & ARM64) for Fedora Copr

[![Fedora Copr](https://img.shields.io/badge/Copr-universish%2FThorium-blue.svg)](https://copr.fedorainfracloud.org/coprs/universish/Thorium/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Arch-x86__64%20(AVX2)%20%7C%20aarch64-brightgreen.svg)]()

Enterprise-grade, automated RPM packaging and continuous delivery pipeline for **Thorium Browser** on Fedora Linux. 

This repository synchronizes upstream builds from [Alex313031/thorium](https://github.com/Alex313031/thorium) and [gz83/thorium](https://github.com/gz83/thorium), packaging them for **Fedora Copr** with specialized GPU runtime routing.

---

## 🎯 Architecture & Mission

Thorium delivers unmatched speed via aggressive CPU compiler optimizations (AVX2 instructions on x86_64, NEON on aarch64). However, running high-performance Chromium under modern Linux display servers (Wayland/XWayland) often leads to hardware acceleration regressions—especially on NVIDIA GPUs.

This project delivers:
1. **Intelligent GPU Acceleration Routing:**
   - **NVIDIA GPU Detection:** Automatically applies `NVD_BACKEND=direct`, `__NV_PRIME_RENDER_OFFLOAD=1`, and `__GLX_VENDOR_LIBRARY_NAME=nvidia` with ANGLE/GL interop.
   - **AMD & Intel Native Fallback:** Preserves default Mesa/VA-API acceleration pathways without forcing incompatible vendor GLX libraries.
   - **Industrial Graphics Support:** Stable execution for ASPEED, Matrox, and software-rendered framebuffers.
2. **Strict Architecture Filtering:** Only compiler-optimized `x86_64` (AVX2) and `aarch64` binaries are packaged.
3. **Automated Synchronization:** GitHub Actions poll upstream releases 4 times daily (aligned with US and Hong Kong working schedules), enforcing fallback extraction (`RPM -> AppImage -> DEB -> Portable ZIP`).

---

## 🚀 Installation Guide

### 1. Enable the Copr Repository
```bash
sudo dnf copr enable universish/Thorium

```

### 2. Install Thorium Browser

```bash
sudo dnf install -y thorium-browser

```

### 3. Verify Hardware Acceleration

Launch Thorium, navigate to `chrome://gpu`, and verify:

* **Video Decode:** Hardware accelerated
* **Rasterization:** Hardware accelerated
* **Graphics Backend:** ANGLE (OpenGL)

---

## ⚙️ Configuration & Flags

Upon initial launch, the smart wrapper initializes:
`~/.config/thorium-flags.conf`

```text
--ozone-platform=x11
--enable-features=VaapiVideoDecodeLinuxGL,VaapiVideoEncoderLinuxGL
--ignore-gpu-blocklist
--enable-zero-copy
--use-gl=angle
--use-angle=gl

```

You can customize runtime arguments directly in this file without modifying the `.desktop` launcher.

---

## 🗑️ Removal & Cleanup

### Remove Package

```bash
sudo dnf remove -y thorium-browser

```

### Disable Copr Repository

```bash
sudo dnf copr disable universish/Thorium

```

### Optional: Remove User Configurations

```bash
rm -rf ~/.config/thorium-flags.conf ~/.config/thorium

```

---

## 🛡️ Security & Integrity

* **Non-Invasive RPM Spec:** Packages do not tamper with root filesystem libraries; binaries reside in `/opt/thorium-browser/`.
* **Reproducible Pipeline:** All builds are assembled inside official Fedora root containers and submitted to official Fedora Copr builders.
* **License:** The packaging automation is provided under the [MIT License](https://www.google.com/search?q=LICENSE). Thorium Browser remains governed by its respective upstream licenses (BSD-3-Clause / Chromium Authors).
