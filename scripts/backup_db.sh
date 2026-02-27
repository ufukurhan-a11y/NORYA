#!/usr/bin/env bash
# Norya veritabanı yedekleme: SQLite (.backup) veya PostgreSQL (pg_dump).
# Kullanım: proje kökünde ./scripts/backup_db.sh [hedef_dizin]
# Hedef dizin verilmezse yedekler ./backups/ içine yazılır.

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

BACKUP_DIR="${1:-$ROOT/backups}"
mkdir -p "$BACKUP_DIR"
STAMP="$(date +%Y%m%d_%H%M%S)"

# .env'den DATABASE_URL oku (yoksa varsayılan)
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi
DATABASE_URL="${DATABASE_URL:-sqlite:///./norya.db}"

if [[ "$DATABASE_URL" == sqlite* ]]; then
  # sqlite:///./norya.db -> norya.db (proje kökünde)
  DB_FILE="${DATABASE_URL#sqlite:///}"
  DB_FILE="${DB_FILE#./}"
  [ -z "$DB_FILE" ] && DB_FILE="norya.db"
  if [ ! -f "$DB_FILE" ]; then
    echo "SQLite dosyası bulunamadı: $DB_FILE"
    exit 1
  fi
  OUT="$BACKUP_DIR/norya_sqlite_$STAMP.db"
  sqlite3 "$DB_FILE" ".backup '$OUT'"
  echo "Yedek alındı: $OUT"
else
  # PostgreSQL: pg_dump (REDACTED URL ile)
  if command -v pg_dump >/dev/null 2>&1; then
    OUT="$BACKUP_DIR/norya_pg_$STAMP.sql"
    # Güvenlik: şifre URL'de olsa bile pg_dump PGPASSWORD ile çalışır
    pg_dump "$DATABASE_URL" --no-owner --no-acl -f "$OUT"
    echo "Yedek alındı: $OUT"
  else
    echo "PostgreSQL yedeği için pg_dump kurulu değil. DATABASE_URL: ${DATABASE_URL%%@*}@..."
    exit 1
  fi
fi
