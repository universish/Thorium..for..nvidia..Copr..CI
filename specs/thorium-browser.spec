Name:           thorium-browser
Version:        1.0.0
Release:        1%{?dist}
Summary:        Compiler-optimized Chromium fork tuned for NVIDIA, AMD, and Intel hardware acceleration
License:        BSD-3-Clause and MIT
URL:            https://thorium.rocks/
ExclusiveArch:  x86_64 aarch64

Source0:        upstream-payload.tar.gz
Source1:        thorium-launcher.sh
Source2:        thorium-browser.desktop
Source3:        thorium-browser.metainfo.xml

Requires:       libva
Requires:       libva-utils
Requires:       mesa-va-drivers
Recommends:     nvidia-vaapi-driver
Recommends:     libva-intel-driver
Recommends:     intel-media-driver

# Fedora debuginfo üretimini ikili pakette kapatır
%global debug_package %{nil}
%global __strip /bin/true

%description
Thorium is an aggressive compiler-optimized fork of Chromium. This package
provides automatic hardware acceleration routing: configuring VA-API direct
backends for NVIDIA platforms, and standard Mesa hardware pipelines for
Intel, AMD, and industrial graphical processing units.

%prep
%setup -q -c -n thorium-extracted

%build
# İkili paket doğrudan hazırlandığı için derleme adımı gerekmez

%install
rm -rf %{buildroot}

# Uygulama kök dizini
mkdir -p %{buildroot}/opt/thorium-browser
cp -a * %{buildroot}/opt/thorium-browser/

# Başlatıcı sarmalayıcı
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/thorium-browser

# Masaüstü ve Simge dosyaları
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/thorium-browser.desktop
install -Dm644 %{SOURCE3} %{buildroot}%{_datadir}/metainfo/thorium-browser.metainfo.xml

# Simge tespiti ve kopyalanması
for size in 16 24 32 48 64 128 256; do
    if [ -f "%{buildroot}/opt/thorium-browser/product_logo_${size}.png" ]; then
        install -Dm644 "%{buildroot}/opt/thorium-browser/product_logo_${size}.png" \
            "%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/thorium-browser.png"
    fi
done

# Varsayılan şablon konfigürasyonu
mkdir -p %{buildroot}%{_sysconfdir}/thorium
cat << 'EOF' > %{buildroot}%{_sysconfdir}/thorium/thorium-flags.conf
--ozone-platform=x11
--enable-features=VaapiVideoDecodeLinuxGL,VaapiVideoEncoderLinuxGL
--ignore-gpu-blocklist
--enable-zero-copy
--use-gl=angle
--use-angle=gl
EOF

%files
/opt/thorium-browser
%{_bindir}/thorium-browser
%{_datadir}/applications/thorium-browser.desktop
%{_datadir}/metainfo/thorium-browser.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/thorium-browser.png
%config(noreplace) %{_sysconfdir}/thorium/thorium-flags.conf

%post
/usr/bin/update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Wed Oct 07 2026 universish <universish@users.noreply.github.com> - %{version}-%{release}
- Automated CI build for NVIDIA & Multi-GPU AVX2/ARM64.
