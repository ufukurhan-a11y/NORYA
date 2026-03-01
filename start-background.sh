#!/bin/bash
# Norya sunucusunu arka planda başlatır. Terminal kapatılsa da çalışmaya devam eder.
# Durdurmak için: ./stop-server.sh veya  lsof -ti :8000 | xargs kill

cd "$(dirname "$0")"
PORT=8000
LOG="norya-server.log"

# Zaten çalışıyorsa uyar
if lsof -ti :$PORT >/dev/null 2>&1; then
  echo "Port $PORT zaten kullanımda. Önce ./stop-server.sh ile kapatın veya: kill \$(lsof -ti :$PORT)"
  exit 1
fi

# .venv varsa onu kullan
if [ -x ".venv/bin/python" ]; then
  EXEC=".venv/bin/python"
elif [ -x "venv/bin/python" ]; then
  EXEC="venv/bin/python"
else
  EXEC="python3"
fi

echo "Sunucu arka planda başlatılıyor (log: $LOG)..."
nohup $EXEC -m uvicorn app.main:app --reload --host 127.0.0.1 --port $PORT >> "$LOG" 2>&1 &
echo "  Ana sayfa: http://127.0.0.1:$PORT"
echo "  Admin:     http://127.0.0.1:$PORT/admin"
echo "  Durdurmak: ./stop-server.sh"
echo "  Log:       tail -f $LOG"
