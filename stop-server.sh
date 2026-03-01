#!/bin/bash
# Port 8000'de çalışan Norya sunucusunu kapatır.
PORT=8000
PID=$(lsof -ti :$PORT 2>/dev/null)
if [ -z "$PID" ]; then
  echo "Port $PORT'da çalışan süreç yok."
  exit 0
fi
kill $PID 2>/dev/null
echo "Sunucu kapatıldı (PID: $PID)."
