#!/bin/bash
# Python sunucusunu kapatıp tekrar açar (port 8000).
cd "$(dirname "$0")"

echo "Sunucu kapatılıyor (port 8000)..."
lsof -ti :8000 | xargs kill -9 2>/dev/null
sleep 2

echo "Sunucu başlatılıyor..."
if [ -d .venv ]; then
  exec .venv/bin/uvicorn app.main:app --reload --port 8000
elif [ -d venv ]; then
  exec venv/bin/uvicorn app.main:app --reload --port 8000
else
  exec uvicorn app.main:app --reload --port 8000
fi
