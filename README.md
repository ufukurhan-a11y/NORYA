# Norya – SaaS Yol Haritası

Norya, kan tahlili sonuçlarını hastalara anlaşılır şekilde açıklayan bir AI servisi. Bu doküman, projeyi **SaaS** (abonelikli, çok kullanıcılı) hâline getirmek için adımları özetler.

## Mevcut Durum

- **API:** FastAPI ile `/analyze` endpoint’i (OpenAI ile tahlil açıklama)
- **Auth:** Yok (herkes API’yi kullanabilir)
- **Veri:** Kalıcı depolama yok

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

## Sonraki Adımlar

1. Frontend (React/Next.js veya basit bir dashboard) eklemek
2. Stripe ile abonelik ve ödeme
3. Kullanım limitleri ve kota yönetimi
4. E-posta (şifre sıfırlama, hoş geldin)

İstersen bir sonraki adımı birlikte seçebiliriz (örn. “Stripe ekle” veya “basit bir React giriş sayfası yap”).
