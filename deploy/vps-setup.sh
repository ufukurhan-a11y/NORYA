#!/usr/bin/env bash
# Norya VPS kurulum scripti – proje kökünden çalıştırın: ./deploy/vps-setup.sh [domain]
# Örnek: cd /var/www/norya && sudo ./deploy/vps-setup.sh
# Nginx + domain: sudo ./deploy/vps-setup.sh norya.example.com

set -e
DOMAIN="${1:-}"

# Proje kökü: script deploy/ içinde olduğu için bir üst dizin
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [ ! -f "requirements.txt" ] || [ ! -d "app" ]; then
  echo "Hata: requirements.txt veya app/ bulunamadı. Proje kökünden çalıştırın: ./deploy/vps-setup.sh"
  exit 1
fi

# Servisi hangi kullanıcı çalıştırsın (sudo ile çalıştırıyorsanız SUDO_USER)
RUN_USER="${SUDO_USER:-$USER}"
if [ "$RUN_USER" = "root" ] || [ -z "$RUN_USER" ]; then
  RUN_USER="www-data"
fi

echo "=== Norya VPS kurulumu ==="
echo "Proje dizini: $ROOT"
echo "Servis kullanıcısı: $RUN_USER"
echo ""

# 1) Python3 venv
if ! command -v python3 &>/dev/null; then
  echo "Python3 yükleniyor..."
  apt-get update -qq && apt-get install -y -qq python3 python3-venv python3-pip
fi
if [ ! -d ".venv" ]; then
  echo "Sanal ortam oluşturuluyor..."
  python3 -m venv .venv
fi
echo "Bağımlılıklar yükleniyor..."
.venv/bin/pip install -q --upgrade pip
.venv/bin/pip install -q -r requirements.txt

# 2) .env
_set_env() {
  local key="$1" val="$2"
  [ -z "$key" ] && return
  if [ -f ".env" ]; then
    grep -v "^${key}=" .env > .env._tmp 2>/dev/null || true
    [ -n "$val" ] && echo "${key}=${val}" >> .env._tmp
    mv .env._tmp .env
  else
    [ -n "$val" ] && echo "${key}=${val}" >> .env
  fi
}

if [ ! -f ".env" ]; then
  if [ -f ".env.example" ]; then
    cp .env.example .env
  else
    touch .env
  fi
fi

# 2b) İnteraktif .env sihirbazı (terminalde çalışıyorsa)
_env_get() { [ -f ".env" ] && grep -E "^${1}=" .env 2>/dev/null | sed "s/^${1}=//" | head -1; }
if [ -t 0 ]; then
  echo ""
  echo "--- .env ayarları (Enter = atla / otomatik üret) ---"
  cur=$(_env_get OPENAI_API_KEY)
  if [ -z "$cur" ] || [ "$cur" = "sk-..." ]; then
    echo -n "OPENAI_API_KEY (OpenAI'dan sk- ile başlayan key): "
    read -r val
    [ -n "$val" ] && _set_env OPENAI_API_KEY "$val"
  fi
  cur=$(_env_get SECRET_KEY)
  if [ -z "$cur" ] || [ "$cur" = "your-secret-key-change-in-production" ]; then
    echo -n "SECRET_KEY (Enter = otomatik üret): "
    read -r val
    [ -z "$val" ] && val=$(openssl rand -hex 32 2>/dev/null || python3 -c "import secrets; print(secrets.token_hex(32))" 2>/dev/null)
    [ -n "$val" ] && _set_env SECRET_KEY "$val" && echo "  -> SECRET_KEY ayarlandı"
  fi
  cur=$(_env_get ADMIN_SECRET)
  if [ -z "$cur" ] || [ "$cur" = "your-admin-secret" ]; then
    echo -n "ADMIN_SECRET (admin panel şifresi, Enter = otomatik üret): "
    read -r val
    [ -z "$val" ] && val=$(openssl rand -hex 24 2>/dev/null || python3 -c "import secrets; print(secrets.token_hex(24))" 2>/dev/null)
    [ -n "$val" ] && _set_env ADMIN_SECRET "$val" && echo "  -> ADMIN_SECRET ayarlandı (panel: /admin)"
  fi
  cur=$(_env_get DATABASE_URL)
  if [ -z "$cur" ] || [ "$cur" = "sqlite:///./norya.db" ]; then
    echo -n "DATABASE_URL (Enter = SQLite, PostgreSQL: postgresql://user:pass@host/db): "
    read -r val
    [ -n "$val" ] && _set_env DATABASE_URL "$val"
  fi
  echo "--- .env hazır ---"
  echo ""
else
  echo ".env mevcut; değerleri elle girmek için: sudo nano $ROOT/.env"
fi

# 3) Dizin sahipliği (root ile çalıştırıldıysa servis kullanıcısına bırak)
if [ "$(id -u)" = "0" ] && [ "$RUN_USER" != "root" ]; then
  chown -R "$RUN_USER:$RUN_USER" "$ROOT"
fi

# 4) Systemd servisi
SVC="/etc/systemd/system/norya.service"
sed -e "s|/var/www/norya|$ROOT|g" \
    -e "s|User=www-data|User=$RUN_USER|g" \
    -e "s|Group=www-data|Group=$RUN_USER|g" \
    "$ROOT/deploy/norya.service.example" > "$ROOT/deploy/norya.service.generated"
echo "Systemd servisi yazılıyor: $SVC"
cp "$ROOT/deploy/norya.service.generated" "$SVC"
systemctl daemon-reload
systemctl enable norya
systemctl restart norya
echo "Servis başlatıldı: systemctl status norya"
rm -f "$ROOT/deploy/norya.service.generated"
# .env sihirbazda güncellendiyse servis yeni değerleri alsın diye tekrar başlat
systemctl restart norya 2>/dev/null || true

# 5) Nginx (domain verilmişse)
if [ -n "$DOMAIN" ]; then
  if ! command -v nginx &>/dev/null; then
    echo "Nginx yükleniyor..."
    apt-get update -qq && apt-get install -y -qq nginx
  fi
  NGINX_CONF="/etc/nginx/sites-available/norya"
  sed "s|norya.example.com|$DOMAIN|g" "$ROOT/deploy/nginx-norya.conf.example" > "$ROOT/deploy/nginx-norya.generated"
  cp "$ROOT/deploy/nginx-norya.generated" "$NGINX_CONF"
  rm -f "$ROOT/deploy/nginx-norya.generated"
  ln -sf /etc/nginx/sites-available/norya /etc/nginx/sites-enabled/
  nginx -t && systemctl reload nginx
  echo "Nginx ayarlandı: $DOMAIN → http://127.0.0.1:8000"
  echo "SSL için: sudo certbot --nginx -d $DOMAIN"
fi

echo ""
echo "=== Kurulum tamamlandı ==="
echo "  Servis: systemctl status norya"
echo "  Log:    journalctl -u norya -f"
if [ -n "$DOMAIN" ]; then
  echo "  Site:   http://$DOMAIN (SSL: certbot --nginx -d $DOMAIN)"
else
  echo "  Uygulama 127.0.0.1:8000'de. Nginx kullanmak için: ./deploy/vps-setup.sh norya.example.com"
fi
echo "  .env düzenlemek için: nano $ROOT/.env  (OPENAI_API_KEY zorunlu)"
