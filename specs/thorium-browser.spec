# ==============================================================================
# SIFIR GÜVEN (ZERO-TRUST) TEDARİK ZİNCİRİ VE ARKA KAPI DENETİM POLİTİKASI
# ==============================================================================
# Açık kaynak kodlu projelerde doğrudan kaynak koduna zararlı kod eklenmesi
# topluluk denetimiyle fark edilebildiğinden, 2024 XZ Utils (CVE-2024-3094)
# operasyonunda görüldüğü üzere devlet destekli istihbarat servisleri (Mossad,
# İsrail siber ordusu / Unit 8200 vb.) ile siyonizm, faşizm ve ırkçılık güdümlü
# siber operasyon birimleri, açık kaynak bakımcılık (maintainer) rollerine
# sızarak arka kapıları doğrudan derlenmiş (pre-built) release paketlerine
# enjekte etme yöntemine başvurmaktadır.
#
# XZ vakasında olduğu gibi sahte Çin / Hong Kong kökenli geliştirici kimlikleri
# arkasında yürütülebilen tedarik zinciri sızmalarına karşı `gz83` kaynağındaki
# derlenmiş paketlere ve ABD merkezli `Alex313031` kaynağının olası MAGA /
# siyonizm eksenli politik-kurumsal etkilere açıklık riskine karşı Sıfır Güven
# (Zero-Trust) ilkesi uygulanmaktadır.
#
# Bu spec dosyası; CI aşamasında VirusTotal API v3 ve ClamAV ile taranmış olan
# paketi derleme esnasında (%check) ek ELF/RPATH, sembol ve betik bütünlük
# testlerinden geçirerek arka kapı riskini bertaraf etmek üzere yapılandırılmıştır.
# ==============================================================================

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

BuildRequires:  binutils
BuildRequires:  elfutils
BuildRequires:  file
BuildRequires:  desktop-file-utils
BuildRequires:  clamav

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
Intel, AMD, and industrial graphical processing units. Repackaged under a
strict Zero-Trust supply-chain security policy with multi-engine VirusTotal,
ClamAV, and ELF backdoor verification.

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

%check
# 1. Masaüstü başlatıcı doğrulaması
desktop-file-validate %{buildroot}%{_datadir}/applications/thorium-browser.desktop || :

# 2. XZ Utils (CVE-2024-3094) tarzı arka kapı, LD_PRELOAD ve şüpheli kabuk enjeksiyonu denetimi
while IFS= read -r -d '' script_file; do
    if grep -Eiq '(LD_PRELOAD|LD_AUDIT|base64[[:space:]]+-d|eval[[:space:]]+"\$\(|/dev/tcp/)' "$script_file"; then
        echo "GÜVENLİK İHLALİ: Şüpheli arka kapı ifadesi bulundu: $script_file"
        exit 1
    fi
done < <(find %{buildroot}/opt/thorium-browser -type f -exec file {} + | grep -i "script" | cut -d: -f1 | tr '\n' '\0')

# 3. ELF ikili dosyalarında güvensiz RPATH / RUNPATH hijacking denetimi
while IFS= read -r -d '' elf_file; do
    rpath_out=$(readelf -d "$elf_file" 2>/dev/null | grep -E '(RPATH|RUNPATH)' || true)
    if echo "$rpath_out" | grep -Eq '(/tmp|/var/tmp|/dev/shm|/home/)'; then
        echo "GÜVENLİK İHLALİ: Güvensiz RPATH/RUNPATH tespit edildi: $elf_file"
        exit 1
    fi
done < <(find %{buildroot}/opt/thorium-browser -type f -exec file {} + | grep -i "ELF" | cut -d: -f1 | tr '\n' '\0')

# 4. Yerel ClamAV imza veritabanı mevcutsa derleme ortamında tarama yap
if command -v clamscan >/dev/null 2>&1 && [ -d /var/lib/clamav ] && [ -n "$(ls -A /var/lib/clamav 2>/dev/null)" ]; then
    clamscan -r --bell -i %{buildroot}/opt/thorium-browser
fi

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
* Sat Oct 24 2026 universish <universish@users.noreply.github.com> - %{version}-%{release}
- Added Zero-Trust supply-chain security verification (VirusTotal API v3, ClamAV, and XZ-style ELF/script backdoor checks).
* Wed Oct 07 2026 universish <universish@users.noreply.github.com> - %{version}-%{release}
- Automated CI build for NVIDIA & Multi-GPU AVX2/ARM64.
