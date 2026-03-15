#!/usr/bin/env bash
# Testleri çalıştırıp HTML raporu oluşturur ve tarayıcıda açar (sunucu gerekmez).
# Kullanım: ./scripts/run_tests_with_report.sh

set -e
cd "$(dirname "$0")/.."
mkdir -p test-reports

# Önce proje sanal ortamındaki pytest, yoksa python -m pytest kullan
if [ -x ".venv/bin/pytest" ]; then
  .venv/bin/pytest
elif [ -x "venv/bin/pytest" ]; then
  venv/bin/pytest
elif python3 -m pytest --version >/dev/null 2>&1; then
  python3 -m pytest
elif python -m pytest --version >/dev/null 2>&1; then
  python -m pytest
else
  echo "pytest bulunamadı. Önce bağımlılıkları yükleyin:"
  echo "  python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
  exit 1
fi

REPORT="test-reports/report.html"
PDF_URL="http://127.0.0.1:8000/dev/test-report.pdf"
echo ""
echo "Rapor: $REPORT"
echo "PDF (sunucu açıksa): $PDF_URL"
echo "Not: PDF için adresi kopyalarken sonuna boşluk veya ek karakter eklemeyin."
if [ -f "$REPORT" ]; then
  if command -v open >/dev/null 2>&1; then
    open "$REPORT"
    echo "HTML rapor tarayıcıda açıldı."
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$REPORT"
    echo "HTML rapor tarayıcıda açıldı."
  else
    echo "Tarayıcıda açmak için: $REPORT dosyasını çift tıklayın veya tarayıcıya sürükleyin."
  fi
  # Sunucu 8000'de çalışıyorsa test raporu seçenek sayfasını aç (PDF/HTML butonları burada)
  if command -v curl >/dev/null 2>&1; then
    if curl -s -o /dev/null -w "%{http_code}" --connect-timeout 1 "http://127.0.0.1:8000/dev/test-report" 2>/dev/null | grep -q 200; then
      echo "Sunucu çalışıyor; test raporu sayfası açılıyor (PDF/HTML butonları orada)."
      if command -v open >/dev/null 2>&1; then
        open "http://127.0.0.1:8000/dev/test-report"
      elif command -v xdg-open >/dev/null 2>&1; then
        xdg-open "http://127.0.0.1:8000/dev/test-report"
      fi
    fi
  fi
fi
