#!/usr/bin/env bash
set -e

# 1. ~/.config/thorium-flags.conf otomatik yapılandırma denetimi
CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}"
FLAGS_FILE="$CONFIG_DIR/thorium-flags.conf"

if [ ! -f "$FLAGS_FILE" ]; then
    mkdir -p "$CONFIG_DIR"
    cat << 'EOF' > "$FLAGS_FILE"
--ozone-platform=x11
--enable-features=VaapiVideoDecodeLinuxGL,VaapiVideoEncoderLinuxGL
--ignore-gpu-blocklist
--enable-zero-copy
--use-gl=angle
--use-angle=gl
EOF
fi

# 2. Donanım ve GPU Tanılama
# NVIDIA GPU ve sürücüsü aktifse offload ve VA-API backend değişkenlerini ata
if [ -e /dev/nvidia0 ] || [ -e /proc/driver/nvidia ] || command -v nvidia-smi >/dev/null 2>&1; then
    export NVD_BACKEND="${NVD_BACKEND:-direct}"
    export __NV_PRIME_RENDER_OFFLOAD="${__NV_PRIME_RENDER_OFFLOAD:-1}"
    export __GLX_VENDOR_LIBRARY_NAME="${__GLX_VENDOR_LIBRARY_NAME:-nvidia}"
fi

# 3. Bayrakları çözümle
USER_FLAGS=()
if [ -f "$FLAGS_FILE" ]; then
    while IFS= read -r line || [ -n "$line" ]; do
        # Boş satırları ve yorumları filtrele
        line="$(echo "$line" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
        [[ -z "$line" || "$line" =~ ^# ]] && continue
        USER_FLAGS+=("$line")
    done < "$FLAGS_FILE"
fi

# 4. İkili dosyayı çalıştır
exec /opt/thorium-browser/thorium-browser "${USER_FLAGS[@]}" "$@"
