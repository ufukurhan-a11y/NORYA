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
echo "  Bilgisayardan: http://127.0.0.1:$PORT"
# macOS: Wi-Fi genelde en0; Linux: eth0 veya wlan0
if [ "$(uname)" = "Darwin" ]; then
  LOCAL_IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null)
fi
if [ -z "$LOCAL_IP" ]; then
  LOCAL_IP=$(ifconfig 2>/dev/null | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -1)
fi
if [ -n "$LOCAL_IP" ]; then
  echo "  Telefondan:    http://$LOCAL_IP:$PORT"
  echo "                 (telefon aynı Wi-Fi'de; bağlanmazsa Mac Güvenlik Duvarı'nı kontrol edin)"
else
  echo "  Telefondan:    http://<BILGISAYAR-IP>:$PORT  (Sistem Ayarları > Wi-Fi > Detaylar > IP)"
fi
echo ""
# 0.0.0.0 = ağdaki diğer cihazlar (telefon vb.) bağlanabilsin
$EXEC -m uvicorn app.main:app --reload --host 0.0.0.0 --port $PORT
