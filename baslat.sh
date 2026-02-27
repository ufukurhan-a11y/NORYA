#!/bin/bash
# Norya sunucusunu başlatır (port 8000). Port doluysa önce kapatır.
set -e
cd "$(dirname "$0")"

PORT=8000
echo "Port $PORT kontrol ediliyor..."
PIDS=$(lsof -ti :$PORT 2>/dev/null || true)
if [ -n "$PIDS" ]; then
  echo "Port $PORT dolu, eski süreç kapatılıyor..."
  echo "$PIDS" | xargs kill -9 2>/dev/null || true
  sleep 2
  if lsof -i :$PORT >/dev/null 2>&1; then
    echo "Port hâlâ dolu. Manuel: kill -9 \$(lsof -ti :$PORT)"
    exit 1
  fi
  sleep 1
fi

echo ""
echo "=============================================="
echo "  Site:     http://127.0.0.1:$PORT"
echo "  Yönetici: http://127.0.0.1:$PORT/admin"
echo "=============================================="
echo ""

if [ -d .venv ]; then
  exec .venv/bin/uvicorn app.main:app --reload --port $PORT
elif [ -d venv ]; then
  exec venv/bin/uvicorn app.main:app --reload --port $PORT
else
  exec uvicorn app.main:app --reload --port $PORT
fi
