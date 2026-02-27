# Norya – Deploy ve production

## 1. Render ile deploy

### 1.1 Repo’yu bağlama

1. [Render Dashboard](https://dashboard.render.com) → **New** → **Web Service**
2. Repo’yu bağlayın (GitHub/GitLab); **norya** projesini seçin
3. **Build Command:** `pip install --no-cache-dir -r requirements.txt`
4. **Start Command:** `gunicorn app.main:app -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT`
5. **Environment** sekmesinde aşağıdaki değişkenleri ekleyin

### 1.2 Ortam değişkenleri (Render Dashboard > Environment)

| Değişken | Açıklama |
|----------|----------|
| `OPENAI_API_KEY` | OpenAI API anahtarı (zorunlu) |
| `SECRET_KEY` | JWT ve oturum için (örn. `openssl rand -hex 32`) |
| `DATABASE_URL` | **Önerilen:** Render’da **PostgreSQL** ekleyin, otomatik `DATABASE_URL` verilir. Yoksa SQLite kullanılır (ephemeral disk – yeniden deploy’da silinir) |
| `ADMIN_SECRET` | Admin paneli ve `/payment/grant` için şifre |
| `CORS_ORIGINS` | Production: frontend origin (virgülle ayrılmış; boş = `*`) |
| `RATE_LIMIT_PER_MINUTE` | IP başına dakikada max istek (varsayılan 30) |
| PayTR için | `PAYTR_MERCHANT_ID`, `PAYTR_MERCHANT_KEY`, `PAYTR_MERCHANT_SALT`, `PAYTR_NOTIFICATION_URL`, `PAYTR_OK_URL`, `PAYTR_FAIL_URL` |

### 1.3 Blueprint (opsiyonel)

Repoda `render.yaml` var. **New** → **Blueprint** ile repoyu seçerseniz servis bu dosyaya göre oluşturulur; env’leri yine Dashboard’dan ekleyin.

### 1.4 Notlar

- Render `PORT` değişkenini verir; uygulama `0.0.0.0:$PORT` dinler
- Kalıcı veri için mutlaka **PostgreSQL** ekleyin (Render’da Create → PostgreSQL)
- PayTR callback için `PAYTR_NOTIFICATION_URL`: `https://<servis-adiniz>.onrender.com/api/payment/callback`

---

## 2. VPS (Ubuntu/Debian) production

### 2.1 Sunucuda hazırlık (tek script ile kurulum)

Projeyi VPS’e alın, **proje kökünde** scripti çalıştırın (sudo gerekir):

```bash
cd /var/www
git clone https://github.com/KULLANICI/norya.git
cd norya
sudo ./deploy/vps-setup.sh
```

Sadece uygulama + systemd kurulur. **Nginx + domain** ile kurmak için:

```bash
sudo ./deploy/vps-setup.sh norya.example.com
```

Script: sanal ortam (.venv), `pip install -r requirements.txt`, interaktif **.env sihirbazı** (OPENAI_API_KEY, SECRET_KEY, ADMIN_SECRET, DATABASE_URL; Enter = otomatik üretim), `.env` yoksa `.env.example`’dan kopyalar, systemd servisini yazar ve başlatır. Domain verirseniz Nginx’i de yapılandırır; SSL için `certbot --nginx -d norya.example.com` çalıştırmanız yeterli. Sonradan sadece .env güncellemek için: `./deploy/env-wizard.sh`

Aşağıdaki adımlar script olmadan elle kurulum içindir.

### 2.2 Sanal ortam ve bağımlılıklar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2.3 Ortam değişkenleri

Proje kökünde `.env` oluşturun (veya systemd ile env dosyası kullanın):

```bash
cp .env.example .env
nano .env   # OPENAI_API_KEY, SECRET_KEY, DATABASE_URL (postgresql://...), ADMIN_SECRET
```

Production’da `DATABASE_URL` için PostgreSQL kullanın. SQLite tek instance için çalışır ama yedekleme ve eşzamanlı yazma için PostgreSQL daha güvenli.

### 2.4 Gunicorn ile çalıştırma (manuel test)

```bash
source .venv/bin/activate
gunicorn app.main:app -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
# http://SUNUCU_IP:8000 ile dene
```

### 2.5 Systemd servisi

Projede hazır örnek: **`deploy/norya.service.example`**. Kopyalayıp düzenleyin; `User`, `WorkingDirectory` ve `EnvironmentFile` yollarını kendi sunucunuza göre ayarlayın.

```ini
[Unit]
Description=Norya FastAPI
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/norya
EnvironmentFile=/var/www/norya/.env
ExecStart=/var/www/norya/.venv/bin/gunicorn app.main:app -w 2 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:8000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

- `127.0.0.1:8000`: Nginx arkasında çalışacaksa sadece localhost dinler
- Nginx kullanmayacaksanız `-b 0.0.0.0:8000` yapıp firewall’da 8000 açın

Komutlar:

```bash
sudo systemctl daemon-reload
sudo systemctl enable norya
sudo systemctl start norya
sudo systemctl status norya
```

### 2.6 Nginx (reverse proxy + SSL)

Nginx kurulumu: `sudo apt install nginx`. Projede hazır örnek: **`deploy/nginx-norya.conf.example`**. `server_name`’i kendi domain’inizle değiştirip `/etc/nginx/sites-available/norya` olarak kopyalayın.

```nginx
server {
    listen 80;
    server_name norya.example.com;
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Aktifleştirme:

```bash
sudo ln -s /etc/nginx/sites-available/norya /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

SSL (Let’s Encrypt):

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d norya.example.com
```

### 2.7 Özet (VPS)

| Adım | Komut / dosya |
|------|----------------|
| Kod | `git clone` veya rsync → `/var/www/norya` |
| Venv | `python3 -m venv .venv && source .venv/bin/activate` |
| Bağımlılık | `pip install -r requirements.txt` |
| Env | `.env` (SECRET_KEY, OPENAI_API_KEY, DATABASE_URL, ADMIN_SECRET) |
| Servis | `norya.service` → systemd enable/start |
| Dış erişim | Nginx reverse proxy → 127.0.0.1:8000, SSL: certbot |

---

## 3. Production kontrol listesi

- [ ] `SECRET_KEY` güçlü ve benzersiz
- [ ] `DATABASE_URL` production DB (Render PostgreSQL veya VPS’te PostgreSQL)
- [ ] `OPENAI_API_KEY` geçerli
- [ ] PayTR kullanıyorsanız: `PAYTR_*` ve callback URL’leri doğru
- [ ] Admin: `ADMIN_SECRET` ayarlı
- [ ] HTTPS (Render otomatik; VPS’te certbot)
- [ ] Rate limit zaten uygulama içinde (IP bazlı)
