#!/bin/bash
# Norya uygulamasını başlatır. İlk çalıştırmada sanal ortam oluşturur.

set -e
cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
  echo "Sanal ortam yok, oluşturuluyor..."
  python3 -m venv .venv
  echo "Bağımlılıklar yükleniyor..."
  .venv/bin/pip install -q -r requirements.txt
fi

echo "Uygulama başlatılıyor: http://0.0.0.0:8000"
.venv/bin/python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
