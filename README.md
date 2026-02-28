# Norya – SaaS Yol Haritası

Norya, kan tahlili sonuçlarını hastalara anlaşılır şekilde açıklayan bir AI servisi. Bu doküman, projeyi **SaaS** (abonelikli, çok kullanıcılı) hâline getirmek için adımları özetler.

---

## Siteyi çalıştırma (önce bunu yap)

**1. Terminali aç** (Cursor: Terminal → New Terminal).

**2. Şu komutu yazıp Enter’a bas:**
```bash
cd /Users/ufukurhan/norya && ./start.sh
```
*(Port 8000 doluysa `start.sh` eski sunucuyu kapatıp yeniyi açar.)*

**3. Şu yazıyı görünce** tarayıcıyı aç:
```text
Uvicorn running on http://127.0.0.1:8000
```

**4. Tarayıcıda tam şu adresi yaz (http ile, https değil):**
- Ana site: **http://127.0.0.1:8000**
- Admin panel: **http://127.0.0.1:8000/admin** veya **http://127.0.0.1:8000/yonetim**

Sunucu kapalıysa sayfa açılmaz. Terminalde `Uvicorn running on...` görünmüyorsa sunucu çalışmıyor demektir.

## Mevcut Durum

- **API:** FastAPI ile `/analyze` endpoint’i (OpenAI ile tahlil açıklama); `/health` ve `/api-check` sağlık kontrolleri.
- **Auth:** JWT tabanlı kayıt/giriş (`/auth/register`, `/auth/login`), e-posta doğrulama (SMTP ile), şifre sıfırlama; API v1 prefix: `/v1/auth/...` de kullanılabilir.
- **Veritabanı:** SQLite (geliştirme) veya PostgreSQL (production); kullanıcılar, analiz geçmişi, ödemeler, indirim kodları, admin paneli.
- **Ödeme:** PayTR entegrasyonu (tek analiz / aylık-yıllık Pro), misafir ödeme (kayıt olmadan tek analiz).
- **Güvenlik:** Rate limit (IP başına dakikada istek), güvenlik başlıkları (CSP, HSTS, X-Content-Type-Options), production’da debug endpoint’leri kapalı.

## SaaS için Gerekli Bileşenler

| Aşama | Bileşen | Açıklama |
|-------|---------|----------|
| 1 | **Kullanıcı & Auth** | Kayıt, giriş, JWT, şifre hash |
| 2 | **Veritabanı** | Kullanıcılar, analiz geçmişi, planlar |
| 3 | **Abonelik / Fiyatlandırma** | Planlar (ücretsiz / pro / kurumsal), Stripe vb. |
| 4 | **Frontend** | Giriş, dashboard, analiz ekranı |
| 5 | **API kotası & limitler** | Kullanım başına / aylık limit |
| 6 | **Ödeme entegrasyonu** | Stripe Checkout / Subscription |

## Proje Yapısı (Hedef)

```
norya/
├── app/
│   ├── main.py           # FastAPI uygulaması
│   ├── core/             # config, db, güvenlik
│   ├── models/           # veritabanı modelleri
│   ├── schemas/          # Pydantic şemaları
│   ├── api/              # route’lar (auth, analyze, vb.)
│   └── services/         # iş mantığı (OpenAI, e-posta vb.)
├── requirements.txt
├── .env.example
└── README.md
```

## Hızlı Başlangıç

```bash
# Sanal ortam ve bağımlılıklar
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# .env dosyasını düzenle (OPENAI_API_KEY, SECRET_KEY, DATABASE_URL)
cp .env.example .env

# İlk çalıştırma (veritabanı tabloları oluşturulur)
uvicorn app.main:app --reload
```

- **Web arayüzü (Kantesti tarzı):** http://localhost:8000/
- **API health:** http://localhost:8000/health
- **Kayıt:** POST http://localhost:8000/auth/register
- **Giriş:** POST http://localhost:8000/auth/login
- **Analiz (giriş gerekli):** POST http://localhost:8000/analyze

Frontend `static/index.html` tek sayfa: mor tema, hero, “Nasıl çalışır”, giriş/kayıt modalleri ve tahlil metni analiz kutusu. [Kantesti](https://www.kantesti.net/tr/) benzeri yapıdadır.

## Misafir ödeme (kayıt olmadan tek analiz)

- **Tek analiz** kartında giriş yapmamış kullanıcılar "Tek Analiz" butonuna basınca **kayıt olmadan ödeme** modali açılır.
- E-posta (zorunlu) ve isim (opsiyonel) girilir; **Güvenli ödemeye geç** ile PayTR iframe açılır.
- Ödeme sonrası PayTR kullanıcıyı sitede `#payment-ok&guest_token=...` ile yönlendirir; sayfa bu token ile `/auth/guest-login` çağırıp oturum açar ve kullanıcıyı analiz sayfasına götürür.
- Aylık/yıllık planlar için giriş zorunludur; misafir ödeme **sadece tek analiz** için geçerlidir.

## "Ödeme şu an aktif değil" hatası

Bu mesaj **güvenlik** değil, **PayTR’nin yapılandırılmamış olması** anlamına gelir. Ödemeyi açmak için:

1. **PayTR** hesabı açın ve Mağaza Panel’den **Entegrasyon Bilgileri**ne girin.
2. **.env** dosyasına şu 3 değişkeni ekleyin (yorum satırını kaldırıp değerleri yapıştırın):
   - `PAYTR_MERCHANT_ID=...`
   - `PAYTR_MERCHANT_KEY=...`
   - `PAYTR_MERCHANT_SALT=...`
3. Sunucuyu yeniden başlatın (`./start.sh` veya `uvicorn app.main:app --reload`).

Test için `PAYTR_TEST_MODE=1` ekleyebilirsiniz. Canlıya geçince `0` yapın.

## Norton / güvenlik rozeti nasıl alınır?

Kantesti gibi sitelerde gördüğünüz **"Norton Secured"** rozetleri ticari güvenlik hizmetidir. Norya şu an bu rozeti kullanmıyor; ödeme sayfasında **256-bit SSL** ve **PayTR** ifadeleri kullanılıyor. İleride eklemek için DigiCert (digicert.com) veya benzeri sağlayıcılardan SSL/site doğrulama hizmeti satın alınır (yıllık ücretli). Norya için zorunlu değildir; HTTPS ve PayTR yeterlidir.

## Sonraki Adımlar

1. Frontend (React/Next.js veya basit bir dashboard) eklemek
2. Stripe ile abonelik ve ödeme
3. Kullanım limitleri ve kota yönetimi
4. E-posta (şifre sıfırlama, hoş geldin)

İstersen bir sonraki adımı birlikte seçebiliriz (örn. “Stripe ekle” veya “basit bir React giriş sayfası yap”).
