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

### Updating Packages

To bypass local metadata caching and immediately pull new builds or packaging revisions (e.g., `<version>-1` to `<version>-2`):

**`upgrade --refresh`:**

```bash
sudo dnf upgrade --refresh "thorium*" "thorium-browser*" "thorium-browser"
```

**If that doesn't work, follow these steps:**

- Flush the cache:
```
sudo dnf clean all && sudo dnf makecache
```
- Install the thorium (it now comes directly from COPR):
```
sudo dnf install thorium-browser
```

### Optional: Remove User Configurations

```bash
rm -rf ~/.config/thorium-flags.conf ~/.config/thorium

```

---

# TEST

with Old desktop PC - Nvidia 1050 & i3 6100 
Motionmark v. 1.3.2 Test
A score between 1150.67 and 1709.21 @60fps.

<img width="1126" height="1080" alt="Ekran Görüntüsü 2026-10-07 05-22-27_cleaned" src="https://github.com/user-attachments/assets/a948d4a1-1e3c-4b24-b044-5372b4a3cc66" />

---

<img width="1230" height="735" alt="Ekran Görüntüsü 2026-10-07 05-45-15_cleaned" src="https://github.com/user-attachments/assets/9ccb921e-7702-41ac-8101-1373c895d38d" />

<img width="1285" height="1080" alt="Ekran Görüntüsü 2026-10-07 05-43-11_cleaned" src="https://github.com/user-attachments/assets/5be5cff2-482b-4054-a1ce-3eea3c8e0ba9" />

<img width="1289" height="523" alt="Ekran Görüntüsü 2026-10-07 05-43-32_cleaned" src="https://github.com/user-attachments/assets/720dcd32-e69d-4e97-adc0-e0638ac124c9" />

<img width="1289" height="523" alt="Ekran Görüntüsü 2026-10-07 05-43-42_cleaned" src="https://github.com/user-attachments/assets/50008281-2a59-47dd-88ee-2146e8cf98c6" />

<img width="1289" height="523" alt="Ekran Görüntüsü 2026-10-07 05-43-54_cleaned" src="https://github.com/user-attachments/assets/f27ffbd5-8989-4a59-a193-a6bc417f8578" />

<img width="1289" height="523" alt="Ekran Görüntüsü 2026-10-07 05-44-03_cleaned" src="https://github.com/user-attachments/assets/57033814-d498-4df2-a4d9-fb2b8bd6f224" />

<img width="1289" height="523" alt="Ekran Görüntüsü 2026-10-07 05-44-10_cleaned" src="https://github.com/user-attachments/assets/ec407a35-e78f-4db6-8bd8-5efbbacf391d" />

<img width="1289" height="523" alt="Ekran Görüntüsü 2026-10-07 05-44-32_cleaned" src="https://github.com/user-attachments/assets/dd1f8aa8-e7f7-4871-9dfc-f16618f56da4" />

<img width="1289" height="523" alt="Ekran Görüntüsü 2026-10-07 05-44-39_cleaned" src="https://github.com/user-attachments/assets/9f72ca71-8618-4924-8584-762ad9ea50cc" />

---

<img width="1920" height="1080" alt="Ekran Görüntüsü 2026-10-07 05-54-42_cleaned" src="https://github.com/user-attachments/assets/9e61de5c-c112-424d-9767-9b3ec5310f94" />

<img width="1920" height="1080" alt="Ekran Görüntüsü 2026-10-07 05-54-58_cleaned" src="https://github.com/user-attachments/assets/48e65753-a4f6-4d97-a8db-b3a3ac608801" />

<img width="1920" height="1080" alt="Ekran Görüntüsü 2026-10-07 05-55-09_cleaned" src="https://github.com/user-attachments/assets/5e1e4d1f-2ae9-45c5-afb5-e6991067b585" />

---

<img width="1456" height="1080" alt="Ekran Görüntüsü 2026-10-07 05-33-43_cleaned" src="https://github.com/user-attachments/assets/504ea9b4-ce8b-4e1c-a45e-5fb1aa741ae3" />

https://github.com/universish/Thorium..for..nvidia..Copr..CI/blob/main/tests/speedometer-3-2026-10-07T02_33_24.235Z.json

---

[HTML5test - How well does your browser support HTML5_.pdf](https://github.com/user-attachments/files/33135968/HTML5test.-.How.well.does.your.browser.support.HTML5_.pdf)

---

## **thorium://gpu/**

### Key Technical Parameters (Stripped)

* **Graphics Features:** Canvas, Compositing, Rasterization, OpenGL, WebGL, and WebGPU are enabled with hardware acceleration.   
* **Video Acceleration: Video decoding is hardware-accelerated, while video encoding is software-based.   
* **Hardware and Driver: NVIDIA GeForce GTX 1050 (Vendor: 0x10de, Device: 0x1c81) with NVIDIA driver 580.178.04 is active.   
* **Rendering Engine (Backend): ANGLE OpenGL ES 3.0 (gl=egl-angle, angle=opengl) is enabled.   
* **Display Layer: The Ozone X11 layer (--ozone-platform=x11) is used in the Wayland session.   
* **Memory and Rasterization: Tile updating and partial rasterization are enabled in zero-copy mode.   
* **Driver Exceptions: Compatibility patches specific to the NVIDIA Linux driver—init_gl_position_in_vertex_shader, disable_rgb_to_yuv_conversion, and disable_discard_framebuffer—have been applied.   

---

### Sanitized GPU Diagnostics Summary (English)

**Hardware & Runtime Environment:**

* **Platform:** Linux x86_64 running under a Wayland session via the Chromium Ozone X11 backend.
* **Active GPU:** NVIDIA GeForce GTX 1050 (Vendor ID: `0x10de`, Device ID: `0x1c81`).
* **Display Driver:** NVIDIA Proprietary Driver 580.178.04 supporting OpenGL 4.5.0.
* **Graphics Pipeline:** ANGLE OpenGL ES 3.0 implementation (`gl=egl-angle, angle=opengl`).
* **Active Flags:** `--ozone-platform=x11 --enable-features=VaapiVideoDecodeLinuxGL,VaapiVideoEncoderLinuxGL --ignore-gpu-blocklist --enable-zero-copy --use-gl=angle --use-angle=gl`.

**Acceleration Status:**
* **Hardware Accelerated:** 2D Canvas, WebGL, WebGPU, Compositing, Rasterization (Zero-copy), and Video Decoding.
* **Disabled / Software Only:** Video Encoding (hardware acceleration disabled via blocklist) and Native Vulkan.
**Driver Workarounds & Notes:**
* Vendor-specific workarounds applied: `init_gl_position_in_vertex_shader`, `disable_rgb_to_yuv_conversion`, `disable_discard_framebuffer`, and `unpack_overlapping_rows_separately_unpack_buffer`.
* VA-API wrapper correctly identified and skipped the direct device node (`nvidia-drm`).

---

## 🛡️ Security & Integrity

* **Non-Invasive RPM Spec:** Packages do not tamper with root filesystem libraries; binaries reside in `/opt/thorium-browser/`.
* **Reproducible Pipeline:** All builds are assembled inside official Fedora root containers and submitted to official Fedora Copr builders.
* **License:** The packaging automation is provided under the [MIT License](https://www.google.com/search?q=LICENSE). Thorium Browser remains governed by its respective upstream licenses (BSD-3-Clause / Chromium Authors).
