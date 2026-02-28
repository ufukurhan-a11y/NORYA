#!/bin/bash
# Norya sunucusunu localhost:8000'de başlatır.
# Port meşgulse önce eski süreci kapatır.

cd "$(dirname "$0")"
PORT=8000

# Port 8000 meşgulse kullanan süreci kapat
PID=$(lsof -ti :$PORT 2>/dev/null)
if [ -n "$PID" ]; then
  echo "Port $PORT kullanımda (PID: $PID). Kapatılıyor..."
  kill $PID 2>/dev/null
  sleep 2
fi

# .venv varsa onu kullan, yoksa venv dene
if [ -x ".venv/bin/python" ]; then
  EXEC=".venv/bin/python"
elif [ -x "venv/bin/python" ]; then
  EXEC="venv/bin/python"
else
  EXEC="python3"
fi

echo "Sunucu başlatılıyor:"
echo "  Ana sayfa: http://127.0.0.1:$PORT"
echo "  Admin:     http://127.0.0.1:$PORT/admin"
echo ""
$EXEC -m uvicorn app.main:app --reload --host 127.0.0.1 --port $PORT
