[speedometer-3-2026-10-07T02_33_24.235Z.json](https://github.com/user-attachments/files/33135953/speedometer-3-2026-10-07T02_33_24.235Z.json)# Thorium Browser (AVX2 & ARM64) for Fedora Copr

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

[{
    "TodoMVC-JavaScript-ES5": {
        "name": "TodoMVC-JavaScript-ES5",
        "unit": "ms",
        "description": "",
        "mean": 94.50300000309944,
        "delta": 19.81896034009664,
        "percentDelta": 20.97177903288428,
        "sum": 945.0300000309944,
        "min": 66.58500000834465,
        "max": 141.5600000023842,
        "values": [
            110.94500000029802,
            79.4550000205636,
            67.27499999850988,
            88.4750000089407,
            72.75499999523163,
            139.2449999973178,
            141.5600000023842,
            96.86000000685453,
            66.58500000834465,
            81.87499999254942
        ]
    },
    "TodoMVC-JavaScript-ES5/Adding100Items": {
        "name": "TodoMVC-JavaScript-ES5/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 60.955000000447036,
        "delta": 17.19399342001339,
        "percentDelta": 28.20768340560625,
        "sum": 609.5500000044703,
        "min": 41.230000004172325,
        "max": 109.375,
        "values": [
            69.375,
            50.94500000029802,
            43.16499999910593,
            61.10999999940395,
            43.564999997615814,
            96.64500000327826,
            109.375,
            49.935000002384186,
            41.230000004172325,
            44.20499999821186
        ]
    },
    "TodoMVC-JavaScript-ES5/Adding100Items/Sync": {
        "name": "TodoMVC-JavaScript-ES5/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 51.79949999898672,
        "delta": 15.459213843571222,
        "percentDelta": 29.844330242325945,
        "sum": 517.9949999898672,
        "min": 34.90999999642372,
        "max": 101.25,
        "values": [
            51.67000000178814,
            44.814999997615814,
            34.90999999642372,
            54.854999996721745,
            35.91999999433756,
            77.17500000447035,
            101.25,
            43.94500000029802,
            35.6600000038743,
            37.79499999433756
        ]
    },
    "TodoMVC-JavaScript-ES5/Adding100Items/Async": {
        "name": "TodoMVC-JavaScript-ES5/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 9.155500001460315,
        "delta": 3.6290042367272837,
        "percentDelta": 39.63742270928352,
        "sum": 91.55500001460314,
        "min": 5.570000000298023,
        "max": 19.469999998807907,
        "values": [
            17.70499999821186,
            6.130000002682209,
            8.255000002682209,
            6.255000002682209,
            7.6450000032782555,
            19.469999998807907,
            8.125,
            5.990000002086163,
            5.570000000298023,
            6.410000003874302
        ]
    },
    "TodoMVC-JavaScript-ES5/CompletingAllItems": {
        "name": "TodoMVC-JavaScript-ES5/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 22.18049999848008,
        "delta": 4.611125413121575,
        "percentDelta": 20.789095887998702,
        "sum": 221.80499998480082,
        "min": 14.159999996423721,
        "max": 32.1600000038743,
        "values": [
            29.174999989569187,
            17.600000008940697,
            14.159999996423721,
            16.980000004172325,
            19.684999994933605,
            27.82499999552965,
            21.74499999731779,
            32.1600000038743,
            15.195000000298023,
            27.279999993741512
        ]
    },
    "TodoMVC-JavaScript-ES5/CompletingAllItems/Sync": {
        "name": "TodoMVC-JavaScript-ES5/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 16.824999998509885,
        "delta": 3.486802321288258,
        "percentDelta": 20.72393653252344,
        "sum": 168.24999998509884,
        "min": 11.134999997913837,
        "max": 24.980000004172325,
        "values": [
            22.644999995827675,
            13.690000005066395,
            11.134999997913837,
            12.66499999910593,
            15.144999995827675,
            20.464999996125698,
            16.99499999731779,
            24.980000004172325,
            11.20499999821186,
            19.32499999552965
        ]
    },
    "TodoMVC-JavaScript-ES5/CompletingAllItems/Async": {
        "name": "TodoMVC-JavaScript-ES5/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 5.355499999970197,
        "delta": 1.2386505431296024,
        "percentDelta": 23.12856956654832,
        "sum": 53.55499999970198,
        "min": 3.024999998509884,
        "max": 7.954999998211861,
        "values": [
            6.529999993741512,
            3.910000003874302,
            3.024999998509884,
            4.315000005066395,
            4.53999999910593,
            7.3599999994039536,
            4.75,
            7.179999999701977,
            3.9900000020861626,
            7.954999998211861
        ]
    },
    "TodoMVC-JavaScript-ES5/DeletingAllItems": {
        "name": "TodoMVC-JavaScript-ES5/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 11.367500004172324,
        "delta": 1.3931912714202446,
        "percentDelta": 12.255916172499564,
        "sum": 113.67500004172325,
        "min": 9.505000002682209,
        "max": 14.774999998509884,
        "values": [
            12.395000010728836,
            10.910000011324883,
            9.950000002980232,
            10.385000005364418,
            9.505000002682209,
            14.774999998509884,
            10.440000005066395,
            14.765000000596046,
            10.160000003874302,
            10.390000000596046
        ]
    },
    "TodoMVC-JavaScript-ES5/DeletingAllItems/Sync": {
        "name": "TodoMVC-JavaScript-ES5/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 10.088500003516675,
        "delta": 1.218074688088237,
        "percentDelta": 12.073892924256702,
        "sum": 100.88500003516674,
        "min": 8.200000002980232,
        "max": 13.435000002384186,
        "values": [
            11.220000006258488,
            10.065000005066395,
            8.200000002980232,
            9.475000001490116,
            8.715000003576279,
            13.435000002384186,
            8.935000002384186,
            12.315000005066395,
            9.005000002682209,
            9.520000003278255
        ]
    },
    "TodoMVC-JavaScript-ES5/DeletingAllItems/Async": {
        "name": "TodoMVC-JavaScript-ES5/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 1.279000000655651,
        "delta": 0.3697925216701756,
        "percentDelta": 28.912628731869404,
        "sum": 12.790000006556511,
        "min": 0.7899999991059303,
        "max": 2.4499999955296516,
        "values": [
            1.1750000044703484,
            0.8450000062584877,
            1.75,
            0.9100000038743019,
            0.7899999991059303,
            1.339999996125698,
            1.505000002682209,
            2.4499999955296516,
            1.155000001192093,
            0.869999997317791
        ]
    },
    "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM": {
        "name": "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM",
        "unit": "ms",
        "description": "",
        "mean": 92.44200000017881,
        "delta": 13.317553937022987,
        "percentDelta": 14.406388802705727,
        "sum": 924.4200000017881,
        "min": 77.19499999284744,
        "max": 137.85499999672174,
        "values": [
            106.9699999988079,
            97.3049999922514,
            80.55000000447035,
            92.92500001192093,
            137.85499999672174,
            79.59000000357628,
            77.19499999284744,
            77.43500000983477,
            88.83499999344349,
            85.75999999791384
        ]
    },
    "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/Adding100Items": {
        "name": "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 55.43000000119209,
        "delta": 12.593617512637959,
        "percentDelta": 22.719858402249898,
        "sum": 554.3000000119209,
        "min": 42.24000000208616,
        "max": 101.75,
        "values": [
            65.4100000038743,
            54.05499999970198,
            48.24000000208616,
            56.24000000208616,
            101.75,
            46.71999999880791,
            45.29999999701977,
            46.42999999970198,
            42.24000000208616,
            47.91500000655651
        ]
    },
    "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/Adding100Items/Sync": {
        "name": "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 38.37700000107289,
        "delta": 3.8360389062555234,
        "percentDelta": 9.995671642255207,
        "sum": 383.77000001072884,
        "min": 33.36999999731779,
        "max": 50.57000000029802,
        "values": [
            50.57000000029802,
            41.34000000357628,
            34.6600000038743,
            42.479999996721745,
            36.17000000178814,
            34.42999999970198,
            33.36999999731779,
            35.10999999940395,
            35.185000002384186,
            40.45500000566244
        ]
    },
    "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/Adding100Items/Async": {
        "name": "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 17.05300000011921,
        "delta": 12.333482351853503,
        "percentDelta": 72.32441418968676,
        "sum": 170.5300000011921,
        "min": 7.054999999701977,
        "max": 65.57999999821186,
        "values": [
            14.840000003576279,
            12.714999996125698,
            13.57999999821186,
            13.760000005364418,
            65.57999999821186,
            12.28999999910593,
            11.929999999701977,
            11.320000000298023,
            7.054999999701977,
            7.46000000089407
        ]
    },
    "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/CompletingAllItems": {
        "name": "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 24.02199999988079,
        "delta": 3.1321927063329675,
        "percentDelta": 13.038850663344062,
        "sum": 240.2199999988079,
        "min": 20.105000004172325,
        "max": 35.15499999374151,
        "values": [
            26.20499999821186,
            22.21000000089407,
            21.275000005960464,
            23.860000006854534,
            22.924999997019768,
            21.384999997913837,
            21.424999997019768,
            20.105000004172325,
            35.15499999374151,
            25.674999997019768
        ]
    },
    "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/CompletingAllItems/Sync": {
        "name": "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 16.927499999850987,
        "delta": 2.8486527576624168,
        "percentDelta": 16.82854974265245,
        "sum": 169.27499999850988,
        "min": 13.949999995529652,
        "max": 27.759999997913837,
        "values": [
            16.91499999910593,
            14.840000003576279,
            15.350000001490116,
            16.96000000089407,
            16.139999993145466,
            13.949999995529652,
            15.804999999701977,
            14.175000004470348,
            27.759999997913837,
            17.38000000268221
        ]
    },
    "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/CompletingAllItems/Async": {
        "name": "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 7.094500000029802,
        "delta": 0.8112678875134418,
        "percentDelta": 11.435166502361461,
        "sum": 70.94500000029802,
        "min": 5.619999997317791,
        "max": 9.28999999910593,
        "values": [
            9.28999999910593,
            7.369999997317791,
            5.925000004470348,
            6.9000000059604645,
            6.785000003874302,
            7.435000002384186,
            5.619999997317791,
            5.929999999701977,
            7.394999995827675,
            8.294999994337559
        ]
    },
    "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/DeletingAllItems": {
        "name": "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 12.98999999910593,
        "delta": 2.266419661303454,
        "percentDelta": 17.447418486985732,
        "sum": 129.8999999910593,
        "min": 10.469999998807907,
        "max": 21.03999999165535,
        "values": [
            15.354999996721745,
            21.03999999165535,
            11.034999996423721,
            12.825000002980232,
            13.179999999701977,
            11.485000006854534,
            10.469999998807907,
            10.900000005960464,
            11.439999997615814,
            12.169999994337559
        ]
    },
    "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/DeletingAllItems/Sync": {
        "name": "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 10.874499999731778,
        "delta": 1.8740373362363063,
        "percentDelta": 17.233319566715988,
        "sum": 108.74499999731779,
        "min": 8.840000003576279,
        "max": 17.474999994039536,
        "values": [
            13.109999999403954,
            17.474999994039536,
            9.419999994337559,
            11.08500000089407,
            9.675000004470348,
            9.605000004172325,
            8.840000003576279,
            9.275000005960464,
            9.824999995529652,
            10.434999994933605
        ]
    },
    "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/DeletingAllItems/Async": {
        "name": "TodoMVC-JavaScript-ES6-Webpack-Complex-DOM/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 2.1154999993741512,
        "delta": 0.5524210489619211,
        "percentDelta": 26.113025248184787,
        "sum": 21.154999993741512,
        "min": 1.6150000020861626,
        "max": 3.564999997615814,
        "values": [
            2.244999997317791,
            3.564999997615814,
            1.6150000020861626,
            1.7400000020861626,
            3.5049999952316284,
            1.880000002682209,
            1.6299999952316284,
            1.625,
            1.6150000020861626,
            1.7349999994039536
        ]
    },
    "TodoMVC-WebComponents": {
        "name": "TodoMVC-WebComponents",
        "unit": "ms",
        "description": "",
        "mean": 43.38550000116229,
        "delta": 23.848741131130833,
        "percentDelta": 54.969381776150854,
        "sum": 433.8550000116229,
        "min": 26.644999980926514,
        "max": 137.64500000327826,
        "values": [
            137.64500000327826,
            29.935000002384186,
            35.270000003278255,
            39.97000001370907,
            34.33500000089407,
            32.440000005066395,
            28.480000004172325,
            34.600000001490116,
            26.644999980926514,
            34.53499999642372
        ]
    },
    "TodoMVC-WebComponents/Adding100Items": {
        "name": "TodoMVC-WebComponents/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 25.920000002533197,
        "delta": 17.738241646861333,
        "percentDelta": 68.43457424817805,
        "sum": 259.200000025332,
        "min": 14.834999993443489,
        "max": 96.23499999940395,
        "values": [
            96.23499999940395,
            16.395000003278255,
            19.469999998807907,
            20.13000001013279,
            20.765000000596046,
            16.83000000566244,
            15.615000009536743,
            20.46500000357628,
            14.834999993443489,
            18.46000000089407
        ]
    },
    "TodoMVC-WebComponents/Adding100Items/Sync": {
        "name": "TodoMVC-WebComponents/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 16.40350000113249,
        "delta": 12.842494837462086,
        "percentDelta": 78.29118685997163,
        "sum": 164.03500001132488,
        "min": 7.869999997317791,
        "max": 67.25,
        "values": [
            67.25,
            9.649999998509884,
            11.570000000298023,
            12.285000003874302,
            12.609999999403954,
            10.255000002682209,
            8.285000003874302,
            13.105000004172325,
            7.869999997317791,
            11.155000001192093
        ]
    },
    "TodoMVC-WebComponents/Adding100Items/Async": {
        "name": "TodoMVC-WebComponents/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 9.51650000140071,
        "delta": 4.9068413854141655,
        "percentDelta": 51.561407919843845,
        "sum": 95.16500001400709,
        "min": 6.575000002980232,
        "max": 28.984999999403954,
        "values": [
            28.984999999403954,
            6.745000004768372,
            7.899999998509884,
            7.845000006258488,
            8.155000001192093,
            6.575000002980232,
            7.330000005662441,
            7.3599999994039536,
            6.964999996125698,
            7.304999999701977
        ]
    },
    "TodoMVC-WebComponents/CompletingAllItems": {
        "name": "TodoMVC-WebComponents/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 10.638000000268221,
        "delta": 5.088065609428123,
        "percentDelta": 47.829155943784876,
        "sum": 106.38000000268221,
        "min": 7.074999995529652,
        "max": 30.25500000268221,
        "values": [
            30.25500000268221,
            8.104999996721745,
            9.08500000089407,
            13.005000002682209,
            7.424999997019768,
            7.465000003576279,
            7.125,
            7.795000001788139,
            7.074999995529652,
            9.04500000178814
        ]
    },
    "TodoMVC-WebComponents/CompletingAllItems/Sync": {
        "name": "TodoMVC-WebComponents/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 5.6655000008642675,
        "delta": 2.6308595503497547,
        "percentDelta": 46.43649368896689,
        "sum": 56.65500000864267,
        "min": 3.7999999970197678,
        "max": 15.840000003576279,
        "values": [
            15.840000003576279,
            4.814999997615814,
            5.240000002086163,
            6.595000006258488,
            3.875,
            3.9849999994039536,
            3.8200000002980232,
            4.450000002980232,
            3.7999999970197678,
            4.2349999994039536
        ]
    },
    "TodoMVC-WebComponents/CompletingAllItems/Async": {
        "name": "TodoMVC-WebComponents/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 4.972499999403953,
        "delta": 2.4771228867113955,
        "percentDelta": 49.81644820529562,
        "sum": 49.724999994039536,
        "min": 3.274999998509884,
        "max": 14.41499999910593,
        "values": [
            14.41499999910593,
            3.2899999991059303,
            3.844999998807907,
            6.409999996423721,
            3.5499999970197678,
            3.480000004172325,
            3.3049999997019768,
            3.344999998807907,
            3.274999998509884,
            4.810000002384186
        ]
    },
    "TodoMVC-WebComponents/DeletingAllItems": {
        "name": "TodoMVC-WebComponents/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 6.827499998360873,
        "delta": 1.2779020919849648,
        "percentDelta": 18.716984141951812,
        "sum": 68.27499998360872,
        "min": 4.734999991953373,
        "max": 11.155000001192093,
        "values": [
            11.155000001192093,
            5.435000002384186,
            6.715000003576279,
            6.83500000089407,
            6.1450000032782555,
            8.144999995827675,
            5.739999994635582,
            6.339999996125698,
            4.734999991953373,
            7.029999993741512
        ]
    },
    "TodoMVC-WebComponents/DeletingAllItems/Sync": {
        "name": "TodoMVC-WebComponents/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 6.072500000149011,
        "delta": 1.2011431793534149,
        "percentDelta": 19.78004412225509,
        "sum": 60.725000001490116,
        "min": 4.159999996423721,
        "max": 10.200000002980232,
        "values": [
            10.200000002980232,
            4.780000001192093,
            5.725000001490116,
            6.185000002384186,
            5.429999999701977,
            7.179999999701977,
            5.054999999701977,
            5.695000000298023,
            4.159999996423721,
            6.314999997615814
        ]
    },
    "TodoMVC-WebComponents/DeletingAllItems/Async": {
        "name": "TodoMVC-WebComponents/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 0.7549999982118607,
        "delta": 0.11003739802225347,
        "percentDelta": 14.574489838790152,
        "sum": 7.549999982118607,
        "min": 0.5749999955296516,
        "max": 0.9900000020861626,
        "values": [
            0.9549999982118607,
            0.6550000011920929,
            0.9900000020861626,
            0.6499999985098839,
            0.7150000035762787,
            0.9649999961256981,
            0.6849999949336052,
            0.6449999958276749,
            0.5749999955296516,
            0.7149999961256981
        ]
    },
    "TodoMVC-React-Complex-DOM": {
        "name": "TodoMVC-React-Complex-DOM",
        "unit": "ms",
        "description": "",
        "mean": 109.44949999973178,
        "delta": 32.75096092435648,
        "percentDelta": 29.923353623759574,
        "sum": 1094.4949999973178,
        "min": 75.4450000077486,
        "max": 230.3099999949336,
        "values": [
            101.8399999961257,
            130.5300000011921,
            96.97999999672174,
            230.3099999949336,
            79.47499999403954,
            115.03499999642372,
            78.04500000923872,
            90.85000000149012,
            75.4450000077486,
            95.98499999940395
        ]
    },
    "TodoMVC-React-Complex-DOM/Adding100Items": {
        "name": "TodoMVC-React-Complex-DOM/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 49.30349999964237,
        "delta": 10.346267687615716,
        "percentDelta": 20.9848543971336,
        "sum": 493.0349999964237,
        "min": 35.730000004172325,
        "max": 81.06000000238419,
        "values": [
            51.59499999880791,
            81.06000000238419,
            38.74499999731779,
            59.32000000029802,
            39.09499999880791,
            60.98499999940395,
            39.25999999791384,
            49.399999998509884,
            35.730000004172325,
            37.84499999880791
        ]
    },
    "TodoMVC-React-Complex-DOM/Adding100Items/Sync": {
        "name": "TodoMVC-React-Complex-DOM/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 42.19699999988079,
        "delta": 9.086876928261203,
        "percentDelta": 21.53441459887403,
        "sum": 421.9699999988079,
        "min": 30.780000001192093,
        "max": 71.16499999910593,
        "values": [
            44.439999997615814,
            71.16499999910593,
            33.67999999970198,
            48.94500000029802,
            33.9100000038743,
            52.350000001490116,
            33.91499999910593,
            41.48499999940395,
            30.780000001192093,
            31.299999997019768
        ]
    },
    "TodoMVC-React-Complex-DOM/Adding100Items/Async": {
        "name": "TodoMVC-React-Complex-DOM/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 7.106499999761581,
        "delta": 1.4578720458840926,
        "percentDelta": 20.51462810009151,
        "sum": 71.06499999761581,
        "min": 4.950000002980232,
        "max": 10.375,
        "values": [
            7.155000001192093,
            9.895000003278255,
            5.064999997615814,
            10.375,
            5.184999994933605,
            8.634999997913837,
            5.344999998807907,
            7.91499999910593,
            4.950000002980232,
            6.545000001788139
        ]
    },
    "TodoMVC-React-Complex-DOM/CompletingAllItems": {
        "name": "TodoMVC-React-Complex-DOM/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 41.54450000077486,
        "delta": 26.145986424249,
        "percentDelta": 62.93489252190143,
        "sum": 415.4450000077486,
        "min": 20.16500000655651,
        "max": 143.98999999463558,
        "values": [
            32.08500000089407,
            32.28999999910593,
            41.65499999374151,
            143.98999999463558,
            25.554999999701977,
            30.74499999731779,
            20.16500000655651,
            24.650000005960464,
            26.610000006854534,
            37.70000000298023
        ]
    },
    "TodoMVC-React-Complex-DOM/CompletingAllItems/Sync": {
        "name": "TodoMVC-React-Complex-DOM/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 33.82399999946356,
        "delta": 25.37256115586278,
        "percentDelta": 75.01348497003661,
        "sum": 338.2399999946356,
        "min": 14.655000001192093,
        "max": 133.52499999850988,
        "values": [
            26.314999997615814,
            26.554999999701977,
            31.809999994933605,
            133.52499999850988,
            17.524999998509884,
            21.354999996721745,
            14.655000001192093,
            18.950000002980232,
            18.450000002980232,
            29.100000001490116
        ]
    },
    "TodoMVC-React-Complex-DOM/CompletingAllItems/Async": {
        "name": "TodoMVC-React-Complex-DOM/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 7.7205000013113025,
        "delta": 1.3617039490964393,
        "percentDelta": 17.637509861604276,
        "sum": 77.20500001311302,
        "min": 5.510000005364418,
        "max": 10.464999996125698,
        "values": [
            5.7700000032782555,
            5.7349999994039536,
            9.844999998807907,
            10.464999996125698,
            8.030000001192093,
            9.390000000596046,
            5.510000005364418,
            5.700000002980232,
            8.160000003874302,
            8.600000001490116
        ]
    },
    "TodoMVC-React-Complex-DOM/DeletingAllItems": {
        "name": "TodoMVC-React-Complex-DOM/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 18.601499999314548,
        "delta": 2.921006935818359,
        "percentDelta": 15.703071988420268,
        "sum": 186.01499999314547,
        "min": 13.104999996721745,
        "max": 27,
        "values": [
            18.15999999642372,
            17.179999999701977,
            16.58000000566244,
            27,
            14.824999995529652,
            23.304999999701977,
            18.62000000476837,
            16.799999997019768,
            13.104999996721745,
            20.439999997615814
        ]
    },
    "TodoMVC-React-Complex-DOM/DeletingAllItems/Sync": {
        "name": "TodoMVC-React-Complex-DOM/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 16.22149999886751,
        "delta": 2.8506574477032722,
        "percentDelta": 17.573328285930945,
        "sum": 162.21499998867512,
        "min": 11.409999996423721,
        "max": 24.714999996125698,
        "values": [
            16.649999998509884,
            14.945000000298023,
            14.195000000298023,
            24.714999996125698,
            11.409999996423721,
            20.484999999403954,
            16.855000004172325,
            14.75,
            11.654999993741512,
            16.554999999701977
        ]
    },
    "TodoMVC-React-Complex-DOM/DeletingAllItems/Async": {
        "name": "TodoMVC-React-Complex-DOM/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 2.3800000004470347,
        "delta": 0.5677393165053422,
        "percentDelta": 23.854593125995958,
        "sum": 23.80000000447035,
        "min": 1.4500000029802322,
        "max": 3.8849999979138374,
        "values": [
            1.5099999979138374,
            2.2349999994039536,
            2.385000005364418,
            2.285000003874302,
            3.4149999991059303,
            2.8200000002980232,
            1.7650000005960464,
            2.0499999970197678,
            1.4500000029802322,
            3.8849999979138374
        ]
    },
    "TodoMVC-React-Redux": {
        "name": "TodoMVC-React-Redux",
        "unit": "ms",
        "description": "",
        "mean": 99.04799999967217,
        "delta": 32.749308999408555,
        "percentDelta": 33.06407903190064,
        "sum": 990.4799999967217,
        "min": 75.20999999344349,
        "max": 227.58999998867512,
        "values": [
            96.49000000208616,
            75.20999999344349,
            84.15000000596046,
            227.58999998867512,
            78.78500001132488,
            92.70499999821186,
            77.28499999642372,
            91.77000000327826,
            77.49999998509884,
            88.99500001221895
        ]
    },
    "TodoMVC-React-Redux/Adding100Items": {
        "name": "TodoMVC-React-Redux/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 49.21950000077486,
        "delta": 15.024133066303783,
        "percentDelta": 30.52475759824309,
        "sum": 492.1950000077486,
        "min": 37.060000002384186,
        "max": 107.1849999949336,
        "values": [
            40.690000005066395,
            37.060000002384186,
            44.32000000029802,
            107.1849999949336,
            39.50000000745058,
            44.48999999463558,
            37.1600000038743,
            51.00500000268221,
            39.45499999076128,
            51.33000000566244
        ]
    },
    "TodoMVC-React-Redux/Adding100Items/Sync": {
        "name": "TodoMVC-React-Redux/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 42.22850000038743,
        "delta": 11.134019860222773,
        "percentDelta": 26.366126810378354,
        "sum": 422.2850000038743,
        "min": 32.85999999940395,
        "max": 84.56499999761581,
        "values": [
            36.150000005960464,
            32.85999999940395,
            38.00999999791384,
            84.56499999761581,
            35.46500000357628,
            38.04500000178814,
            32.92999999970198,
            45.96999999880791,
            33.54999999701977,
            44.74000000208616
        ]
    },
    "TodoMVC-React-Redux/Adding100Items/Async": {
        "name": "TodoMVC-React-Redux/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 6.99100000038743,
        "delta": 3.9925756588978865,
        "percentDelta": 57.11022255294842,
        "sum": 69.9100000038743,
        "min": 4.035000003874302,
        "max": 22.61999999731779,
        "values": [
            4.53999999910593,
            4.200000002980232,
            6.310000002384186,
            22.61999999731779,
            4.035000003874302,
            6.444999992847443,
            4.230000004172325,
            5.035000003874302,
            5.904999993741512,
            6.590000003576279
        ]
    },
    "TodoMVC-React-Redux/CompletingAllItems": {
        "name": "TodoMVC-React-Redux/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 33.65199999958277,
        "delta": 15.612288475040655,
        "percentDelta": 46.39334504705284,
        "sum": 336.5199999958277,
        "min": 23.66499999165535,
        "max": 94.95999999344349,
        "values": [
            35.19999999552965,
            23.66499999165535,
            24.50500000268221,
            94.95999999344349,
            25.070000000298023,
            30.34000000357628,
            26.57999999821186,
            26.900000005960464,
            24.644999995827675,
            24.655000008642673
        ]
    },
    "TodoMVC-React-Redux/CompletingAllItems/Sync": {
        "name": "TodoMVC-React-Redux/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 29.15899999961257,
        "delta": 15.160568409917863,
        "percentDelta": 51.9927583597493,
        "sum": 291.5899999961257,
        "min": 19.489999994635582,
        "max": 88.68999999761581,
        "values": [
            30.714999996125698,
            19.864999994635582,
            20.679999999701977,
            88.68999999761581,
            20.63000000268221,
            25.75,
            21.980000004172325,
            23.065000005066395,
            19.489999994635582,
            20.725000001490116
        ]
    },
    "TodoMVC-React-Redux/CompletingAllItems/Async": {
        "name": "TodoMVC-React-Redux/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 4.4929999999701975,
        "delta": 0.548756889371366,
        "percentDelta": 12.213596469508257,
        "sum": 44.92999999970198,
        "min": 3.7999999970197678,
        "max": 6.269999995827675,
        "values": [
            4.4849999994039536,
            3.7999999970197678,
            3.8250000029802322,
            6.269999995827675,
            4.439999997615814,
            4.590000003576279,
            4.5999999940395355,
            3.8350000008940697,
            5.155000001192093,
            3.9300000071525574
        ]
    },
    "TodoMVC-React-Redux/DeletingAllItems": {
        "name": "TodoMVC-React-Redux/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 16.176499999314547,
        "delta": 2.879202010353957,
        "percentDelta": 17.79867097626779,
        "sum": 161.76499999314547,
        "min": 13.009999997913837,
        "max": 25.445000000298023,
        "values": [
            20.600000001490116,
            14.484999999403954,
            15.325000002980232,
            25.445000000298023,
            14.215000003576279,
            17.875,
            13.544999994337559,
            13.864999994635582,
            13.399999998509884,
            13.009999997913837
        ]
    },
    "TodoMVC-React-Redux/DeletingAllItems/Sync": {
        "name": "TodoMVC-React-Redux/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 14.909999999403954,
        "delta": 2.5927198851401414,
        "percentDelta": 17.389134039193753,
        "sum": 149.09999999403954,
        "min": 11.574999995529652,
        "max": 22.40999999642372,
        "values": [
            19.87000000476837,
            13.645000003278255,
            14.410000003874302,
            22.40999999642372,
            13.259999997913837,
            16.649999998509884,
            12.684999994933605,
            11.574999995529652,
            12.45499999821186,
            12.140000000596046
        ]
    },
    "TodoMVC-React-Redux/DeletingAllItems/Async": {
        "name": "TodoMVC-React-Redux/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 1.266499999910593,
        "delta": 0.548595875920858,
        "percentDelta": 43.31590019420335,
        "sum": 12.66499999910593,
        "min": 0.7299999967217445,
        "max": 3.035000003874302,
        "values": [
            0.7299999967217445,
            0.8399999961256981,
            0.9149999991059303,
            3.035000003874302,
            0.9550000056624413,
            1.2250000014901161,
            0.8599999994039536,
            2.2899999991059303,
            0.9450000002980232,
            0.869999997317791
        ]
    },
    "TodoMVC-Backbone": {
        "name": "TodoMVC-Backbone",
        "unit": "ms",
        "description": "",
        "mean": 67.28249999806285,
        "delta": 15.746251944736192,
        "percentDelta": 23.40319094146256,
        "sum": 672.8249999806285,
        "min": 51.04499999433756,
        "max": 113.97999999672174,
        "values": [
            113.97999999672174,
            51.04499999433756,
            52.37499998509884,
            82.7699999883771,
            94.5650000050664,
            56.33500000834465,
            59.270000003278255,
            56.650000005960464,
            53.144999995827675,
            52.689999997615814
        ]
    },
    "TodoMVC-Backbone/Adding100Items": {
        "name": "TodoMVC-Backbone/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 34.90999999716878,
        "delta": 13.062958305438604,
        "percentDelta": 37.418958196786065,
        "sum": 349.0999999716878,
        "min": 24.964999996125698,
        "max": 84.9299999922514,
        "values": [
            84.9299999922514,
            25.099999994039536,
            24.964999996125698,
            38.40499999374151,
            36.63000000268221,
            27.450000002980232,
            33.09000000357628,
            26.484999999403954,
            26.679999992251396,
            25.364999994635582
        ]
    },
    "TodoMVC-Backbone/Adding100Items/Sync": {
        "name": "TodoMVC-Backbone/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 29.52749999985099,
        "delta": 12.453699946435417,
        "percentDelta": 42.176614838703806,
        "sum": 295.2749999985099,
        "min": 19.90999999642372,
        "max": 77.36499999463558,
        "values": [
            77.36499999463558,
            19.90999999642372,
            20.030000001192093,
            31.594999998807907,
            31.74500000476837,
            22.50500000268221,
            27.645000003278255,
            21.875,
            21.86999999731779,
            20.734999999403954
        ]
    },
    "TodoMVC-Backbone/Adding100Items/Async": {
        "name": "TodoMVC-Backbone/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 5.382499997317791,
        "delta": 0.714241717519645,
        "percentDelta": 13.269702143531187,
        "sum": 53.82499997317791,
        "min": 4.6099999994039536,
        "max": 7.564999997615814,
        "values": [
            7.564999997615814,
            5.189999997615814,
            4.934999994933605,
            6.809999994933605,
            4.884999997913837,
            4.945000000298023,
            5.445000000298023,
            4.6099999994039536,
            4.809999994933605,
            4.629999995231628
        ]
    },
    "TodoMVC-Backbone/CompletingAllItems": {
        "name": "TodoMVC-Backbone/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 18.386500000953674,
        "delta": 3.787183854149839,
        "percentDelta": 20.597633339425148,
        "sum": 183.86500000953674,
        "min": 14.71000000089407,
        "max": 31.92000000178814,
        "values": [
            16.78999999910593,
            14.71000000089407,
            16.11999999731779,
            23.104999996721745,
            31.92000000178814,
            16.975000001490116,
            16.524999998509884,
            16.83000000566244,
            14.975000001490116,
            15.915000006556511
        ]
    },
    "TodoMVC-Backbone/CompletingAllItems/Sync": {
        "name": "TodoMVC-Backbone/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 12.845500000566243,
        "delta": 2.5068613846115695,
        "percentDelta": 19.515483122502545,
        "sum": 128.45500000566244,
        "min": 10.140000000596046,
        "max": 21.725000001490116,
        "values": [
            12.134999997913837,
            10.140000000596046,
            11.83500000089407,
            15.979999996721745,
            21.725000001490116,
            11.58500000089407,
            12.144999995827675,
            11.005000002682209,
            10.520000003278255,
            11.385000005364418
        ]
    },
    "TodoMVC-Backbone/CompletingAllItems/Async": {
        "name": "TodoMVC-Backbone/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 5.54100000038743,
        "delta": 1.3303637422034604,
        "percentDelta": 24.009452122549007,
        "sum": 55.4100000038743,
        "min": 4.284999996423721,
        "max": 10.195000000298023,
        "values": [
            4.655000001192093,
            4.570000000298023,
            4.284999996423721,
            7.125,
            10.195000000298023,
            5.3900000005960464,
            4.380000002682209,
            5.825000002980232,
            4.454999998211861,
            4.530000001192093
        ]
    },
    "TodoMVC-Backbone/DeletingAllItems": {
        "name": "TodoMVC-Backbone/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 13.985999999940395,
        "delta": 3.7836625461373736,
        "percentDelta": 27.05321425821177,
        "sum": 139.85999999940395,
        "min": 9.655000001192093,
        "max": 26.015000000596046,
        "values": [
            12.260000005364418,
            11.234999999403954,
            11.28999999165535,
            21.259999997913837,
            26.015000000596046,
            11.910000003874302,
            9.655000001192093,
            13.33500000089407,
            11.490000002086163,
            11.409999996423721
        ]
    },
    "TodoMVC-Backbone/DeletingAllItems/Sync": {
        "name": "TodoMVC-Backbone/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 12.619500000029802,
        "delta": 3.7510387902298263,
        "percentDelta": 29.724147471936035,
        "sum": 126.19500000029802,
        "min": 8.54500000178814,
        "max": 24.660000003874302,
        "values": [
            11.215000003576279,
            9.759999997913837,
            10.199999995529652,
            19.600000001490116,
            24.660000003874302,
            9.814999997615814,
            8.54500000178814,
            12.28999999910593,
            10.16499999910593,
            9.945000000298023
        ]
    },
    "TodoMVC-Backbone/DeletingAllItems/Async": {
        "name": "TodoMVC-Backbone/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 1.3664999999105931,
        "delta": 0.23715545360023357,
        "percentDelta": 17.354954527314312,
        "sum": 13.66499999910593,
        "min": 1.0450000017881393,
        "max": 2.0950000062584877,
        "values": [
            1.0450000017881393,
            1.4750000014901161,
            1.089999996125698,
            1.6599999964237213,
            1.3549999967217445,
            2.0950000062584877,
            1.1099999994039536,
            1.0450000017881393,
            1.3250000029802322,
            1.464999996125698
        ]
    },
    "TodoMVC-Angular-Complex-DOM": {
        "name": "TodoMVC-Angular-Complex-DOM",
        "unit": "ms",
        "description": "",
        "mean": 79.36450000032782,
        "delta": 7.9914785834579725,
        "percentDelta": 10.069336521272058,
        "sum": 793.6450000032783,
        "min": 68.6900000050664,
        "max": 97.72499999403954,
        "values": [
            97.72499999403954,
            68.6900000050664,
            73.67000000178814,
            90.68999999761581,
            88.70500000566244,
            90.67000000178814,
            72.45000000298023,
            68.9649999961257,
            70.08499999344349,
            71.99500000476837
        ]
    },
    "TodoMVC-Angular-Complex-DOM/Adding100Items": {
        "name": "TodoMVC-Angular-Complex-DOM/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 50.80749999955297,
        "delta": 5.6120529813249,
        "percentDelta": 11.045717623134925,
        "sum": 508.07499999552965,
        "min": 41.65499999374151,
        "max": 65.81499999761581,
        "values": [
            65.81499999761581,
            47.71999999880791,
            46.940000005066395,
            57.189999997615814,
            60.5350000038743,
            51.024999998509884,
            45.24500000476837,
            41.65499999374151,
            47.894999995827675,
            44.05499999970198
        ]
    },
    "TodoMVC-Angular-Complex-DOM/Adding100Items/Sync": {
        "name": "TodoMVC-Angular-Complex-DOM/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 44.76199999973178,
        "delta": 4.953595047259032,
        "percentDelta": 11.066518581137382,
        "sum": 447.6199999973178,
        "min": 36.314999997615814,
        "max": 56.54500000178814,
        "values": [
            56.54500000178814,
            42.19500000029802,
            41.53999999910593,
            51.35999999940395,
            54.32999999821186,
            44.82000000029802,
            39.92000000178814,
            36.314999997615814,
            42.03000000119209,
            38.564999997615814
        ]
    },
    "TodoMVC-Angular-Complex-DOM/Adding100Items/Async": {
        "name": "TodoMVC-Angular-Complex-DOM/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 6.045499999821186,
        "delta": 0.8444148073716164,
        "percentDelta": 13.967658711381896,
        "sum": 60.45499999821186,
        "min": 5.325000002980232,
        "max": 9.269999995827675,
        "values": [
            9.269999995827675,
            5.524999998509884,
            5.4000000059604645,
            5.829999998211861,
            6.205000005662441,
            6.204999998211861,
            5.325000002980232,
            5.339999996125698,
            5.864999994635582,
            5.490000002086163
        ]
    },
    "TodoMVC-Angular-Complex-DOM/CompletingAllItems": {
        "name": "TodoMVC-Angular-Complex-DOM/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 17.434000001102685,
        "delta": 2.771076562353416,
        "percentDelta": 15.894668820569851,
        "sum": 174.34000001102686,
        "min": 11.17000000178814,
        "max": 24.530000001192093,
        "values": [
            20.91999999433756,
            11.17000000178814,
            16.70499999821186,
            18.054999999701977,
            18.445000000298023,
            24.530000001192093,
            17.690000005066395,
            17.145000003278255,
            11.859999999403954,
            17.820000007748604
        ]
    },
    "TodoMVC-Angular-Complex-DOM/CompletingAllItems/Sync": {
        "name": "TodoMVC-Angular-Complex-DOM/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 9.538000001013279,
        "delta": 1.636996382575155,
        "percentDelta": 17.162889310140983,
        "sum": 95.38000001013279,
        "min": 6.605000004172325,
        "max": 14.344999998807907,
        "values": [
            12.449999995529652,
            6.605000004172325,
            8.375,
            9.185000002384186,
            9.33500000089407,
            14.344999998807907,
            9.484999999403954,
            8.895000003278255,
            7.304999999701977,
            9.400000005960464
        ]
    },
    "TodoMVC-Angular-Complex-DOM/CompletingAllItems/Async": {
        "name": "TodoMVC-Angular-Complex-DOM/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 7.896000000089407,
        "delta": 1.3262115012923787,
        "percentDelta": 16.795991657514715,
        "sum": 78.96000000089407,
        "min": 4.554999999701977,
        "max": 10.185000002384186,
        "values": [
            8.469999998807907,
            4.564999997615814,
            8.32999999821186,
            8.869999997317791,
            9.109999999403954,
            10.185000002384186,
            8.205000005662441,
            8.25,
            4.554999999701977,
            8.42000000178814
        ]
    },
    "TodoMVC-Angular-Complex-DOM/DeletingAllItems": {
        "name": "TodoMVC-Angular-Complex-DOM/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 11.122999999672174,
        "delta": 1.593925732758563,
        "percentDelta": 14.329998496858225,
        "sum": 111.22999999672174,
        "min": 9.514999993145466,
        "max": 15.445000000298023,
        "values": [
            10.990000002086163,
            9.800000004470348,
            10.024999998509884,
            15.445000000298023,
            9.725000001490116,
            15.115000002086163,
            9.514999993145466,
            10.16499999910593,
            10.32999999821186,
            10.119999997317791
        ]
    },
    "TodoMVC-Angular-Complex-DOM/DeletingAllItems/Sync": {
        "name": "TodoMVC-Angular-Complex-DOM/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 9.924000000953674,
        "delta": 1.397036158143418,
        "percentDelta": 14.07734943580377,
        "sum": 99.24000000953674,
        "min": 8.549999997019768,
        "max": 14.03999999910593,
        "values": [
            10.030000001192093,
            8.825000002980232,
            8.67000000178814,
            14.03999999910593,
            8.645000003278255,
            12.975000001490116,
            8.549999997019768,
            9.010000005364418,
            9.314999997615814,
            9.179999999701977
        ]
    },
    "TodoMVC-Angular-Complex-DOM/DeletingAllItems/Async": {
        "name": "TodoMVC-Angular-Complex-DOM/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 1.1989999987185,
        "delta": 0.264600391609672,
        "percentDelta": 22.068423010215085,
        "sum": 11.989999987185001,
        "min": 0.9399999976158142,
        "max": 2.1400000005960464,
        "values": [
            0.9600000008940697,
            0.9750000014901161,
            1.3549999967217445,
            1.405000001192093,
            1.0799999982118607,
            2.1400000005960464,
            0.9649999961256981,
            1.1549999937415123,
            1.0150000005960464,
            0.9399999976158142
        ]
    },
    "TodoMVC-Vue": {
        "name": "TodoMVC-Vue",
        "unit": "ms",
        "description": "",
        "mean": 46.278999998420474,
        "delta": 7.147472855860433,
        "percentDelta": 15.444311363911018,
        "sum": 462.78999998420477,
        "min": 37.935000009834766,
        "max": 64.80499998480082,
        "values": [
            62.59500000625849,
            37.935000009834766,
            40.91999999433756,
            45.770000003278255,
            41.58499999344349,
            51.145000010728836,
            64.80499998480082,
            39.90999999642372,
            38.98999999463558,
            39.13499999046326
        ]
    },
    "TodoMVC-Vue/Adding100Items": {
        "name": "TodoMVC-Vue/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 25.657000000029804,
        "delta": 4.767928179845924,
        "percentDelta": 18.58334247901308,
        "sum": 256.570000000298,
        "min": 21.07499999552965,
        "max": 43.060000002384186,
        "values": [
            43.060000002384186,
            22.060000002384186,
            22.695000000298023,
            25.440000005066395,
            23.094999998807907,
            30.390000008046627,
            24.03499999642372,
            23.015000000596046,
            21.07499999552965,
            21.70499999076128
        ]
    },
    "TodoMVC-Vue/Adding100Items/Sync": {
        "name": "TodoMVC-Vue/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 4.922999999672174,
        "delta": 2.5881703705390966,
        "percentDelta": 52.57303210870291,
        "sum": 49.229999996721745,
        "min": 2.764999993145466,
        "max": 14.969999998807907,
        "values": [
            14.969999998807907,
            3.1200000047683716,
            3.6150000020861626,
            3.9849999994039536,
            4.034999996423721,
            5.760000005364418,
            3.844999998807907,
            3.4200000017881393,
            2.764999993145466,
            3.714999996125698
        ]
    },
    "TodoMVC-Vue/Adding100Items/Async": {
        "name": "TodoMVC-Vue/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 20.73400000035763,
        "delta": 2.3065176574593016,
        "percentDelta": 11.124325539787392,
        "sum": 207.34000000357628,
        "min": 17.989999994635582,
        "max": 28.09000000357628,
        "values": [
            28.09000000357628,
            18.939999997615814,
            19.07999999821186,
            21.45500000566244,
            19.060000002384186,
            24.63000000268221,
            20.189999997615814,
            19.594999998807907,
            18.310000002384186,
            17.989999994635582
        ]
    },
    "TodoMVC-Vue/CompletingAllItems": {
        "name": "TodoMVC-Vue/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 10.927999999374151,
        "delta": 0.734965491159823,
        "percentDelta": 6.725526090793509,
        "sum": 109.27999999374151,
        "min": 9.745000004768372,
        "max": 12.83500000834465,
        "values": [
            12.109999999403954,
            9.745000004768372,
            11.57999999076128,
            10.530000001192093,
            11.559999994933605,
            12.83500000834465,
            9.969999998807907,
            10.284999996423721,
            10.479999996721745,
            10.185000002384186
        ]
    },
    "TodoMVC-Vue/CompletingAllItems/Sync": {
        "name": "TodoMVC-Vue/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 1.6559999994933605,
        "delta": 0.20086544493120764,
        "percentDelta": 12.129555857044732,
        "sum": 16.559999994933605,
        "min": 1.3949999958276749,
        "max": 2.155000001192093,
        "values": [
            1.8149999976158142,
            1.4250000044703484,
            1.6999999955296516,
            1.4600000008940697,
            2.094999998807907,
            2.155000001192093,
            1.4149999991059303,
            1.5399999991059303,
            1.3949999958276749,
            1.5600000023841858
        ]
    },
    "TodoMVC-Vue/CompletingAllItems/Async": {
        "name": "TodoMVC-Vue/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 9.27199999988079,
        "delta": 0.5657106462001744,
        "percentDelta": 6.101279618285674,
        "sum": 92.7199999988079,
        "min": 8.320000000298023,
        "max": 10.680000007152557,
        "values": [
            10.29500000178814,
            8.320000000298023,
            9.879999995231628,
            9.070000000298023,
            9.464999996125698,
            10.680000007152557,
            8.554999999701977,
            8.744999997317791,
            9.08500000089407,
            8.625
        ]
    },
    "TodoMVC-Vue/DeletingAllItems": {
        "name": "TodoMVC-Vue/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 9.693999999016523,
        "delta": 5.3533458793813535,
        "percentDelta": 55.22329151974893,
        "sum": 96.93999999016523,
        "min": 6.130000002682209,
        "max": 30.799999989569187,
        "values": [
            7.425000004470348,
            6.130000002682209,
            6.6450000032782555,
            9.799999997019768,
            6.929999999701977,
            7.919999994337559,
            30.799999989569187,
            6.6099999994039536,
            7.435000002384186,
            7.244999997317791
        ]
    },
    "TodoMVC-Vue/DeletingAllItems/Sync": {
        "name": "TodoMVC-Vue/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 5.429500000178814,
        "delta": 3.2710106413472206,
        "percentDelta": 60.24515408858078,
        "sum": 54.29500000178814,
        "min": 3.505000002682209,
        "max": 18.29499999433756,
        "values": [
            4.045000001788139,
            3.505000002682209,
            3.6950000002980232,
            5.804999999701977,
            3.630000002682209,
            4.364999994635582,
            18.29499999433756,
            3.530000001192093,
            3.6500000059604645,
            3.774999998509884
        ]
    },
    "TodoMVC-Vue/DeletingAllItems/Async": {
        "name": "TodoMVC-Vue/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 4.264499998837709,
        "delta": 2.090704738524747,
        "percentDelta": 49.02578823061482,
        "sum": 42.644999988377094,
        "min": 2.625,
        "max": 12.504999995231628,
        "values": [
            3.380000002682209,
            2.625,
            2.9500000029802322,
            3.994999997317791,
            3.2999999970197678,
            3.5549999997019768,
            12.504999995231628,
            3.0799999982118607,
            3.7849999964237213,
            3.469999998807907
        ]
    },
    "TodoMVC-jQuery": {
        "name": "TodoMVC-jQuery",
        "unit": "ms",
        "description": "",
        "mean": 304.6270000003278,
        "delta": 33.16220772526445,
        "percentDelta": 10.886168240250786,
        "sum": 3046.2700000032783,
        "min": 251.4050000011921,
        "max": 374.625,
        "values": [
            312.64500000327826,
            292.00499998778105,
            253.12500000745058,
            367.00500001758337,
            374.625,
            349.2749999985099,
            251.4050000011921,
            279.7449999898672,
            308.8400000035763,
            257.59999999403954
        ]
    },
    "TodoMVC-jQuery/Adding100Items": {
        "name": "TodoMVC-jQuery/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 77.7820000000298,
        "delta": 11.575114502342627,
        "percentDelta": 14.881482222542738,
        "sum": 777.820000000298,
        "min": 62.42499999701977,
        "max": 101.48000000417233,
        "values": [
            90.39000000059605,
            62.894999995827675,
            65.91499999910593,
            101.48000000417233,
            97.4100000038743,
            94.74499999731779,
            62.54500000178814,
            67.60999999940395,
            72.4050000011921,
            62.42499999701977
        ]
    },
    "TodoMVC-jQuery/Adding100Items/Sync": {
        "name": "TodoMVC-jQuery/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 69.93499999940396,
        "delta": 10.392275833585504,
        "percentDelta": 14.859906818723209,
        "sum": 699.3499999940395,
        "min": 56.78499999642372,
        "max": 95.27000000327826,
        "values": [
            84.6550000011921,
            57.019999995827675,
            60.33500000089407,
            95.27000000327826,
            72.74000000208616,
            88.33499999344349,
            56.80499999970198,
            61.20499999821186,
            66.20000000298023,
            56.78499999642372
        ]
    },
    "TodoMVC-jQuery/Adding100Items/Async": {
        "name": "TodoMVC-jQuery/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 7.847000000625849,
        "delta": 4.234341315566989,
        "percentDelta": 53.96127584082162,
        "sum": 78.47000000625849,
        "min": 5.579999998211861,
        "max": 24.67000000178814,
        "values": [
            5.7349999994039536,
            5.875,
            5.579999998211861,
            6.21000000089407,
            24.67000000178814,
            6.410000003874302,
            5.740000002086163,
            6.405000001192093,
            6.204999998211861,
            5.6400000005960464
        ]
    },
    "TodoMVC-jQuery/CompletingAllItems": {
        "name": "TodoMVC-jQuery/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 140.5910000011325,
        "delta": 13.508810070627382,
        "percentDelta": 9.608588082109499,
        "sum": 1405.9100000113249,
        "min": 119.3449999988079,
        "max": 172.1950000077486,
        "values": [
            141.7149999961257,
            154.35499999672174,
            123.73000000417233,
            148.0700000077486,
            165.1899999976158,
            172.1950000077486,
            119.3449999988079,
            128.57999999821186,
            132.45500000566244,
            120.27499999850988
        ]
    },
    "TodoMVC-jQuery/CompletingAllItems/Sync": {
        "name": "TodoMVC-jQuery/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 129.0689999997616,
        "delta": 11.07279339059101,
        "percentDelta": 8.578972015442487,
        "sum": 1290.6899999976158,
        "min": 110.23999999463558,
        "max": 155.62999999523163,
        "values": [
            133.09999999403954,
            144.54500000178814,
            113.39500000327826,
            139.92500000447035,
            155.62999999523163,
            138.17000000178814,
            110.23999999463558,
            119.3449999988079,
            123.74000000208616,
            112.60000000149012
        ]
    },
    "TodoMVC-jQuery/CompletingAllItems/Async": {
        "name": "TodoMVC-jQuery/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 11.522000001370907,
        "delta": 5.683874529648992,
        "percentDelta": 49.33062427506261,
        "sum": 115.22000001370907,
        "min": 7.674999997019768,
        "max": 34.025000005960464,
        "values": [
            8.615000002086163,
            9.809999994933605,
            10.33500000089407,
            8.145000003278255,
            9.560000002384186,
            34.025000005960464,
            9.105000004172325,
            9.234999999403954,
            8.715000003576279,
            7.674999997019768
        ]
    },
    "TodoMVC-jQuery/DeletingAllItems": {
        "name": "TodoMVC-jQuery/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 86.25399999916553,
        "delta": 13.205909469079616,
        "percentDelta": 15.310489332909055,
        "sum": 862.5399999916553,
        "min": 63.480000004172325,
        "max": 117.45500000566244,
        "values": [
            80.54000000655651,
            74.75499999523163,
            63.480000004172325,
            117.45500000566244,
            112.02499999850988,
            82.33499999344349,
            69.51500000059605,
            83.5549999922514,
            103.97999999672174,
            74.89999999850988
        ]
    },
    "TodoMVC-jQuery/DeletingAllItems/Sync": {
        "name": "TodoMVC-jQuery/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 82.16499999910593,
        "delta": 11.983176812872449,
        "percentDelta": 14.584283834969686,
        "sum": 821.6499999910593,
        "min": 61.24000000208616,
        "max": 110.5300000011921,
        "values": [
            77.01500000059605,
            72.53999999910593,
            61.24000000208616,
            110.5300000011921,
            106.76999999582767,
            80.04999999701977,
            67.2199999988079,
            81.26999999582767,
            95.3449999988079,
            69.67000000178814
        ]
    },
    "TodoMVC-jQuery/DeletingAllItems/Async": {
        "name": "TodoMVC-jQuery/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 4.089000000059604,
        "delta": 1.6579978496906107,
        "percentDelta": 40.54775861253222,
        "sum": 40.89000000059605,
        "min": 2.214999996125698,
        "max": 8.634999997913837,
        "values": [
            3.5250000059604645,
            2.214999996125698,
            2.2400000020861626,
            6.925000004470348,
            5.255000002682209,
            2.2849999964237213,
            2.2950000017881393,
            2.2849999964237213,
            8.634999997913837,
            5.2299999967217445
        ]
    },
    "TodoMVC-Preact-Complex-DOM": {
        "name": "TodoMVC-Preact-Complex-DOM",
        "unit": "ms",
        "description": "",
        "mean": 22.87000000104308,
        "delta": 2.7493868998561743,
        "percentDelta": 12.021805420772965,
        "sum": 228.7000000104308,
        "min": 19.879999987781048,
        "max": 31.00500000268221,
        "values": [
            31.00500000268221,
            28.820000000298023,
            22.189999997615814,
            21.75000000745058,
            19.879999987781048,
            20.08500000834465,
            22.21000000834465,
            20.42000000923872,
            21.774999991059303,
            20.564999997615814
        ]
    },
    "TodoMVC-Preact-Complex-DOM/Adding100Items": {
        "name": "TodoMVC-Preact-Complex-DOM/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 11.776500002294778,
        "delta": 1.883810063143821,
        "percentDelta": 15.996349193535773,
        "sum": 117.76500002294779,
        "min": 9.780000001192093,
        "max": 16.730000004172325,
        "values": [
            16.450000002980232,
            16.730000004172325,
            10.580000005662441,
            10.71000000089407,
            10.339999996125698,
            9.785000003874302,
            10.620000004768372,
            9.780000001192093,
            12.33500000089407,
            10.435000002384186
        ]
    },
    "TodoMVC-Preact-Complex-DOM/Adding100Items/Sync": {
        "name": "TodoMVC-Preact-Complex-DOM/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 1.783500000089407,
        "delta": 0.44533174640027073,
        "percentDelta": 24.969540026798217,
        "sum": 17.83500000089407,
        "min": 1.244999997317791,
        "max": 3.064999997615814,
        "values": [
            3.064999997615814,
            1.8049999997019768,
            1.7050000056624413,
            1.3149999976158142,
            1.3650000020861626,
            1.3550000041723251,
            1.5399999991059303,
            1.244999997317791,
            2.7349999994039536,
            1.7049999982118607
        ]
    },
    "TodoMVC-Preact-Complex-DOM/Adding100Items/Async": {
        "name": "TodoMVC-Preact-Complex-DOM/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 9.993000002205372,
        "delta": 1.6106752010180168,
        "percentDelta": 16.118034630867147,
        "sum": 99.93000002205372,
        "min": 8.429999999701977,
        "max": 14.925000004470348,
        "values": [
            13.385000005364418,
            14.925000004470348,
            8.875,
            9.395000003278255,
            8.974999994039536,
            8.429999999701977,
            9.080000005662441,
            8.535000003874302,
            9.600000001490116,
            8.730000004172325
        ]
    },
    "TodoMVC-Preact-Complex-DOM/CompletingAllItems": {
        "name": "TodoMVC-Preact-Complex-DOM/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 8.468500001728534,
        "delta": 0.7376583200574226,
        "percentDelta": 8.71061368491299,
        "sum": 84.68500001728535,
        "min": 7.254999995231628,
        "max": 10.58500000089407,
        "values": [
            10.58500000089407,
            9.54500000178814,
            8.824999995529652,
            8.495000004768372,
            7.254999995231628,
            7.855000004172325,
            8.695000007748604,
            8.38000001013279,
            7.284999996423721,
            7.7650000005960464
        ]
    },
    "TodoMVC-Preact-Complex-DOM/CompletingAllItems/Sync": {
        "name": "TodoMVC-Preact-Complex-DOM/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 1.2290000028908252,
        "delta": 0.20181151118393403,
        "percentDelta": 16.420790130938787,
        "sum": 12.290000028908253,
        "min": 1,
        "max": 1.9700000062584877,
        "values": [
            1.9700000062584877,
            1.2250000014901161,
            1.2100000008940697,
            1.385000005364418,
            1.1400000005960464,
            1.1050000041723251,
            1.135000005364418,
            1.0800000056624413,
            1,
            1.0399999991059303
        ]
    },
    "TodoMVC-Preact-Complex-DOM/CompletingAllItems/Async": {
        "name": "TodoMVC-Preact-Complex-DOM/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 7.23949999883771,
        "delta": 0.5842578544497249,
        "percentDelta": 8.070417218641158,
        "sum": 72.3949999883771,
        "min": 6.114999994635582,
        "max": 8.614999994635582,
        "values": [
            8.614999994635582,
            8.320000000298023,
            7.614999994635582,
            7.1099999994039536,
            6.114999994635582,
            6.75,
            7.560000002384186,
            7.300000004470348,
            6.284999996423721,
            6.725000001490116
        ]
    },
    "TodoMVC-Preact-Complex-DOM/DeletingAllItems": {
        "name": "TodoMVC-Preact-Complex-DOM/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 2.624999997019768,
        "delta": 0.37627513706884314,
        "percentDelta": 14.33429095223003,
        "sum": 26.249999970197678,
        "min": 2.1549999937415123,
        "max": 3.969999998807907,
        "values": [
            3.969999998807907,
            2.5449999943375587,
            2.7849999964237213,
            2.5450000017881393,
            2.2849999964237213,
            2.4450000002980232,
            2.894999995827675,
            2.2599999979138374,
            2.1549999937415123,
            2.364999994635582
        ]
    },
    "TodoMVC-Preact-Complex-DOM/DeletingAllItems/Sync": {
        "name": "TodoMVC-Preact-Complex-DOM/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 0.8609999977052212,
        "delta": 0.1723368417374443,
        "percentDelta": 20.015893402643993,
        "sum": 8.609999977052212,
        "min": 0.6499999985098839,
        "max": 1.4499999955296516,
        "values": [
            1.4499999955296516,
            0.869999997317791,
            1.0700000002980232,
            0.8549999967217445,
            0.6599999964237213,
            0.8299999982118607,
            0.7849999964237213,
            0.7100000008940697,
            0.6499999985098839,
            0.7299999967217445
        ]
    },
    "TodoMVC-Preact-Complex-DOM/DeletingAllItems/Async": {
        "name": "TodoMVC-Preact-Complex-DOM/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 1.7639999993145465,
        "delta": 0.22344518775175543,
        "percentDelta": 12.66696076182435,
        "sum": 17.639999993145466,
        "min": 1.5049999952316284,
        "max": 2.5200000032782555,
        "values": [
            2.5200000032782555,
            1.6749999970197678,
            1.714999996125698,
            1.6900000050663948,
            1.625,
            1.6150000020861626,
            2.1099999994039536,
            1.5499999970197678,
            1.5049999952316284,
            1.6349999979138374
        ]
    },
    "TodoMVC-Svelte-Complex-DOM": {
        "name": "TodoMVC-Svelte-Complex-DOM",
        "unit": "ms",
        "description": "",
        "mean": 26.07750000357628,
        "delta": 8.542550403068562,
        "percentDelta": 32.75831809758233,
        "sum": 260.7750000357628,
        "min": 17.50499999523163,
        "max": 57.860000014305115,
        "values": [
            23.339999988675117,
            57.860000014305115,
            32.275000005960464,
            19.964999996125698,
            18.62500000745058,
            20.510000012815,
            26.08500000834465,
            17.50499999523163,
            21.424999989569187,
            23.185000017285347
        ]
    },
    "TodoMVC-Svelte-Complex-DOM/Adding100Items": {
        "name": "TodoMVC-Svelte-Complex-DOM/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 14.230000001937151,
        "delta": 5.0587352978609,
        "percentDelta": 35.549791266143686,
        "sum": 142.3000000193715,
        "min": 9.109999999403954,
        "max": 31.760000005364418,
        "values": [
            12.945000000298023,
            31.760000005364418,
            21.12000000476837,
            9.855000004172325,
            10.570000000298023,
            10.75,
            14.325000002980232,
            9.109999999403954,
            10.214999996125698,
            11.650000005960464
        ]
    },
    "TodoMVC-Svelte-Complex-DOM/Adding100Items/Sync": {
        "name": "TodoMVC-Svelte-Complex-DOM/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 2.238499999791384,
        "delta": 0.5509539251912173,
        "percentDelta": 24.612639054838652,
        "sum": 22.384999997913837,
        "min": 1.4500000029802322,
        "max": 4.090000003576279,
        "values": [
            2.399999998509884,
            4.090000003576279,
            2.7100000008940697,
            1.4500000029802322,
            1.844999998807907,
            1.6749999970197678,
            2.2400000020861626,
            1.4849999994039536,
            2.2549999952316284,
            2.2349999994039536
        ]
    },
    "TodoMVC-Svelte-Complex-DOM/Adding100Items/Async": {
        "name": "TodoMVC-Svelte-Complex-DOM/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 11.991500002145767,
        "delta": 4.543816077874099,
        "percentDelta": 37.891974123846275,
        "sum": 119.91500002145767,
        "min": 7.625,
        "max": 27.67000000178814,
        "values": [
            10.54500000178814,
            27.67000000178814,
            18.410000003874302,
            8.405000001192093,
            8.725000001490116,
            9.075000002980232,
            12.08500000089407,
            7.625,
            7.96000000089407,
            9.415000006556511
        ]
    },
    "TodoMVC-Svelte-Complex-DOM/CompletingAllItems": {
        "name": "TodoMVC-Svelte-Complex-DOM/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 9.002500002086162,
        "delta": 3.2052463303661036,
        "percentDelta": 35.60395811855982,
        "sum": 90.02500002086163,
        "min": 5.910000003874302,
        "max": 21.385000005364418,
        "values": [
            7.394999995827675,
            21.385000005364418,
            7.620000004768372,
            6.954999998211861,
            5.910000003874302,
            7.5300000086426735,
            8.71000000089407,
            6.394999995827675,
            8.909999996423721,
            9.21500001102686
        ]
    },
    "TodoMVC-Svelte-Complex-DOM/CompletingAllItems/Sync": {
        "name": "TodoMVC-Svelte-Complex-DOM/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 1.2180000007152558,
        "delta": 0.21840979797352986,
        "percentDelta": 17.931838903552656,
        "sum": 12.180000007152557,
        "min": 0.8400000035762787,
        "max": 1.9500000029802322,
        "values": [
            1.25,
            1.9500000029802322,
            1.3900000005960464,
            1.089999996125698,
            0.8400000035762787,
            1.0650000050663948,
            1.1950000002980232,
            1.0099999979138374,
            1.0449999943375587,
            1.3450000062584877
        ]
    },
    "TodoMVC-Svelte-Complex-DOM/CompletingAllItems/Async": {
        "name": "TodoMVC-Svelte-Complex-DOM/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 7.7845000013709065,
        "delta": 3.0112725896779025,
        "percentDelta": 38.682928757757026,
        "sum": 77.84500001370907,
        "min": 5.070000000298023,
        "max": 19.435000002384186,
        "values": [
            6.144999995827675,
            19.435000002384186,
            6.230000004172325,
            5.865000002086163,
            5.070000000298023,
            6.465000003576279,
            7.5150000005960464,
            5.384999997913837,
            7.865000002086163,
            7.870000004768372
        ]
    },
    "TodoMVC-Svelte-Complex-DOM/DeletingAllItems": {
        "name": "TodoMVC-Svelte-Complex-DOM/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 2.8449999995529653,
        "delta": 0.5980376646875485,
        "percentDelta": 21.020656055589388,
        "sum": 28.44999999552965,
        "min": 2,
        "max": 4.715000003576279,
        "values": [
            2.9999999925494194,
            4.715000003576279,
            3.5349999964237213,
            3.1549999937415123,
            2.1450000032782555,
            2.230000004172325,
            3.0500000044703484,
            2,
            2.2999999970197678,
            2.3200000002980232
        ]
    },
    "TodoMVC-Svelte-Complex-DOM/DeletingAllItems/Sync": {
        "name": "TodoMVC-Svelte-Complex-DOM/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 0.8524999998509883,
        "delta": 0.13192953080080624,
        "percentDelta": 15.475604788723366,
        "sum": 8.524999998509884,
        "min": 0.630000002682209,
        "max": 1.219999998807907,
        "values": [
            0.9349999949336052,
            1.219999998807907,
            0.9900000020861626,
            0.9399999976158142,
            0.6649999991059303,
            0.7400000020861626,
            0.9450000002980232,
            0.630000002682209,
            0.7599999979138374,
            0.7000000029802322
        ]
    },
    "TodoMVC-Svelte-Complex-DOM/DeletingAllItems/Async": {
        "name": "TodoMVC-Svelte-Complex-DOM/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 1.9924999997019768,
        "delta": 0.46947630769233917,
        "percentDelta": 23.56217353889887,
        "sum": 19.924999997019768,
        "min": 1.369999997317791,
        "max": 3.4950000047683716,
        "values": [
            2.064999997615814,
            3.4950000047683716,
            2.5449999943375587,
            2.214999996125698,
            1.4800000041723251,
            1.4900000020861626,
            2.105000004172325,
            1.369999997317791,
            1.5399999991059303,
            1.619999997317791
        ]
    },
    "TodoMVC-Lit-Complex-DOM": {
        "name": "TodoMVC-Lit-Complex-DOM",
        "unit": "ms",
        "description": "",
        "mean": 28.008000002801417,
        "delta": 2.2797230635907177,
        "percentDelta": 8.139542499866806,
        "sum": 280.0800000280142,
        "min": 24.560000009834766,
        "max": 33.37999998778105,
        "values": [
            32.9750000089407,
            28.88500002026558,
            24.560000009834766,
            29.19999998807907,
            25.24999999254942,
            27.950000002980232,
            33.37999998778105,
            24.79000000655651,
            27.424999989569187,
            25.665000021457672
        ]
    },
    "TodoMVC-Lit-Complex-DOM/Adding100Items": {
        "name": "TodoMVC-Lit-Complex-DOM/Adding100Items",
        "unit": "ms",
        "description": "",
        "mean": 16.388000002503397,
        "delta": 1.7703618455396986,
        "percentDelta": 10.802793783678679,
        "sum": 163.88000002503395,
        "min": 13.885000005364418,
        "max": 20.719999998807907,
        "values": [
            20.110000006854534,
            16.530000008642673,
            13.905000001192093,
            17.49499999731779,
            14.159999996423721,
            15.225000001490116,
            20.719999998807907,
            13.885000005364418,
            16.945000000298023,
            14.905000008642673
        ]
    },
    "TodoMVC-Lit-Complex-DOM/Adding100Items/Sync": {
        "name": "TodoMVC-Lit-Complex-DOM/Adding100Items/Sync",
        "unit": "ms",
        "description": "",
        "mean": 1.8845000013709068,
        "delta": 0.31005881068683205,
        "percentDelta": 16.453107480035833,
        "sum": 18.84500001370907,
        "min": 1.4450000002980232,
        "max": 2.8700000047683716,
        "values": [
            2.8700000047683716,
            1.4500000029802322,
            1.4450000002980232,
            1.619999997317791,
            1.9900000020861626,
            1.719999998807907,
            2.0549999997019768,
            1.535000003874302,
            2.1099999994039536,
            2.0500000044703484
        ]
    },
    "TodoMVC-Lit-Complex-DOM/Adding100Items/Async": {
        "name": "TodoMVC-Lit-Complex-DOM/Adding100Items/Async",
        "unit": "ms",
        "description": "",
        "mean": 14.503500001132489,
        "delta": 1.6014161909503448,
        "percentDelta": 11.04158438187541,
        "sum": 145.03500001132488,
        "min": 12.169999994337559,
        "max": 18.66499999910593,
        "values": [
            17.240000002086163,
            15.080000005662441,
            12.46000000089407,
            15.875,
            12.169999994337559,
            13.505000002682209,
            18.66499999910593,
            12.350000001490116,
            14.83500000089407,
            12.855000004172325
        ]
    },
    "TodoMVC-Lit-Complex-DOM/CompletingAllItems": {
        "name": "TodoMVC-Lit-Complex-DOM/CompletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 8.067999999970198,
        "delta": 0.4792185003946585,
        "percentDelta": 5.939743435751471,
        "sum": 80.67999999970198,
        "min": 7.309999994933605,
        "max": 9.32999999821186,
        "values": [
            9.094999998807907,
            8.425000004470348,
            7.570000007748604,
            7.9749999940395355,
            7.695000000298023,
            9.32999999821186,
            7.824999995529652,
            7.7650000005960464,
            7.309999994933605,
            7.690000005066395
        ]
    },
    "TodoMVC-Lit-Complex-DOM/CompletingAllItems/Sync": {
        "name": "TodoMVC-Lit-Complex-DOM/CompletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 2.025000000745058,
        "delta": 0.20225617870462947,
        "percentDelta": 9.987959438529055,
        "sum": 20.25000000745058,
        "min": 1.6349999979138374,
        "max": 2.6799999997019768,
        "values": [
            2.0700000002980232,
            2.0250000059604645,
            2.285000003874302,
            1.8849999979138374,
            1.8900000005960464,
            2.6799999997019768,
            1.8999999985098839,
            1.9600000008940697,
            1.6349999979138374,
            1.9200000017881393
        ]
    },
    "TodoMVC-Lit-Complex-DOM/CompletingAllItems/Async": {
        "name": "TodoMVC-Lit-Complex-DOM/CompletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 6.04299999922514,
        "delta": 0.36741465846511134,
        "percentDelta": 6.080004277878915,
        "sum": 60.429999992251396,
        "min": 5.285000003874302,
        "max": 7.024999998509884,
        "values": [
            7.024999998509884,
            6.399999998509884,
            5.285000003874302,
            6.089999996125698,
            5.804999999701977,
            6.649999998509884,
            5.924999997019768,
            5.804999999701977,
            5.674999997019768,
            5.7700000032782555
        ]
    },
    "TodoMVC-Lit-Complex-DOM/DeletingAllItems": {
        "name": "TodoMVC-Lit-Complex-DOM/DeletingAllItems",
        "unit": "ms",
        "description": "",
        "mean": 3.5520000003278254,
        "delta": 0.3906223980473469,
        "percentDelta": 10.997252196263938,
        "sum": 35.520000003278255,
        "min": 3.070000007748604,
        "max": 4.834999993443489,
        "values": [
            3.7700000032782555,
            3.9300000071525574,
            3.0850000008940697,
            3.7299999967217445,
            3.394999995827675,
            3.3950000032782555,
            4.834999993443489,
            3.1400000005960464,
            3.1699999943375587,
            3.070000007748604
        ]
    },
    "TodoMVC-Lit-Complex-DOM/DeletingAllItems/Sync": {
        "name": "TodoMVC-Lit-Complex-DOM/DeletingAllItems/Sync",
        "unit": "ms",
        "description": "",
        "mean": 1.6015000000596047,
        "delta": 0.18668735270213185,
        "percentDelta": 11.65703107681447,
        "sum": 16.015000000596046,
        "min": 1.3200000002980232,
        "max": 2.144999995827675,
        "values": [
            1.6050000041723251,
            1.7950000017881393,
            1.3200000002980232,
            1.8350000008940697,
            1.584999993443489,
            1.5800000056624413,
            2.144999995827675,
            1.405000001192093,
            1.4049999937415123,
            1.3400000035762787
        ]
    },
    "TodoMVC-Lit-Complex-DOM/DeletingAllItems/Async": {
        "name": "TodoMVC-Lit-Complex-DOM/DeletingAllItems/Async",
        "unit": "ms",
        "description": "",
        "mean": 1.950500000268221,
        "delta": 0.21749835315459215,
        "percentDelta": 11.150902492934279,
        "sum": 19.50500000268221,
        "min": 1.7300000041723251,
        "max": 2.689999997615814,
        "values": [
            2.1649999991059303,
            2.135000005364418,
            1.7650000005960464,
            1.8949999958276749,
            1.8100000023841858,
            1.8149999976158142,
            2.689999997615814,
            1.7349999994039536,
            1.7650000005960464,
            1.7300000041723251
        ]
    },
    "NewsSite-Next": {
        "name": "NewsSite-Next",
        "unit": "ms",
        "description": "",
        "mean": 219.08750000447034,
        "delta": 20.408312884421974,
        "percentDelta": 9.315142527075054,
        "sum": 2190.8750000447035,
        "min": 181.17000000178814,
        "max": 253.01999999582767,
        "values": [
            237.10999999940395,
            197.5949999988079,
            253.01999999582767,
            225.89000000804663,
            182.010000012815,
            227.87500000745058,
            181.17000000178814,
            190.8250000104308,
            250.51500000059605,
            244.86500000953674
        ]
    },
    "NewsSite-Next/NavigateToUS": {
        "name": "NewsSite-Next/NavigateToUS",
        "unit": "ms",
        "description": "",
        "mean": 79.14600000157952,
        "delta": 13.582054993634491,
        "percentDelta": 17.160759853136526,
        "sum": 791.4600000157952,
        "min": 65.23500000685453,
        "max": 119.59000000357628,
        "values": [
            107.24499999731779,
            66.00999999046326,
            74.0300000011921,
            81.64500000327826,
            65.23500000685453,
            69.48499999940395,
            65.42999999970198,
            68.3150000050664,
            119.59000000357628,
            74.4750000089407
        ]
    },
    "NewsSite-Next/NavigateToUS/Sync": {
        "name": "NewsSite-Next/NavigateToUS/Sync",
        "unit": "ms",
        "description": "",
        "mean": 38.66200000047684,
        "delta": 9.458713294920807,
        "percentDelta": 24.465142245109277,
        "sum": 386.6200000047684,
        "min": 29.760000005364418,
        "max": 71.7149999961257,
        "values": [
            71.7149999961257,
            31.989999994635582,
            31.314999997615814,
            38.39000000059605,
            29.760000005364418,
            32.66499999910593,
            30.375,
            31.560000002384186,
            50.815000005066395,
            38.0350000038743
        ]
    },
    "NewsSite-Next/NavigateToUS/Async": {
        "name": "NewsSite-Next/NavigateToUS/Async",
        "unit": "ms",
        "description": "",
        "mean": 40.484000001102686,
        "delta": 7.455630395604901,
        "percentDelta": 18.416239490667493,
        "sum": 404.84000001102686,
        "min": 34.019999995827675,
        "max": 68.77499999850988,
        "values": [
            35.53000000119209,
            34.019999995827675,
            42.71500000357628,
            43.25500000268221,
            35.475000001490116,
            36.82000000029802,
            35.05499999970198,
            36.75500000268221,
            68.77499999850988,
            36.440000005066395
        ]
    },
    "NewsSite-Next/NavigateToWorld": {
        "name": "NewsSite-Next/NavigateToWorld",
        "unit": "ms",
        "description": "",
        "mean": 73.27850000113249,
        "delta": 12.453798200448709,
        "percentDelta": 16.99515983577208,
        "sum": 732.7850000113249,
        "min": 57.70499999821186,
        "max": 107.0899999961257,
        "values": [
            62.355000004172325,
            60.67000000178814,
            84.96000000089407,
            74.16500000655651,
            58.95499999821186,
            95.65500000864267,
            57.70499999821186,
            58.435000002384186,
            72.79499999433756,
            107.0899999961257
        ]
    },
    "NewsSite-Next/NavigateToWorld/Sync": {
        "name": "NewsSite-Next/NavigateToWorld/Sync",
        "unit": "ms",
        "description": "",
        "mean": 33.08500000014901,
        "delta": 3.9512058062523607,
        "percentDelta": 11.942589712058531,
        "sum": 330.8500000014901,
        "min": 26.384999997913837,
        "max": 43.15500000119209,
        "values": [
            32.89000000059605,
            29.354999996721745,
            38.89000000059605,
            34.28000000119209,
            27.140000000596046,
            36.84000000357628,
            26.384999997913837,
            27.740000002086163,
            34.17499999701977,
            43.15500000119209
        ]
    },
    "NewsSite-Next/NavigateToWorld/Async": {
        "name": "NewsSite-Next/NavigateToWorld/Async",
        "unit": "ms",
        "description": "",
        "mean": 40.19350000098348,
        "delta": 8.860072087414371,
        "percentDelta": 22.0435445711311,
        "sum": 401.93500000983477,
        "min": 29.46500000357628,
        "max": 63.934999994933605,
        "values": [
            29.46500000357628,
            31.315000005066395,
            46.07000000029802,
            39.88500000536442,
            31.814999997615814,
            58.815000005066395,
            31.320000000298023,
            30.695000000298023,
            38.61999999731779,
            63.934999994933605
        ]
    },
    "NewsSite-Next/NavigateToPolitics": {
        "name": "NewsSite-Next/NavigateToPolitics",
        "unit": "ms",
        "description": "",
        "mean": 66.66300000175833,
        "delta": 7.683624221331519,
        "percentDelta": 11.526070265557884,
        "sum": 666.6300000175834,
        "min": 57.820000007748604,
        "max": 94.02999999374151,
        "values": [
            67.50999999791384,
            70.91500000655651,
            94.02999999374151,
            70.07999999821186,
            57.820000007748604,
            62.73499999940395,
            58.0350000038743,
            64.07500000298023,
            58.13000000268221,
            63.30000000447035
        ]
    },
    "NewsSite-Next/NavigateToPolitics/Sync": {
        "name": "NewsSite-Next/NavigateToPolitics/Sync",
        "unit": "ms",
        "description": "",
        "mean": 29.74250000119209,
        "delta": 3.3321077961728314,
        "percentDelta": 11.203186672402385,
        "sum": 297.42500001192093,
        "min": 24.615000002086163,
        "max": 40.51500000059605,
        "values": [
            31.95499999821186,
            26.185000002384186,
            40.51500000059605,
            33.44500000029802,
            24.615000002086163,
            28.50499999523163,
            26.035000003874302,
            28.05000000447035,
            27.92000000178814,
            30.200000002980232
        ]
    },
    "NewsSite-Next/NavigateToPolitics/Async": {
        "name": "NewsSite-Next/NavigateToPolitics/Async",
        "unit": "ms",
        "description": "",
        "mean": 36.92050000056624,
        "delta": 5.024477780417624,
        "percentDelta": 13.608910443630407,
        "sum": 369.20500000566244,
        "min": 30.21000000089407,
        "max": 53.514999993145466,
        "values": [
            35.55499999970198,
            44.730000004172325,
            53.514999993145466,
            36.63499999791384,
            33.20500000566244,
            34.230000004172325,
            32,
            36.024999998509884,
            30.21000000089407,
            33.100000001490116
        ]
    },
    "NewsSite-Nuxt": {
        "name": "NewsSite-Nuxt",
        "unit": "ms",
        "description": "",
        "mean": 177.19049999788405,
        "delta": 32.96537581613668,
        "percentDelta": 18.60448264242741,
        "sum": 1771.9049999788404,
        "min": 141.99999999254942,
        "max": 264.25999999791384,
        "values": [
            247.86499999463558,
            141.99999999254942,
            211.36500000208616,
            264.25999999791384,
            150.62000000476837,
            150.66499999910593,
            151.12999999523163,
            147.20499999821186,
            151.16499999910593,
            155.62999999523163
        ]
    },
    "NewsSite-Nuxt/NavigateToUS": {
        "name": "NewsSite-Nuxt/NavigateToUS",
        "unit": "ms",
        "description": "",
        "mean": 71.94999999925494,
        "delta": 23.51020371745677,
        "percentDelta": 32.67575221362088,
        "sum": 719.4999999925494,
        "min": 47.69500000029802,
        "max": 146.86499999463558,
        "values": [
            146.86499999463558,
            50.65999999642372,
            96.14000000059605,
            103.46000000089407,
            51.32999999821186,
            56.375,
            59.020000003278255,
            47.69500000029802,
            55.99499999731779,
            51.96000000089407
        ]
    },
    "NewsSite-Nuxt/NavigateToUS/Sync": {
        "name": "NewsSite-Nuxt/NavigateToUS/Sync",
        "unit": "ms",
        "description": "",
        "mean": 32.36449999958277,
        "delta": 18.116993116370203,
        "percentDelta": 55.97797931870958,
        "sum": 323.6449999958277,
        "min": 17.609999999403954,
        "max": 100.62999999523163,
        "values": [
            100.62999999523163,
            20.66499999910593,
            38.28999999910593,
            40.394999995827675,
            17.935000002384186,
            24.695000000298023,
            23.84000000357628,
            17.609999999403954,
            18.695000000298023,
            20.890000000596046
        ]
    },
    "NewsSite-Nuxt/NavigateToUS/Async": {
        "name": "NewsSite-Nuxt/NavigateToUS/Async",
        "unit": "ms",
        "description": "",
        "mean": 39.58549999967217,
        "delta": 8.628206789973822,
        "percentDelta": 21.796381983416342,
        "sum": 395.85499999672174,
        "min": 29.99499999731779,
        "max": 63.065000005066395,
        "values": [
            46.23499999940395,
            29.99499999731779,
            57.850000001490116,
            63.065000005066395,
            33.394999995827675,
            31.679999999701977,
            35.17999999970198,
            30.08500000089407,
            37.29999999701977,
            31.070000000298023
        ]
    },
    "NewsSite-Nuxt/NavigateToWorld": {
        "name": "NewsSite-Nuxt/NavigateToWorld",
        "unit": "ms",
        "description": "",
        "mean": 52.27799999937415,
        "delta": 10.387078035060377,
        "percentDelta": 19.868927723296082,
        "sum": 522.7799999937415,
        "min": 43.87999999523163,
        "max": 91.4699999988079,
        "values": [
            49.42500000447035,
            45.07000000029802,
            58.439999997615814,
            91.4699999988079,
            47.83500000089407,
            44.355000004172325,
            44.57000000029802,
            43.87999999523163,
            45.144999995827675,
            52.5899999961257
        ]
    },
    "NewsSite-Nuxt/NavigateToWorld/Sync": {
        "name": "NewsSite-Nuxt/NavigateToWorld/Sync",
        "unit": "ms",
        "description": "",
        "mean": 22.833000000566244,
        "delta": 6.080148501858283,
        "percentDelta": 26.628776339979414,
        "sum": 228.33000000566244,
        "min": 17.234999999403954,
        "max": 44.605000004172325,
        "values": [
            21.475000001490116,
            18.03999999910593,
            27.890000000596046,
            44.605000004172325,
            19.67000000178814,
            17.234999999403954,
            17.770000003278255,
            17.890000000596046,
            17.844999998807907,
            25.90999999642372
        ]
    },
    "NewsSite-Nuxt/NavigateToWorld/Async": {
        "name": "NewsSite-Nuxt/NavigateToWorld/Async",
        "unit": "ms",
        "description": "",
        "mean": 29.44499999880791,
        "delta": 4.467198476499712,
        "percentDelta": 15.171331216439357,
        "sum": 294.44999998807907,
        "min": 25.989999994635582,
        "max": 46.86499999463558,
        "values": [
            27.950000002980232,
            27.030000001192093,
            30.549999997019768,
            46.86499999463558,
            28.16499999910593,
            27.12000000476837,
            26.799999997019768,
            25.989999994635582,
            27.299999997019768,
            26.679999999701977
        ]
    },
    "NewsSite-Nuxt/NavigateToPolitics": {
        "name": "NewsSite-Nuxt/NavigateToPolitics",
        "unit": "ms",
        "description": "",
        "mean": 52.962499999254945,
        "delta": 4.705137696533461,
        "percentDelta": 8.883904076657354,
        "sum": 529.6249999925494,
        "min": 46.269999995827675,
        "max": 69.32999999821186,
        "values": [
            51.57499999552965,
            46.269999995827675,
            56.7850000038743,
            69.32999999821186,
            51.45500000566244,
            49.934999994933605,
            47.53999999165535,
            55.63000000268221,
            50.025000005960464,
            51.07999999821186
        ]
    },
    "NewsSite-Nuxt/NavigateToPolitics/Sync": {
        "name": "NewsSite-Nuxt/NavigateToPolitics/Sync",
        "unit": "ms",
        "description": "",
        "mean": 21.554499999433755,
        "delta": 3.5961262732098107,
        "percentDelta": 16.68387702477108,
        "sum": 215.54499999433756,
        "min": 18.820000000298023,
        "max": 35.30499999970198,
        "values": [
            19.384999997913837,
            20.07499999552965,
            23.46000000089407,
            35.30499999970198,
            21.21000000089407,
            18.90999999642372,
            19.69999999552965,
            19.355000004172325,
            19.325000002980232,
            18.820000000298023
        ]
    },
    "NewsSite-Nuxt/NavigateToPolitics/Async": {
        "name": "NewsSite-Nuxt/NavigateToPolitics/Async",
        "unit": "ms",
        "description": "",
        "mean": 31.407999999821186,
        "delta": 2.0985861678273476,
        "percentDelta": 6.681693096788384,
        "sum": 314.07999999821186,
        "min": 26.195000000298023,
        "max": 36.274999998509884,
        "values": [
            32.189999997615814,
            26.195000000298023,
            33.32500000298023,
            34.024999998509884,
            30.24500000476837,
            31.024999998509884,
            27.839999996125698,
            36.274999998509884,
            30.700000002980232,
            32.25999999791384
        ]
    },
    "Editor-CodeMirror": {
        "name": "Editor-CodeMirror",
        "unit": "ms",
        "description": "",
        "mean": 50.21650000065565,
        "delta": 10.355137444144592,
        "percentDelta": 20.620986018558426,
        "sum": 502.1650000065565,
        "min": 38.73499999940395,
        "max": 88.01500001549721,
        "values": [
            88.01500001549721,
            45.29999999701977,
            54.1600000038743,
            52.65499999374151,
            52.57000000029802,
            41.71999999880791,
            38.73499999940395,
            48.40500000119209,
            41.315000005066395,
            39.28999999165535
        ]
    },
    "Editor-CodeMirror/Long": {
        "name": "Editor-CodeMirror/Long",
        "unit": "ms",
        "description": "",
        "mean": 23.764500001072882,
        "delta": 7.792826696435531,
        "percentDelta": 32.7918815716035,
        "sum": 237.64500001072884,
        "min": 16.979999996721745,
        "max": 53.885000012815,
        "values": [
            53.885000012815,
            22.08500000089407,
            24.484999999403954,
            24.15999999642372,
            19.424999997019768,
            18.524999998509884,
            18.070000000298023,
            21.50500000268221,
            18.525000005960464,
            16.979999996721745
        ]
    },
    "Editor-CodeMirror/Long/Sync": {
        "name": "Editor-CodeMirror/Long/Sync",
        "unit": "ms",
        "description": "",
        "mean": 15.440999999642372,
        "delta": 6.257869548815437,
        "percentDelta": 40.52761834700068,
        "sum": 154.40999999642372,
        "min": 10.679999999701977,
        "max": 39.650000005960464,
        "values": [
            39.650000005960464,
            14.294999994337559,
            15.41499999910593,
            16.625,
            11.899999998509884,
            11.07999999821186,
            10.679999999701977,
            12.344999998807907,
            11.615000002086163,
            10.804999999701977
        ]
    },
    "Editor-CodeMirror/Long/Async": {
        "name": "Editor-CodeMirror/Long/Async",
        "unit": "ms",
        "description": "",
        "mean": 8.323500001430512,
        "delta": 1.6173324406734355,
        "percentDelta": 19.430917767711588,
        "sum": 83.23500001430511,
        "min": 6.174999997019768,
        "max": 14.235000006854534,
        "values": [
            14.235000006854534,
            7.790000006556511,
            9.070000000298023,
            7.534999996423721,
            7.524999998509884,
            7.445000000298023,
            7.3900000005960464,
            9.160000003874302,
            6.910000003874302,
            6.174999997019768
        ]
    },
    "Editor-CodeMirror/Highlight": {
        "name": "Editor-CodeMirror/Highlight",
        "unit": "ms",
        "description": "",
        "mean": 26.451999999582767,
        "delta": 3.402875437676029,
        "percentDelta": 12.864340835209827,
        "sum": 264.5199999958277,
        "min": 20.66499999910593,
        "max": 34.13000000268221,
        "values": [
            34.13000000268221,
            23.214999996125698,
            29.67500000447035,
            28.49499999731779,
            33.145000003278255,
            23.195000000298023,
            20.66499999910593,
            26.899999998509884,
            22.78999999910593,
            22.309999994933605
        ]
    },
    "Editor-CodeMirror/Highlight/Sync": {
        "name": "Editor-CodeMirror/Highlight/Sync",
        "unit": "ms",
        "description": "",
        "mean": 23.789499999582766,
        "delta": 3.164506395458966,
        "percentDelta": 13.302113938983446,
        "sum": 237.89499999582767,
        "min": 18.484999999403954,
        "max": 31.490000002086163,
        "values": [
            31.490000002086163,
            21.089999996125698,
            26.365000002086163,
            25.489999994635582,
            29.935000002384186,
            20.759999997913837,
            18.484999999403954,
            23.740000002086163,
            20.54500000178814,
            19.99499999731779
        ]
    },
    "Editor-CodeMirror/Highlight/Async": {
        "name": "Editor-CodeMirror/Highlight/Async",
        "unit": "ms",
        "description": "",
        "mean": 2.6625,
        "delta": 0.3332248044164512,
        "percentDelta": 12.51548561188549,
        "sum": 26.625,
        "min": 2.125,
        "max": 3.310000002384186,
        "values": [
            2.6400000005960464,
            2.125,
            3.310000002384186,
            3.005000002682209,
            3.2100000008940697,
            2.435000002384186,
            2.1799999997019768,
            3.1599999964237213,
            2.244999997317791,
            2.314999997615814
        ]
    },
    "Editor-TipTap": {
        "name": "Editor-TipTap",
        "unit": "ms",
        "description": "",
        "mean": 132.1804999984801,
        "delta": 35.68287936580173,
        "percentDelta": 26.99556997152533,
        "sum": 1321.8049999848008,
        "min": 97.875,
        "max": 267.945000000298,
        "values": [
            267.945000000298,
            113.29999999701977,
            146.14000000059605,
            119.44499999284744,
            124.9100000038743,
            98.81000000238419,
            113.27499999850988,
            131.29500000178814,
            108.80999998748302,
            97.875
        ]
    },
    "Editor-TipTap/Long": {
        "name": "Editor-TipTap/Long",
        "unit": "ms",
        "description": "",
        "mean": 66.66149999797344,
        "delta": 11.180991153939168,
        "percentDelta": 16.77278662238185,
        "sum": 666.6149999797344,
        "min": 50.684999994933605,
        "max": 106.83499999344349,
        "values": [
            106.83499999344349,
            64.94500000029802,
            71.56499999761581,
            65.51500000059605,
            68.73499999940395,
            51.19999999552965,
            61.560000002384186,
            63.73499999940395,
            61.8399999961257,
            50.684999994933605
        ]
    },
    "Editor-TipTap/Long/Sync": {
        "name": "Editor-TipTap/Long/Sync",
        "unit": "ms",
        "description": "",
        "mean": 59.87449999898672,
        "delta": 11.64281177793351,
        "percentDelta": 19.445359507186772,
        "sum": 598.7449999898672,
        "min": 49.16999999433756,
        "max": 103.87999999523163,
        "values": [
            103.87999999523163,
            55.05499999970198,
            62.49000000208616,
            63.70499999821186,
            58.350000001490116,
            49.66499999910593,
            53.375,
            51.725000001490116,
            51.32999999821186,
            49.16999999433756
        ]
    },
    "Editor-TipTap/Long/Async": {
        "name": "Editor-TipTap/Long/Async",
        "unit": "ms",
        "description": "",
        "mean": 6.786999998986721,
        "delta": 3.069801226550666,
        "percentDelta": 45.23060596742269,
        "sum": 67.86999998986721,
        "min": 1.5150000005960464,
        "max": 12.009999997913837,
        "values": [
            2.9549999982118607,
            9.890000000596046,
            9.074999995529652,
            1.8100000023841858,
            10.384999997913837,
            1.5349999964237213,
            8.185000002384186,
            12.009999997913837,
            10.509999997913837,
            1.5150000005960464
        ]
    },
    "Editor-TipTap/Highlight": {
        "name": "Editor-TipTap/Highlight",
        "unit": "ms",
        "description": "",
        "mean": 65.51900000050664,
        "delta": 24.93090718958205,
        "percentDelta": 38.051415908956585,
        "sum": 655.1900000050664,
        "min": 46.96999999135733,
        "max": 161.11000000685453,
        "values": [
            161.11000000685453,
            48.354999996721745,
            74.57500000298023,
            53.929999992251396,
            56.17500000447035,
            47.610000006854534,
            51.7149999961257,
            67.56000000238419,
            46.96999999135733,
            47.190000005066395
        ]
    },
    "Editor-TipTap/Highlight/Sync": {
        "name": "Editor-TipTap/Highlight/Sync",
        "unit": "ms",
        "description": "",
        "mean": 61.295000000298025,
        "delta": 24.765796993020697,
        "percentDelta": 40.40426950469089,
        "sum": 612.9500000029802,
        "min": 42.54499999433756,
        "max": 156.27000000327826,
        "values": [
            156.27000000327826,
            44.29500000178814,
            70.46000000089407,
            50.2149999961257,
            51.88000000268221,
            43.45000000298023,
            47.67499999701977,
            62.875,
            42.54499999433756,
            43.2850000038743
        ]
    },
    "Editor-TipTap/Highlight/Async": {
        "name": "Editor-TipTap/Highlight/Async",
        "unit": "ms",
        "description": "",
        "mean": 4.224000000208616,
        "delta": 0.2472314422118326,
        "percentDelta": 5.853017097528936,
        "sum": 42.24000000208616,
        "min": 3.714999996125698,
        "max": 4.840000003576279,
        "values": [
            4.840000003576279,
            4.059999994933605,
            4.115000002086163,
            3.714999996125698,
            4.295000001788139,
            4.160000003874302,
            4.03999999910593,
            4.685000002384186,
            4.424999997019768,
            3.905000001192093
        ]
    },
    "Charts-observable-plot": {
        "name": "Charts-observable-plot",
        "unit": "ms",
        "description": "",
        "mean": 106.25949999839068,
        "delta": 18.798211344467354,
        "percentDelta": 17.690852436489966,
        "sum": 1062.5949999839067,
        "min": 87.23499999940395,
        "max": 174.91999999433756,
        "values": [
            111.74000000208616,
            94.40999998897314,
            119.53000000864267,
            102.90499998629093,
            98.8550000116229,
            87.23499999940395,
            95.2749999910593,
            174.91999999433756,
            89.01000000536442,
            88.7149999961257
        ]
    },
    "Charts-observable-plot/Stacked by 6": {
        "name": "Charts-observable-plot/Stacked by 6",
        "unit": "ms",
        "description": "",
        "mean": 51.402000000327824,
        "delta": 16.07176317440518,
        "percentDelta": 31.266805132684876,
        "sum": 514.0200000032783,
        "min": 35.55000000447035,
        "max": 111.13499999791384,
        "values": [
            60.235000006854534,
            43.66499999910593,
            52.730000004172325,
            52.40499999374151,
            42.91499999910593,
            35.55000000447035,
            40.83499999344349,
            111.13499999791384,
            37.274999998509884,
            37.275000005960464
        ]
    },
    "Charts-observable-plot/Stacked by 6/Sync": {
        "name": "Charts-observable-plot/Stacked by 6/Sync",
        "unit": "ms",
        "description": "",
        "mean": 41.068999999016526,
        "delta": 9.654741583978407,
        "percentDelta": 23.508586973653138,
        "sum": 410.68999999016523,
        "min": 30.134999997913837,
        "max": 74.32999999821186,
        "values": [
            52.96500000357628,
            35.684999994933605,
            42.480000004172325,
            41.314999997615814,
            35.82499999552965,
            30.134999997913837,
            33.434999994933605,
            74.32999999821186,
            32.274999998509884,
            32.24500000476837
        ]
    },
    "Charts-observable-plot/Stacked by 6/Async": {
        "name": "Charts-observable-plot/Stacked by 6/Async",
        "unit": "ms",
        "description": "",
        "mean": 10.333000001311301,
        "delta": 6.8121200469018754,
        "percentDelta": 65.92586902194317,
        "sum": 103.33000001311302,
        "min": 5,
        "max": 36.80499999970198,
        "values": [
            7.2700000032782555,
            7.980000004172325,
            10.25,
            11.089999996125698,
            7.090000003576279,
            5.415000006556511,
            7.399999998509884,
            36.80499999970198,
            5,
            5.030000001192093
        ]
    },
    "Charts-observable-plot/Stacked by 20": {
        "name": "Charts-observable-plot/Stacked by 20",
        "unit": "ms",
        "description": "",
        "mean": 38.53599999919534,
        "delta": 3.416767388772614,
        "percentDelta": 8.866429802895887,
        "sum": 385.3599999919534,
        "min": 33.89000000059605,
        "max": 48.560000002384186,
        "values": [
            33.89000000059605,
            35.82000000029802,
            48.560000002384186,
            34.4649999961257,
            40.75000000745058,
            36.26500000059605,
            36.8399999961257,
            44.86999999731779,
            37.729999996721745,
            36.16999999433756
        ]
    },
    "Charts-observable-plot/Stacked by 20/Sync": {
        "name": "Charts-observable-plot/Stacked by 20/Sync",
        "unit": "ms",
        "description": "",
        "mean": 30.212000000476838,
        "delta": 2.0781442900420215,
        "percentDelta": 6.8785392890547525,
        "sum": 302.1200000047684,
        "min": 26.815000005066395,
        "max": 35.89000000059605,
        "values": [
            26.815000005066395,
            28.41499999910593,
            35.89000000059605,
            27.04500000178814,
            33.5350000038743,
            29.219999998807907,
            29.314999997615814,
            32.524999998509884,
            29.969999998807907,
            29.390000000596046
        ]
    },
    "Charts-observable-plot/Stacked by 20/Async": {
        "name": "Charts-observable-plot/Stacked by 20/Async",
        "unit": "ms",
        "description": "",
        "mean": 8.3239999987185,
        "delta": 1.590390759474648,
        "percentDelta": 19.106087935121245,
        "sum": 83.239999987185,
        "min": 6.779999993741512,
        "max": 12.67000000178814,
        "values": [
            7.074999995529652,
            7.405000001192093,
            12.67000000178814,
            7.419999994337559,
            7.215000003576279,
            7.045000001788139,
            7.524999998509884,
            12.344999998807907,
            7.759999997913837,
            6.779999993741512
        ]
    },
    "Charts-observable-plot/Dotted": {
        "name": "Charts-observable-plot/Dotted",
        "unit": "ms",
        "description": "",
        "mean": 16.321499998867512,
        "delta": 1.175734262651325,
        "percentDelta": 7.20359196601357,
        "sum": 163.21499998867512,
        "min": 14.00500001013279,
        "max": 18.91499999910593,
        "values": [
            17.614999994635582,
            14.924999989569187,
            18.240000002086163,
            16.03499999642372,
            15.190000005066395,
            15.419999994337559,
            17.600000001490116,
            18.91499999910593,
            14.00500001013279,
            15.269999995827675
        ]
    },
    "Charts-observable-plot/Dotted/Sync": {
        "name": "Charts-observable-plot/Dotted/Sync",
        "unit": "ms",
        "description": "",
        "mean": 10.22449999973178,
        "delta": 0.9795201474105601,
        "percentDelta": 9.580127609528642,
        "sum": 102.24499999731779,
        "min": 7.860000006854534,
        "max": 12.409999996423721,
        "values": [
            12.409999996423721,
            9.519999995827675,
            11.719999998807907,
            10.134999997913837,
            9.575000002980232,
            10.219999998807907,
            9.155000001192093,
            11.685000002384186,
            7.860000006854534,
            9.964999996125698
        ]
    },
    "Charts-observable-plot/Dotted/Async": {
        "name": "Charts-observable-plot/Dotted/Async",
        "unit": "ms",
        "description": "",
        "mean": 6.096999999135733,
        "delta": 0.7523749640194504,
        "percentDelta": 12.340084699460418,
        "sum": 60.96999999135733,
        "min": 5.199999995529652,
        "max": 8.445000000298023,
        "values": [
            5.204999998211861,
            5.404999993741512,
            6.5200000032782555,
            5.899999998509884,
            5.615000002086163,
            5.199999995529652,
            8.445000000298023,
            7.2299999967217445,
            6.1450000032782555,
            5.304999999701977
        ]
    },
    "Charts-chartjs": {
        "name": "Charts-chartjs",
        "unit": "ms",
        "description": "",
        "mean": 122.94950000420212,
        "delta": 15.113924312585468,
        "percentDelta": 12.292790383099492,
        "sum": 1229.4950000420213,
        "min": 106.17499999701977,
        "max": 174.55000000447035,
        "values": [
            174.55000000447035,
            107.92500001937151,
            121.989999987185,
            143.05000000447035,
            124.51500000804663,
            112.30500000715256,
            114.86500001698732,
            106.17499999701977,
            108.56000000983477,
            115.55999998748302
        ]
    },
    "Charts-chartjs/Draw scatter": {
        "name": "Charts-chartjs/Draw scatter",
        "unit": "ms",
        "description": "",
        "mean": 64.73400000259281,
        "delta": 11.30185636072618,
        "percentDelta": 17.45891859034434,
        "sum": 647.340000025928,
        "min": 51.62000000476837,
        "max": 105.2800000011921,
        "values": [
            105.2800000011921,
            56.65500000864267,
            64.81999999284744,
            71.02499999850988,
            71.4450000077486,
            57.88000000268221,
            54.00000000745058,
            51.62000000476837,
            55.29500000923872,
            59.31999999284744
        ]
    },
    "Charts-chartjs/Draw scatter/Sync": {
        "name": "Charts-chartjs/Draw scatter/Sync",
        "unit": "ms",
        "description": "",
        "mean": 60.551000002026555,
        "delta": 10.531188508514282,
        "percentDelta": 17.392261908410788,
        "sum": 605.5100000202656,
        "min": 48.51000000536442,
        "max": 98.22500000149012,
        "values": [
            98.22500000149012,
            53.70500000566244,
            59.15499999374151,
            67.64000000059605,
            66.96500000357628,
            54.310000002384186,
            50.87000000476837,
            48.51000000536442,
            52.275000005960464,
            53.854999996721745
        ]
    },
    "Charts-chartjs/Draw scatter/Async": {
        "name": "Charts-chartjs/Draw scatter/Async",
        "unit": "ms",
        "description": "",
        "mean": 4.183000000566244,
        "delta": 1.020676335569066,
        "percentDelta": 24.40058176980395,
        "sum": 41.83000000566244,
        "min": 2.9500000029802322,
        "max": 7.054999999701977,
        "values": [
            7.054999999701977,
            2.9500000029802322,
            5.66499999910593,
            3.3849999979138374,
            4.480000004172325,
            3.5700000002980232,
            3.130000002682209,
            3.1099999994039536,
            3.0200000032782555,
            5.464999996125698
        ]
    },
    "Charts-chartjs/Show tooltip": {
        "name": "Charts-chartjs/Show tooltip",
        "unit": "ms",
        "description": "",
        "mean": 21.0385000012815,
        "delta": 3.516306221826449,
        "percentDelta": 16.713673606066326,
        "sum": 210.385000012815,
        "min": 17.594999998807907,
        "max": 30.62000000476837,
        "values": [
            30.62000000476837,
            17.71500000357628,
            18.344999998807907,
            29.775000005960464,
            19.094999998807907,
            19.950000002980232,
            19.730000004172325,
            17.71000000089407,
            17.594999998807907,
            19.849999994039536
        ]
    },
    "Charts-chartjs/Show tooltip/Sync": {
        "name": "Charts-chartjs/Show tooltip/Sync",
        "unit": "ms",
        "description": "",
        "mean": 0.3950000017881393,
        "delta": 0.13564561104511383,
        "percentDelta": 34.34066086862151,
        "sum": 3.9500000178813934,
        "min": 0.09000000357627869,
        "max": 0.6600000038743019,
        "values": [
            0.5250000059604645,
            0.3200000002980232,
            0.4100000038743019,
            0.4100000038743019,
            0.11999999731779099,
            0.5200000032782555,
            0.6600000038743019,
            0.3049999997019768,
            0.09000000357627869,
            0.5899999961256981
        ]
    },
    "Charts-chartjs/Show tooltip/Async": {
        "name": "Charts-chartjs/Show tooltip/Async",
        "unit": "ms",
        "description": "",
        "mean": 20.64349999949336,
        "delta": 3.4741168346705167,
        "percentDelta": 16.829107635603357,
        "sum": 206.4349999949336,
        "min": 17.395000003278255,
        "max": 30.094999998807907,
        "values": [
            30.094999998807907,
            17.395000003278255,
            17.934999994933605,
            29.365000002086163,
            18.975000001490116,
            19.429999999701977,
            19.070000000298023,
            17.405000001192093,
            17.50499999523163,
            19.259999997913837
        ]
    },
    "Charts-chartjs/Draw opaque scatter": {
        "name": "Charts-chartjs/Draw opaque scatter",
        "unit": "ms",
        "description": "",
        "mean": 37.17700000032782,
        "delta": 2.132246943619827,
        "percentDelta": 5.735392698714326,
        "sum": 371.77000000327826,
        "min": 33.55500000715256,
        "max": 42.25,
        "values": [
            38.649999998509884,
            33.55500000715256,
            38.82499999552965,
            42.25,
            33.975000001490116,
            34.475000001490116,
            41.13500000536442,
            36.84499999135733,
            35.67000000178814,
            36.39000000059605
        ]
    },
    "Charts-chartjs/Draw opaque scatter/Sync": {
        "name": "Charts-chartjs/Draw opaque scatter/Sync",
        "unit": "ms",
        "description": "",
        "mean": 34.67299999967217,
        "delta": 2.1557637485531753,
        "percentDelta": 6.217413401129288,
        "sum": 346.72999999672174,
        "min": 31.304999999701977,
        "max": 39.725000001490116,
        "values": [
            34.92000000178814,
            31.990000002086163,
            36.17499999701977,
            39.59499999880791,
            31.304999999701977,
            32.71000000089407,
            39.725000001490116,
            34.48999999463558,
            32.19500000029802,
            33.625
        ]
    },
    "Charts-chartjs/Draw opaque scatter/Async": {
        "name": "Charts-chartjs/Draw opaque scatter/Async",
        "unit": "ms",
        "description": "",
        "mean": 2.504000000655651,
        "delta": 0.5454561473820005,
        "percentDelta": 21.783392461628495,
        "sum": 25.04000000655651,
        "min": 1.410000003874302,
        "max": 3.7299999967217445,
        "values": [
            3.7299999967217445,
            1.5650000050663948,
            2.649999998509884,
            2.655000001192093,
            2.6700000017881393,
            1.7650000005960464,
            1.410000003874302,
            2.3549999967217445,
            3.475000001490116,
            2.7650000005960464
        ]
    },
    "React-Stockcharts-SVG": {
        "name": "React-Stockcharts-SVG",
        "unit": "ms",
        "description": "",
        "mean": 179.86850000247358,
        "delta": 10.384131457306566,
        "percentDelta": 5.7731795490393045,
        "sum": 1798.685000024736,
        "min": 161.92999999970198,
        "max": 201.72499999403954,
        "values": [
            201.72499999403954,
            173.37000000476837,
            195.3250000104308,
            164.79499999433756,
            175.10000000149012,
            198.3449999988079,
            167.40500000864267,
            161.92999999970198,
            174.48500000685453,
            186.20500000566244
        ]
    },
    "React-Stockcharts-SVG/Render": {
        "name": "React-Stockcharts-SVG/Render",
        "unit": "ms",
        "description": "",
        "mean": 51.53400000035763,
        "delta": 4.476033882375638,
        "percentDelta": 8.685593748485612,
        "sum": 515.3400000035763,
        "min": 43.46999999135733,
        "max": 63.980000004172325,
        "values": [
            56.649999998509884,
            45.90500000119209,
            55.354999996721745,
            43.46999999135733,
            53.94500000029802,
            48.649999998509884,
            46.695000007748604,
            47.2149999961257,
            53.4750000089407,
            63.980000004172325
        ]
    },
    "React-Stockcharts-SVG/Render/Sync": {
        "name": "React-Stockcharts-SVG/Render/Sync",
        "unit": "ms",
        "description": "",
        "mean": 46.48450000062585,
        "delta": 4.472980174743059,
        "percentDelta": 9.622519710189065,
        "sum": 464.8450000062585,
        "min": 38.0899999961257,
        "max": 59.2850000038743,
        "values": [
            51.814999997615814,
            41.26500000059605,
            49.149999998509884,
            38.0899999961257,
            48.78000000119209,
            43.78000000119209,
            41.83000000566244,
            42.399999998509884,
            48.45000000298023,
            59.2850000038743
        ]
    },
    "React-Stockcharts-SVG/Render/Async": {
        "name": "React-Stockcharts-SVG/Render/Async",
        "unit": "ms",
        "description": "",
        "mean": 5.049499999731779,
        "delta": 0.3303207552548273,
        "percentDelta": 6.541652743288908,
        "sum": 50.49499999731779,
        "min": 4.6400000005960464,
        "max": 6.204999998211861,
        "values": [
            4.83500000089407,
            4.6400000005960464,
            6.204999998211861,
            5.379999995231628,
            5.16499999910593,
            4.869999997317791,
            4.865000002086163,
            4.814999997615814,
            5.0250000059604645,
            4.695000000298023
        ]
    },
    "React-Stockcharts-SVG/PanTheChart": {
        "name": "React-Stockcharts-SVG/PanTheChart",
        "unit": "ms",
        "description": "",
        "mean": 43.726500001549724,
        "delta": 3.2907564565435723,
        "percentDelta": 7.525771457644549,
        "sum": 437.2650000154972,
        "min": 36.979999996721745,
        "max": 53.875,
        "values": [
            53.875,
            46.90500000119209,
            44.9750000089407,
            42.84499999880791,
            42.020000003278255,
            45.90999999642372,
            42.1600000038743,
            39.74500000476837,
            36.979999996721745,
            41.850000001490116
        ]
    },
    "React-Stockcharts-SVG/PanTheChart/Sync": {
        "name": "React-Stockcharts-SVG/PanTheChart/Sync",
        "unit": "ms",
        "description": "",
        "mean": 7.177999999374151,
        "delta": 0.3728451379614688,
        "percentDelta": 5.1942760935354855,
        "sum": 71.77999999374151,
        "min": 6.240000002086163,
        "max": 7.655000001192093,
        "values": [
            7.655000001192093,
            7.579999998211861,
            6.925000004470348,
            7.519999995827675,
            7.6049999967217445,
            7.529999993741512,
            6.240000002086163,
            6.91499999910593,
            6.420000001788139,
            7.3900000005960464
        ]
    },
    "React-Stockcharts-SVG/PanTheChart/Async": {
        "name": "React-Stockcharts-SVG/PanTheChart/Async",
        "unit": "ms",
        "description": "",
        "mean": 36.54850000217557,
        "delta": 3.084716971806345,
        "percentDelta": 8.440064494090661,
        "sum": 365.4850000217557,
        "min": 30.559999994933605,
        "max": 46.21999999880791,
        "values": [
            46.21999999880791,
            39.32500000298023,
            38.05000000447035,
            35.32500000298023,
            34.41500000655651,
            38.38000000268221,
            35.92000000178814,
            32.83000000566244,
            30.559999994933605,
            34.46000000089407
        ]
    },
    "React-Stockcharts-SVG/ZoomTheChart": {
        "name": "React-Stockcharts-SVG/ZoomTheChart",
        "unit": "ms",
        "description": "",
        "mean": 84.60800000056625,
        "delta": 6.533926603915652,
        "percentDelta": 7.722587230370559,
        "sum": 846.0800000056624,
        "min": 74.9699999988079,
        "max": 103.7850000038743,
        "values": [
            91.19999999552965,
            80.56000000238419,
            94.99500000476837,
            78.48000000417233,
            79.13499999791384,
            103.7850000038743,
            78.54999999701977,
            74.9699999988079,
            84.0300000011921,
            80.375
        ]
    },
    "React-Stockcharts-SVG/ZoomTheChart/Sync": {
        "name": "React-Stockcharts-SVG/ZoomTheChart/Sync",
        "unit": "ms",
        "description": "",
        "mean": 81.66249999850989,
        "delta": 6.545237941478092,
        "percentDelta": 8.01498599920101,
        "sum": 816.6249999850988,
        "min": 72.07999999821186,
        "max": 100.85999999940395,
        "values": [
            87.9699999988079,
            77.88499999791384,
            92.27499999850988,
            75.64500000327826,
            75.56499999761581,
            100.85999999940395,
            75.68999999761581,
            72.07999999821186,
            81.11999999731779,
            77.53499999642372
        ]
    },
    "React-Stockcharts-SVG/ZoomTheChart/Async": {
        "name": "React-Stockcharts-SVG/ZoomTheChart/Async",
        "unit": "ms",
        "description": "",
        "mean": 2.9455000020563604,
        "delta": 0.18932157760882987,
        "percentDelta": 6.42748523091691,
        "sum": 29.455000020563602,
        "min": 2.6750000044703484,
        "max": 3.5700000002980232,
        "values": [
            3.2299999967217445,
            2.6750000044703484,
            2.7200000062584877,
            2.8350000008940697,
            3.5700000002980232,
            2.9250000044703484,
            2.8599999994039536,
            2.8900000005960464,
            2.910000003874302,
            2.8400000035762787
        ]
    },
    "Perf-Dashboard": {
        "name": "Perf-Dashboard",
        "unit": "ms",
        "description": "",
        "mean": 122.08149999901653,
        "delta": 24.412451222316523,
        "percentDelta": 19.996847370414997,
        "sum": 1220.8149999901652,
        "min": 100.12499998509884,
        "max": 193.27499999850988,
        "values": [
            138.88999999314547,
            101.02000000327826,
            171.2099999934435,
            102.25000000745058,
            193.27499999850988,
            106.95500000566244,
            102.30499999970198,
            100.12499998509884,
            103.52499999850988,
            101.26000000536442
        ]
    },
    "Perf-Dashboard/Render": {
        "name": "Perf-Dashboard/Render",
        "unit": "ms",
        "description": "",
        "mean": 29.366999998688698,
        "delta": 7.053591537521858,
        "percentDelta": 24.018767793226466,
        "sum": 293.669999986887,
        "min": 22.61999999731779,
        "max": 53.32000000029802,
        "values": [
            37.15999999642372,
            24.480000004172325,
            53.32000000029802,
            24.075000002980232,
            35.059999994933605,
            26.054999999701977,
            22.769999995827675,
            22.61999999731779,
            23.99499999731779,
            24.134999997913837
        ]
    },
    "Perf-Dashboard/Render/Sync": {
        "name": "Perf-Dashboard/Render/Sync",
        "unit": "ms",
        "description": "",
        "mean": 24.333499999344347,
        "delta": 5.809859716479244,
        "percentDelta": 23.875972287734143,
        "sum": 243.3349999934435,
        "min": 18.479999996721745,
        "max": 43.75500000268221,
        "values": [
            31.61999999731779,
            20.070000000298023,
            43.75500000268221,
            19.83500000089407,
            28.58500000089407,
            22.21000000089407,
            18.91999999433756,
            18.479999996721745,
            20,
            19.859999999403954
        ]
    },
    "Perf-Dashboard/Render/Async": {
        "name": "Perf-Dashboard/Render/Async",
        "unit": "ms",
        "description": "",
        "mean": 5.0334999993443486,
        "delta": 1.287481206192752,
        "percentDelta": 25.57824985319273,
        "sum": 50.33499999344349,
        "min": 3.844999998807907,
        "max": 9.564999997615814,
        "values": [
            5.53999999910593,
            4.410000003874302,
            9.564999997615814,
            4.240000002086163,
            6.4749999940395355,
            3.844999998807907,
            3.850000001490116,
            4.1400000005960464,
            3.994999997317791,
            4.274999998509884
        ]
    },
    "Perf-Dashboard/SelectingPoints": {
        "name": "Perf-Dashboard/SelectingPoints",
        "unit": "ms",
        "description": "",
        "mean": 53.0260000012815,
        "delta": 10.266180321094131,
        "percentDelta": 19.360653869509346,
        "sum": 530.260000012815,
        "min": 42.70500000566244,
        "max": 87.05499999970198,
        "values": [
            63.935000002384186,
            44.16499999910593,
            63.23499999940395,
            45.625,
            87.05499999970198,
            50.34000000357628,
            42.70500000566244,
            44.90999999642372,
            43.21000000089407,
            45.08000000566244
        ]
    },
    "Perf-Dashboard/SelectingPoints/Sync": {
        "name": "Perf-Dashboard/SelectingPoints/Sync",
        "unit": "ms",
        "description": "",
        "mean": 49.911500001698734,
        "delta": 9.153834450553799,
        "percentDelta": 18.34013093223455,
        "sum": 499.1150000169873,
        "min": 40.310000002384186,
        "max": 79.58500000089407,
        "values": [
            59.96000000089407,
            42.17499999701977,
            60.105000004172325,
            43.145000003278255,
            79.58500000089407,
            47.50500000268221,
            40.310000002384186,
            42.29999999701977,
            41.01000000536442,
            43.020000003278255
        ]
    },
    "Perf-Dashboard/SelectingPoints/Async": {
        "name": "Perf-Dashboard/SelectingPoints/Async",
        "unit": "ms",
        "description": "",
        "mean": 3.1144999995827676,
        "delta": 1.1724670594011406,
        "percentDelta": 37.64543456600448,
        "sum": 31.144999995827675,
        "min": 1.9900000020861626,
        "max": 7.469999998807907,
        "values": [
            3.975000001490116,
            1.9900000020861626,
            3.1299999952316284,
            2.4799999967217445,
            7.469999998807907,
            2.8350000008940697,
            2.3950000032782555,
            2.6099999994039536,
            2.1999999955296516,
            2.060000002384186
        ]
    },
    "Perf-Dashboard/SelectingRange": {
        "name": "Perf-Dashboard/SelectingRange",
        "unit": "ms",
        "description": "",
        "mean": 39.68849999904633,
        "delta": 9.339510907869023,
        "percentDelta": 23.53203297704232,
        "sum": 396.88499999046326,
        "min": 30.560000002384186,
        "max": 71.1600000038743,
        "values": [
            37.79499999433756,
            32.375,
            54.65499999374151,
            32.55000000447035,
            71.1600000038743,
            30.560000002384186,
            36.82999999821186,
            32.59499999135733,
            36.32000000029802,
            32.04500000178814
        ]
    },
    "Perf-Dashboard/SelectingRange/Sync": {
        "name": "Perf-Dashboard/SelectingRange/Sync",
        "unit": "ms",
        "description": "",
        "mean": 35.84349999949336,
        "delta": 7.266621048013373,
        "percentDelta": 20.273190531382493,
        "sum": 358.4349999949336,
        "min": 28.240000002086163,
        "max": 56.67999999970198,
        "values": [
            34.939999997615814,
            28.265000000596046,
            52.184999994933605,
            29.910000003874302,
            56.67999999970198,
            28.240000002086163,
            34.54999999701977,
            30.104999996721745,
            33.850000001490116,
            29.71000000089407
        ]
    },
    "Perf-Dashboard/SelectingRange/Async": {
        "name": "Perf-Dashboard/SelectingRange/Async",
        "unit": "ms",
        "description": "",
        "mean": 3.8449999995529653,
        "delta": 2.7007055683661294,
        "percentDelta": 70.23941661066642,
        "sum": 38.44999999552965,
        "min": 2.280000001192093,
        "max": 14.480000004172325,
        "values": [
            2.8549999967217445,
            4.1099999994039536,
            2.469999998807907,
            2.6400000005960464,
            14.480000004172325,
            2.3200000002980232,
            2.280000001192093,
            2.489999994635582,
            2.469999998807907,
            2.3350000008940697
        ]
    },
    "Iteration-0-Total": {
        "name": "Iteration-0-Total",
        "unit": "ms",
        "description": "Test totals for iteration 0",
        "mean": 134.79975000023842,
        "delta": 38.09681158748666,
        "percentDelta": 28.2617820785419,
        "sum": 2695.9950000047684,
        "min": 23.339999988675117,
        "max": 312.64500000327826,
        "values": [
            110.94500000029802,
            106.9699999988079,
            137.64500000327826,
            101.8399999961257,
            96.49000000208616,
            113.97999999672174,
            97.72499999403954,
            62.59500000625849,
            312.64500000327826,
            31.00500000268221,
            23.339999988675117,
            32.9750000089407,
            237.10999999940395,
            247.86499999463558,
            88.01500001549721,
            267.945000000298,
            111.74000000208616,
            174.55000000447035,
            201.72499999403954,
            138.88999999314547
        ]
    },
    "Iteration-1-Total": {
        "name": "Iteration-1-Total",
        "unit": "ms",
        "description": "Test totals for iteration 1",
        "mean": 97.62975000217557,
        "delta": 30.877630174283794,
        "percentDelta": 31.627275675289265,
        "sum": 1952.5950000435114,
        "min": 28.820000000298023,
        "max": 292.00499998778105,
        "values": [
            79.4550000205636,
            97.3049999922514,
            29.935000002384186,
            130.5300000011921,
            75.20999999344349,
            51.04499999433756,
            68.6900000050664,
            37.935000009834766,
            292.00499998778105,
            28.820000000298023,
            57.860000014305115,
            28.88500002026558,
            197.5949999988079,
            141.99999999254942,
            45.29999999701977,
            113.29999999701977,
            94.40999998897314,
            107.92500001937151,
            173.37000000476837,
            101.02000000327826
        ]
    },
    "Iteration-2-Total": {
        "name": "Iteration-2-Total",
        "unit": "ms",
        "description": "Test totals for iteration 2",
        "mean": 106.80400000065565,
        "delta": 35.00244975706678,
        "percentDelta": 32.77260192207399,
        "sum": 2136.080000013113,
        "min": 22.189999997615814,
        "max": 253.12500000745058,
        "values": [
            67.27499999850988,
            80.55000000447035,
            35.270000003278255,
            96.97999999672174,
            84.15000000596046,
            52.37499998509884,
            73.67000000178814,
            40.91999999433756,
            253.12500000745058,
            22.189999997615814,
            32.275000005960464,
            24.560000009834766,
            253.01999999582767,
            211.36500000208616,
            54.1600000038743,
            146.14000000059605,
            119.53000000864267,
            121.989999987185,
            195.3250000104308,
            171.2099999934435
        ]
    },
    "Iteration-3-Total": {
        "name": "Iteration-3-Total",
        "unit": "ms",
        "description": "Test totals for iteration 3",
        "mean": 125.5835000000894,
        "delta": 43.959796438762396,
        "percentDelta": 35.00443644167514,
        "sum": 2511.670000001788,
        "min": 19.964999996125698,
        "max": 367.00500001758337,
        "values": [
            88.4750000089407,
            92.92500001192093,
            39.97000001370907,
            230.3099999949336,
            227.58999998867512,
            82.7699999883771,
            90.68999999761581,
            45.770000003278255,
            367.00500001758337,
            21.75000000745058,
            19.964999996125698,
            29.19999998807907,
            225.89000000804663,
            264.25999999791384,
            52.65499999374151,
            119.44499999284744,
            102.90499998629093,
            143.05000000447035,
            164.79499999433756,
            102.25000000745058
        ]
    },
    "Iteration-4-Total": {
        "name": "Iteration-4-Total",
        "unit": "ms",
        "description": "Test totals for iteration 4",
        "mean": 108.41475000157952,
        "delta": 38.810906628837216,
        "percentDelta": 35.79854828634643,
        "sum": 2168.2950000315905,
        "min": 18.62500000745058,
        "max": 374.625,
        "values": [
            72.75499999523163,
            137.85499999672174,
            34.33500000089407,
            79.47499999403954,
            78.78500001132488,
            94.5650000050664,
            88.70500000566244,
            41.58499999344349,
            374.625,
            19.879999987781048,
            18.62500000745058,
            25.24999999254942,
            182.010000012815,
            150.62000000476837,
            52.57000000029802,
            124.9100000038743,
            98.8550000116229,
            124.51500000804663,
            175.10000000149012,
            193.27499999850988
        ]
    },
    "Iteration-5-Total": {
        "name": "Iteration-5-Total",
        "unit": "ms",
        "description": "Test totals for iteration 5",
        "mean": 104.94475000314415,
        "delta": 37.66793482907409,
        "percentDelta": 35.89311025844128,
        "sum": 2098.895000062883,
        "min": 20.08500000834465,
        "max": 349.2749999985099,
        "values": [
            139.2449999973178,
            79.59000000357628,
            32.440000005066395,
            115.03499999642372,
            92.70499999821186,
            56.33500000834465,
            90.67000000178814,
            51.145000010728836,
            349.2749999985099,
            20.08500000834465,
            20.510000012815,
            27.950000002980232,
            227.87500000745058,
            150.66499999910593,
            41.71999999880791,
            98.81000000238419,
            87.23499999940395,
            112.30500000715256,
            198.3449999988079,
            106.95500000566244
        ]
    },
    "Iteration-6-Total": {
        "name": "Iteration-6-Total",
        "unit": "ms",
        "description": "Test totals for iteration 6",
        "mean": 94.81650000065565,
        "delta": 28.05633916414771,
        "percentDelta": 29.5901442934022,
        "sum": 1896.330000013113,
        "min": 22.21000000834465,
        "max": 251.4050000011921,
        "values": [
            141.5600000023842,
            77.19499999284744,
            28.480000004172325,
            78.04500000923872,
            77.28499999642372,
            59.270000003278255,
            72.45000000298023,
            64.80499998480082,
            251.4050000011921,
            22.21000000834465,
            26.08500000834465,
            33.37999998778105,
            181.17000000178814,
            151.12999999523163,
            38.73499999940395,
            113.27499999850988,
            95.2749999910593,
            114.86500001698732,
            167.40500000864267,
            102.30499999970198
        ]
    },
    "Iteration-7-Total": {
        "name": "Iteration-7-Total",
        "unit": "ms",
        "description": "Test totals for iteration 7",
        "mean": 98.01900000050664,
        "delta": 31.492694579019563,
        "percentDelta": 32.12917350601086,
        "sum": 1960.3800000101328,
        "min": 17.50499999523163,
        "max": 279.7449999898672,
        "values": [
            96.86000000685453,
            77.43500000983477,
            34.600000001490116,
            90.85000000149012,
            91.77000000327826,
            56.650000005960464,
            68.9649999961257,
            39.90999999642372,
            279.7449999898672,
            20.42000000923872,
            17.50499999523163,
            24.79000000655651,
            190.8250000104308,
            147.20499999821186,
            48.40500000119209,
            131.29500000178814,
            174.91999999433756,
            106.17499999701977,
            161.92999999970198,
            100.12499998509884
        ]
    },
    "Iteration-8-Total": {
        "name": "Iteration-8-Total",
        "unit": "ms",
        "description": "Test totals for iteration 8",
        "mean": 95.20399999730289,
        "delta": 35.57929860667474,
        "percentDelta": 37.37164258611266,
        "sum": 1904.0799999460578,
        "min": 21.424999989569187,
        "max": 308.8400000035763,
        "values": [
            66.58500000834465,
            88.83499999344349,
            26.644999980926514,
            75.4450000077486,
            77.49999998509884,
            53.144999995827675,
            70.08499999344349,
            38.98999999463558,
            308.8400000035763,
            21.774999991059303,
            21.424999989569187,
            27.424999989569187,
            250.51500000059605,
            151.16499999910593,
            41.315000005066395,
            108.80999998748302,
            89.01000000536442,
            108.56000000983477,
            174.48500000685453,
            103.52499999850988
        ]
    },
    "Iteration-9-Total": {
        "name": "Iteration-9-Total",
        "unit": "ms",
        "description": "Test totals for iteration 9",
        "mean": 95.36925000064075,
        "delta": 32.103308337407185,
        "percentDelta": 33.662116811437116,
        "sum": 1907.385000012815,
        "min": 20.564999997615814,
        "max": 257.59999999403954,
        "values": [
            81.87499999254942,
            85.75999999791384,
            34.53499999642372,
            95.98499999940395,
            88.99500001221895,
            52.689999997615814,
            71.99500000476837,
            39.13499999046326,
            257.59999999403954,
            20.564999997615814,
            23.185000017285347,
            25.665000021457672,
            244.86500000953674,
            155.62999999523163,
            39.28999999165535,
            97.875,
            88.7149999961257,
            115.55999998748302,
            186.20500000566244,
            101.26000000536442
        ]
    },
    "Geomean": {
        "name": "Geomean",
        "unit": "ms",
        "description": "Geomean of test totals",
        "mean": 82.83423933939957,
        "delta": 7.913251175995865,
        "percentDelta": 9.553116246498782,
        "sum": 828.3423933939957,
        "min": 72.41259163582257,
        "max": 109.66044870525954,
        "values": [
            109.66044870525954,
            79.78437763456836,
            82.74392245387924,
            93.4223704479295,
            82.18335892516515,
            80.10922390120736,
            77.24402610270998,
            76.32009857661532,
            72.41259163582257,
            74.4619750108387
        ]
    },
    "Score": {
        "name": "Score",
        "unit": "score",
        "description": "Scaled inverse of the Geomean",
        "mean": 12.238138440863722,
        "delta": 0.9945446597531545,
        "percentDelta": 8.126600827069606,
        "sum": 122.38138440863722,
        "min": 9.119058072503016,
        "max": 13.809752936743383,
        "values": [
            9.119058072503016,
            12.533782046658816,
            12.085479759040812,
            10.704074358264828,
            12.167913469083004,
            12.482957034176543,
            12.94598495772758,
            13.102708443125657,
            13.809752936743383,
            13.429673331313598
        ]
    }
}Uploading speedometer-3-2026-10-07T02_33_24.235Z.json…]()

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
