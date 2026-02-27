#!/bin/bash
# Port 8000'i kapatır, port boşalana kadar bekler, sonra sunucuyu başlatır.
cd "$(dirname "$0")"

echo "Port 8000 kapatılıyor..."
for i in 1 2 3 4 5 6 7 8 9 10; do
  PIDS=$(lsof -ti :8000 2>/dev/null)
  if [ -z "$PIDS" ]; then
    break
  fi
  echo "$PIDS" | xargs kill -9 2>/dev/null
  echo "  Bekleniyor... ($i)"
  sleep 2
done

PIDS=$(lsof -ti :8000 2>/dev/null)
if [ -n "$PIDS" ]; then
  echo "HATA: Port 8000 hâlâ kullanımda (PID: $PIDS). Manuel kapat: kill -9 $PIDS"
  exit 1
fi

echo "Port 8000 boş. OS'un portu bırakması için 3 saniye bekleniyor..."
sleep 3

echo "Sunucu başlatılıyor..."
echo "=============================================="
echo "  Ana site:    http://127.0.0.1:8000"
echo "  Yönetici:    http://127.0.0.1:8000/admin"
echo "=============================================="
echo ""

if [ -d .venv ]; then
  exec .venv/bin/uvicorn app.main:app --reload --port 8000
elif [ -d venv ]; then
  exec venv/bin/uvicorn app.main:app --reload --port 8000
else
  exec uvicorn app.main:app --reload --port 8000
fi
