#!/usr/bin/env bash
# Sadece .env sihirbazı – proje kökünden: ./deploy/env-wizard.sh
# Değerleri sonradan girmek veya güncellemek için kullanın.

set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [ ! -f ".env" ]; then
  [ -f ".env.example" ] && cp .env.example .env || touch .env
fi

_set_env() {
  local key="$1" val="$2"
  [ -z "$key" ] && return
  grep -v "^${key}=" .env > .env._tmp 2>/dev/null || true
  [ -n "$val" ] && echo "${key}=${val}" >> .env._tmp
  mv .env._tmp .env
}
_env_get() { grep -E "^${1}=" .env 2>/dev/null | sed "s/^${1}=//" | head -1; }

echo "=== Norya .env ayarları ==="
echo ""

echo -n "OPENAI_API_KEY [mevcut: $(_env_get OPENAI_API_KEY)]: "
read -r val
[ -n "$val" ] && _set_env OPENAI_API_KEY "$val"

echo -n "SECRET_KEY (Enter = otomatik üret) [mevcut ayarlı]: "
read -r val
if [ -n "$val" ]; then
  _set_env SECRET_KEY "$val"
else
  cur=$(_env_get SECRET_KEY)
  if [ -z "$cur" ] || [ "$cur" = "your-secret-key-change-in-production" ]; then
    v=$(openssl rand -hex 32 2>/dev/null || python3 -c "import secrets; print(secrets.token_hex(32))" 2>/dev/null)
    _set_env SECRET_KEY "$v" && echo "  -> SECRET_KEY üretildi"
  fi
fi

echo -n "ADMIN_SECRET (Enter = otomatik üret) [mevcut ayarlı]: "
read -r val
if [ -n "$val" ]; then
  _set_env ADMIN_SECRET "$val"
else
  cur=$(_env_get ADMIN_SECRET)
  if [ -z "$cur" ] || [ "$cur" = "your-admin-secret" ]; then
    v=$(openssl rand -hex 24 2>/dev/null || python3 -c "import secrets; print(secrets.token_hex(24))" 2>/dev/null)
    _set_env ADMIN_SECRET "$v" && echo "  -> ADMIN_SECRET üretildi (/admin)"
  fi
fi

echo -n "DATABASE_URL (Enter = değiştirme): "
read -r val
[ -n "$val" ] && _set_env DATABASE_URL "$val"

echo ""
echo ".env güncellendi. Servisi yenilemek için: sudo systemctl restart norya"
