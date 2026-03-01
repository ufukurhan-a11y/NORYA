#!/bin/bash
# Norya deploy — kodu GitHub'a push eder; Render bağlıysa otomatik canlıya alır.
# Kullanım: ./deploy/deploy.sh   veya   ./deploy/deploy.sh "Rapor PDF canlıda düzeltmesi"
set -e
cd "$(dirname "$0")/.."

if [ ! -d "app" ] || [ ! -f "requirements.txt" ]; then
  echo "Hata: Proje kökünde değilsiniz. cd /Users/ufukurhan/norya && ./deploy/deploy.sh"
  exit 1
fi

BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")
echo "Dal: $BRANCH"
echo ""

# Değişiklik var mı?
if git diff --quiet && git diff --cached --quiet; then
  echo "Yeni değişiklik yok. Yine de push etmek için: git push origin $BRANCH"
  read -p "Push yapılsın mı? (y/N) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[yY]$ ]]; then
    exit 0
  fi
  git push origin "$BRANCH"
else
  MSG="${1:-Deploy: $(date +%Y-%m-%d\ %H:%M)}"
  git add -A
  git status
  echo ""
  read -p "Commit mesajı (Enter = '$MSG'): " custom
  [ -n "$custom" ] && MSG="$custom"
  git commit -m "$MSG"
  git push origin "$BRANCH"
fi

echo ""
echo "=============================================="
echo "  Push tamamlandı."
echo "  Render bağlıysa birkaç dakika içinde"
echo "  https://noryaai.com güncellenecek."
echo "=============================================="
