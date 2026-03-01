# Render’da Web Service Nasıl Oluşturulur?

Adım adım: Norya’yı Render’da 7/24 çalışan bir web servisi yapmak.

---

## Zaten Render’da Norya servisi var mı?

**Varsa yeni servis açma, tekrar para verme.** Mevcut Web Service’i kullan:

1. **render.com** → Dashboard → **norya** (veya Norya’nın bağlı olduğu servis) servisine tıkla.
2. Kod güncellemek için: GitHub’a push at → Render **otomatik** yeni deploy alır (Auto-Deploy açıksa).
3. Veya **Manual Deploy** → **Deploy latest commit** ile elle deploy al.
4. Environment (OPENAI_API_KEY vb.) değiştirmek için: **Environment** sekmesi → değişkeni ekle/düzenle → **Save** (gerekirse **Manual Deploy** tetiklenir).

Yani **tek Web Service = tek ödeme**. Yeni servis oluşturman gerekmez; mevcut servisi güncel tutman yeterli.

---

## 1. Render hesabı (yeni servis açacaksan)

1. Tarayıcıda **https://render.com** aç.
2. **Get Started for Free** (veya **Sign Up**) tıkla.
3. **Sign up with GitHub** seç → GitHub ile giriş yap.
4. Render’a “Repository access” isteyecek; **NORYA** (veya Norya’nın olduğu repo) erişimine izin ver.

---

## 2. Yeni Web Service

1. Render **Dashboard**’da sağ üst **New +** butonuna tıkla.
2. Açılan menüden **Web Service** seç.
3. **Connect a repository** ekranında:
   - GitHub’da **NORYA** (veya `norya` / `ufukurhan-a11y/NORYA`) reposunu ara.
   - Görünmüyorsa **Configure account** ile GitHub’dan daha fazla repo erişimi ver.
   - Repoyu bulunca yanındaki **Connect**’e tıkla.

---

## 3. Ayarlar (Render otomatik doldurur)

Repo bağlandığında Render, projedeki **render.yaml** dosyasını okur. Genelde şunlar gelir:

| Alan | Değer (Norya için) |
|------|---------------------|
| **Name** | `norya` (istersen `noryaai` yaz) |
| **Region** | Frankfurt veya en yakın bölge |
| **Runtime** | **Docker** (render.yaml’da `runtime: docker` var) |
| **Instance Type** | **Free** (deneme) veya **Starter** (7/24 uyanık kalsın) |

Build / Start komutları **Dockerfile**’dan alınır; ekstra bir şey yazmana gerek yok.

---

## 4. Environment (ortam) değişkenleri

Aynı sayfada **Environment** veya **Environment Variables** bölümüne in.

**Add Environment Variable** ile tek tek ekle:

| Key | Value |
|-----|--------|
| `ENVIRONMENT` | `production` |
| `SECRET_KEY` | Rastgele güçlü key (terminalde: `openssl rand -hex 32`) |
| `OPENAI_API_KEY` | `sk-...` (OpenAI’dan aldığın anahtar) |
| `FRONTEND_URL` | `https://noryaai.com` (veya Render URL: `https://norya-xxxx.onrender.com`) |
| `CORS_ORIGINS` | `https://noryaai.com,https://www.noryaai.com` (veya Render URL’ini ekle) |

İsteğe bağlı (e-posta, ödeme, admin):

- `ADMIN_SECRET` → Admin paneline giriş şifresi
- `SMTP_HOST`, `SMTP_USER`, `SMTP_PASSWORD`, `SMTP_FROM` → Şifre sıfırlama maili
- `PAYTR_MERCHANT_ID`, `PAYTR_MERCHANT_KEY`, `PAYTR_MERCHANT_SALT`, `PAYTR_NOTIFICATION_URL`, `PAYTR_OK_URL`, `PAYTR_FAIL_URL` → Ödeme

---

## 5. Servisi oluştur

1. En altta **Create Web Service** butonuna tıkla.
2. Render önce **build** alır (Docker image, birkaç dakika sürebilir).
3. **Logs** sekmesinden build ve başlangıç loglarını izleyebilirsin.
4. Build bitince servis **Live** olur; sağ üstte **https://norya-xxxx.onrender.com** gibi bir URL görünür.
5. Bu linke tıklayıp siteyi dene (kayıt, giriş, analiz).

---

## 6. Özel domain (noryaai.com) – isteğe bağlı

1. Render’da servise tıkla → sol menü **Settings** → **Custom Domains**.
2. **Add Custom Domain** → `noryaai.com` yaz → Add.
3. Render sana bir **CNAME** hedefi verir (örn. `norya-xxxx.onrender.com`).
4. **Cloudflare** (veya domain sağlayıcın) DNS’e gir:
   - **CNAME** kaydı: Name `@` veya `noryaai.com`, Target = Render’ın verdiği adres.
   - **www** için: Name `www`, Target = `noryaai.com` veya Render URL.
5. Bir süre sonra **https://noryaai.com** açılır.

---

## Özet

1. **render.com** → GitHub ile giriş → **New +** → **Web Service**.
2. **NORYA** reposunu **Connect** et.
3. **Name**, **Runtime: Docker**, **Instance Type** kontrol et.
4. **Environment**’a `ENVIRONMENT`, `SECRET_KEY`, `OPENAI_API_KEY`, `FRONTEND_URL`, `CORS_ORIGINS` ekle.
5. **Create Web Service** → build bitene kadar bekle → URL’den test et.
6. İstersen **Custom Domains** ile noryaai.com bağla.

Detaylı deploy ve domain: **docs/RENDER-DEPLOY.md**
