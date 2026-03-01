# MinIO nasıl çalıştırılır (PDF depolama)

MinIO, PDF raporlarını saklamak için kullanılır. Aşağıdaki yollardan birini seçebilirsin.

---

## 1. Lokal: Docker ile (en kolay)

Bilgisayarında Docker kuruluysa tek komutla MinIO’yu ayağa kaldırırsın.

```bash
docker run -d \
  --name minio \
  -p 9000:9000 \
  -p 9001:9001 \
  -e MINIO_ROOT_USER=minioadmin \
  -e MINIO_ROOT_PASSWORD=minioadmin123 \
  minio/minio server /data --console-address ":9001"
```

- **API (uygulama):** http://localhost:9000  
- **Web konsol:** http://localhost:9001 (tarayıcıdan bucket / ayarlara bakabilirsin)

**.env** dosyana ekle (MinIO’yu PDF için açmak için):

```env
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin123
MINIO_BUCKET=norya-pdf
MINIO_SECURE=0
MINIO_USE_FOR_PDF=1
```

`MINIO_SECURE=0` çünkü lokal http kullanıyorsun. Kaydedip uygulamayı yeniden başlat. Artık “Raporu İndir” dediğinde PDF MinIO’ya yüklenecek ve indirme oradan presigned URL ile yapılacak.

---

## 2. Lokal: Docker Compose

Proje kökünde `docker-compose.yml` (veya `compose.yaml`) oluşturup MinIO’yu servis olarak tanımlayabilirsin:

```yaml
services:
  minio:
    image: minio/minio
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin123
    command: server /data --console-address ":9001"
    volumes:
      - minio_data:/data

volumes:
  minio_data: {}
```

Çalıştırmak:

```bash
docker compose up -d minio
```

.env ayarları yine **1. adım**daki gibi: `MINIO_ENDPOINT=localhost:9000`, `MINIO_ACCESS_KEY=minioadmin`, `MINIO_SECRET_KEY=minioadmin123`, `MINIO_BUCKET=norya-pdf`, `MINIO_SECURE=0`, `MINIO_USE_FOR_PDF=1`.

---

## 3. Canlı (Render / bulut)

Canlıda MinIO kullanmak için:

- **Seçenek A:** Render’da ayrı bir **Private Service** olarak MinIO çalıştır (Docker image: `minio/minio`). Render sadece kendi ağından erişim verir; `MINIO_ENDPOINT` olarak Render’ın verdiği internal host:port’u kullanırsın.
- **Seçenek B:** Dışarıda bir MinIO/S3 servisi kullan (örn. [MinIO Cloud](https://min.io/cloud), [DigitalOcean Spaces](https://www.digitalocean.com/products/spaces), [AWS S3](https://aws.amazon.com/s3/)). Bunlar S3 uyumlu API verir; MinIO client ile konuşabilirsin.

Render **Environment** kısmına ekle:

```env
MINIO_ENDPOINT=your-minio-host.com
MINIO_ACCESS_KEY=...
MINIO_SECRET_KEY=...
MINIO_BUCKET=norya-pdf
MINIO_SECURE=1
MINIO_USE_FOR_PDF=1
```

---

## 4. MinIO’yu kullanmak zorunda mıyım?

Hayır. Bu değişkenleri **hiç doldurmazsan** veya **MINIO_USE_FOR_PDF=0** bırakırsan uygulama PDF’i eskisi gibi kendisi üretir ve doğrudan indirir; MinIO’ya hiç dokunmaz. MinIO sadece “PDF’i object storage’a at, indirmeyi oradan yap” istediğinde kullanılır.

---

## Özet

| Ortam        | MinIO nasıl çalışır        | .env’de ne yazmalı                          |
|-------------|----------------------------|---------------------------------------------|
| Lokal       | `docker run ... minio/minio` veya `docker compose up -d minio` | `MINIO_ENDPOINT=localhost:9000`, `MINIO_SECURE=0`, `MINIO_USE_FOR_PDF=1` |
| Canlı       | Render’da ayrı MinIO servisi veya harici S3/MinIO | `MINIO_ENDPOINT=host`, `MINIO_SECURE=1`, `MINIO_USE_FOR_PDF=1` |

Hepsi için: `MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY`, `MINIO_BUCKET` (örn. `norya-pdf`) dolu olmalı.
