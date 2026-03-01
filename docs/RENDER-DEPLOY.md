# Norya — Render’da Yayına Alma

Domain: **noryaai.com** (Cloudflare’de hazır). Bu rehber Render Web Service + özel domain bağlama adımlarını anlatır.

---

## 1. Render hesabı ve repo bağlama

1. **https://render.com** → **Get Started** (veya Sign Up).
2. **Sign up with GitHub** ile giriş yap; Render’a GitHub erişim izni ver.
3. **Dashboard** → **New +** → **Web Service**.
4. **Connect a repository** bölümünde **ufukurhan-a11y/NORYA** reposunu seç (görünmüyorsa “Configure account” ile GitHub’dan repo erişimini aç).
5. **Connect**’e tıkla.

---

## 2. Web Service ayarları

Render otomatik olarak şunları algılar (repo’daki `render.yaml` sayesinde):

- **Name:** norya (istersen değiştir, örn. noryaai)
- **Runtime:** Python
- **Build Command:** `pip install --no-cache-dir -r requirements.txt`
- **Start Command:** `gunicorn app.main:app -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT`

Bunları olduğu gibi bırak. **Instance type:** Free (başlangıç için) veya ücretli plan.

**Create Web Service**’e basma; önce Environment değişkenlerini ekle (3. adım).

---

## 3. Environment (ortam) değişkenleri

Aynı sayfada **Environment** / **Environment Variables** bölümüne git. **Add Environment Variable** ile şunları ekle:

| Key | Value | Zorunlu |
|-----|--------|--------|
| `ENVIRONMENT` | `production` | Evet |
| `SECRET_KEY` | Rastgele güçlü key (örn. `openssl rand -hex 32` çıktısı) | Evet |
| `OPENAI_API_KEY` | Mevcut OpenAI anahtarın (sk-...) | Evet |
| `FRONTEND_URL` | `https://noryaai.com` | Evet |
| `CORS_ORIGINS` | `https://noryaai.com,https://www.noryaai.com` | Evet |
| `DATABASE_URL` | Boş bırakırsan SQLite kullanır (Render’da kalıcı değil). Kalıcı için Render PostgreSQL ekleyip connection string yapıştır. | İsteğe bağlı |
| `SMTP_HOST` / `SMTP_USER` / `SMTP_PASSWORD` / `SMTP_FROM` | E-posta (şifre sıfırlama) için | İsteğe bağlı |
| `PAYTR_MERCHANT_ID` / `PAYTR_MERCHANT_KEY` / `PAYTR_MERCHANT_SALT` | PayTR bilgilerin | Ödeme için |
| `PAYTR_NOTIFICATION_URL` | `https://noryaai.com/api/payment/callback` | Ödeme için |
| `PAYTR_OK_URL` | `https://noryaai.com/#payment-ok` | Ödeme için |
| `PAYTR_FAIL_URL` | `https://noryaai.com/#pricing` | Ödeme için |

En azından: `ENVIRONMENT`, `SECRET_KEY`, `OPENAI_API_KEY`, `FRONTEND_URL`, `CORS_ORIGINS` doldur.

---

## 4. Servisi oluştur ve ilk deploy

1. **Create Web Service**’e tıkla.
2. Render build alır ve uygulamayı başlatır. **Logs** sekmesinden ilerlemeyi izle.
3. Bittiğinde sağ üstte **norya-xxxx.onrender.com** gibi bir URL görünür. Tıklayıp siteyi dene (kayıt, giriş, analiz).

---

## 5. Özel domain: noryaai.com

1. Render Dashboard’da **norya** servisini aç.
2. Sol menüden **Settings** → **Custom Domains**.
3. **Add Custom Domain** → **noryaai.com** yaz → Add.
4. Render sana bir **CNAME** hedefi verir (örn. `norya-xxxx.onrender.com`). Not al.

**Cloudflare’de DNS:**

1. **dash.cloudflare.com** → **noryaai.com** → **DNS** → **Records**.
2. **CNAME** ekle:
   - **Name:** `@` (veya boş; bazı panelde “apex” için A kaydı istenir, o zaman Render’ın verdiği A kaydını kullan).
   - **Target:** Render’ın verdiği adres (örn. `norya-xxxx.onrender.com`).
   - **Proxy status:** Proxied (turuncu bulut) açık.
3. **www** için bir **CNAME** daha:
   - **Name:** `www`
   - **Target:** `noryaai.com` veya Render URL’i (panel ne istiyorsa).
   - **Proxy:** Açık.

Not: Cloudflare’de root domain (`@`) için bazen CNAME yerine **A** kaydı istenir; Render “Custom domain” sayfasında root için ne yazıyorsa (A veya CNAME) onu uygula.

---

## 6. SSL (HTTPS)

Render, özel domain eklediğinde otomatik SSL sağlar. Cloudflare proxy açıksa HTTPS ziyaret sorunsuz çalışır.

**Uygulama tarafı:** Production’da (`ENVIRONMENT=production`) FastAPI, HTTP ile gelen istekleri otomatik olarak HTTPS’e yönlendirir (302). Böylece PayTR ve tarayıcılar siteyi güvenli görür. Yönlendirmeyi kapatmak için `FORCE_HTTPS_REDIRECT=0` kullanabilirsiniz.

---

## 7. Kontrol

- **https://noryaai.com** aç (DNS yayılımı 5–30 dakika sürebilir).
- Kayıt, giriş, analiz, gerekirse ödeme akışını test et.
- `.env`’de eksik bir şey varsa (ör. PayTR) Render **Environment**’tan ekleyip **Manual Deploy** → **Clear build cache & deploy** ile yeniden deploy et.

---

## Özet

1. render.com → GitHub ile giriş → New Web Service → NORYA repo.
2. Build/Start komutları `render.yaml`’dan gelir; Environment’a `ENVIRONMENT`, `SECRET_KEY`, `OPENAI_API_KEY`, `FRONTEND_URL`, `CORS_ORIGINS` ekle.
3. Create Web Service → ilk deploy.
4. Settings → Custom Domains → noryaai.com ekle.
5. Cloudflare DNS’te noryaai.com ve www’yi Render’a yönlendir.
6. https://noryaai.com ile test et.

---

## Analiz "geçici olarak hata veriyor" / zaman aşımı

Bu mesaj **domain’den değil**, aşağıdakilerden biri yüzünden çıkar:

| Kaynak | Açıklama |
|--------|----------|
| **Host (Render)** | Free tier’da ~15 dk hareketsizlikten sonra servis uyur. İlk istek **cold start** tetikler; sunucu 30–60 sn uyanır, bazen ilk istek timeout’a düşer. |
| **OpenAI (ChatGPT API)** | Ağ kesintisi, rate limit veya API’nin yavaş yanıtı. Backend 503/502 döner; kullanıcı "Servis geçici olarak yanıt vermiyor" görür. |

**Yapılan iyileştirmeler (kodda):**

- OpenAI timeout 30 → **90 saniye** (görsel analiz için yeterli süre).
- Bağlantı hatasında **2. retry** (APIConnectionError’da ek deneme).
- Frontend analiz isteği **90 sn** (metin), **120 sn** (PDF/görsel yükleme) bekliyor; zaman aşımında net mesaj.

**Cold start’ı azaltmak:**

- **Uptime Robot** (veya benzeri) ile 5 dk’da bir `https://noryaai.com/health` ping’le; servis uyumaz.
- Veya Render’da **ücretli plan** (Always On); servis uyumaz.

**OpenAI tarafı:**

- Rate limit alıyorsan `.env`’e ikinci anahtar ekle: `OPENAI_API_KEYS=sk-...,sk-...` (fallback kullanılır).
- Billing açık ve kota yeterli mi kontrol et.

---

## PDF "Raporu İndir" 500 veya hata veriyorsa

1. **Server logları:** Render Dashboard → norya servisi → **Logs**. "PDF build failed" veya WeasyPrint/cairo ile ilgili satırları kontrol et.
2. **WeasyPrint sistem kütüphaneleri:** Varsayılan Python buildpack’te cairo/pango yoksa PDF 500 döner. Çözüm: **Docker ile build**.
   - Repo’da `Dockerfile` var (WeasyPrint için cairo/pango kurulu).
   - Render’da: **Settings** → **Build & Deploy** → **Environment** → **Docker** seç (veya "Dockerfile" kullan). **Save** → **Manual Deploy**.
3. **401/403:** Tarayıcıda F12 → Network → "Raporu İndir" tıkla. `pdf-token` isteğinin response status’una bak. 401 ise giriş token’ı gidmiyor; 403 ise yetki/ban. Console’da `[PDF] Token response status: ...` log’u da görünür.
