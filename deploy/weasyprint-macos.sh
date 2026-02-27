#!/usr/bin/env bash
# WeasyPrint sistem kütüphaneleri (macOS) – PDF raporu için gerekli.
# Bir kez çalıştır: ./deploy/weasyprint-macos.sh
# Gerekirse önce: sudo chown -R $(whoami) /opt/homebrew/Cellar /opt/homebrew/lib /opt/homebrew/opt /opt/homebrew/share 2>/dev/null

set -e
echo "WeasyPrint bağımlılıkları yükleniyor (Homebrew)..."
brew install pango gdk-pixbuf libffi
echo "Tamam. PDF indirme artık çalışmalı."
