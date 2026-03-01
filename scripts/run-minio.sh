#!/bin/bash
# MinIO'yu Docker ile başlatır (PDF depolama için).
# Kullanım: ./scripts/run-minio.sh
# Gereksinim: Docker kurulu olmalı (https://docs.docker.com/get-docker/)

set -e
echo "MinIO başlatılıyor (port 9000 API, 9001 konsol)..."

if ! command -v docker &>/dev/null; then
  echo "Hata: Docker bulunamadı. Önce Docker kurun: https://docs.docker.com/get-docker/"
  exit 1
fi

# Eski container varsa kaldır
docker rm -f minio 2>/dev/null || true

docker run -d \
  --name minio \
  -p 9000:9000 \
  -p 9001:9001 \
  -e MINIO_ROOT_USER=minioadmin \
  -e MINIO_ROOT_PASSWORD=minioadmin123 \
  minio/minio server /data --console-address ":9001"

echo ""
echo "MinIO çalışıyor."
echo "  API:    http://localhost:9000"
echo "  Konsol: http://localhost:9001 (minioadmin / minioadmin123)"
echo ""
echo ".env örneği (PDF için MinIO kullanacaksan):"
echo "  MINIO_ENDPOINT=localhost:9000"
echo "  MINIO_ACCESS_KEY=minioadmin"
echo "  MINIO_SECRET_KEY=minioadmin123"
echo "  MINIO_BUCKET=norya-pdf"
echo "  MINIO_SECURE=0"
echo "  MINIO_USE_FOR_PDF=1"
