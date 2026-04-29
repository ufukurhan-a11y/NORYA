# NoryaAI — Tam Mimari Dokümanı

> Oluşturulma: 2026-04-11
> Versiyon: 1.0

---

## İçindekiler

1. [Genel Bakış](#1-genel-bakis)
2. [Backend Mimarisi](#2-backend-mimarisi)
3. [Veritabanı Yapısı](#3-veritabani-yapisi)
4. [OpenAI / ChatGPT Entegrasyonu](#4-openai--chatgpt-entegrasyonu)
5. [Ödeme Altyapısı (PayTR)](#5-odeme-altyapisi-paytr)
6. [Frontend Mimarisi](#6-frontend-mimarisi)
7. [Kurumsal / B2B Sistem](#7-kurumsal--b2b-sistem)
8. [Güvenlik](#8-guvenlik)
9. [Deployment](#9-deployment)
10. [Dosya Yapısı](#10-dosya-yapisi)

---

## 1. Genel Bakış

NoryaAI, kan tahlili sonuçlarını AI ile analiz edip anlaşılır raporlar üreten bir SaaS platformudur.

### Teknoloji Yığını

| Katman | Teknoloji |
|--------|-----------|
| Backend | Python 3.12+ / FastAPI / Uvicorn / Gunicorn |
| Veritabanı | SQLite (dev) / PostgreSQL (prod) |
| ORM | SQLModel (SQLAlchemy + Pydantic) |
| AI | OpenAI GPT-4o-mini |
| Ödeme | PayTR (Türkiye ödeme altyapısı) |
| Frontend | Jinja2 şablonları + Tailwind CSS + Vanilla JS |
| i18n | 9 dil desteği (TR, EN, DE, FR, ES, IT, HE, HI, AR) |
| Analitik | Google Analytics 4, Google Ads, Meta Pixel, LinkedIn Insight |
| E-posta | SMTP (şifre sıfırlama, drip campaign) |
| Depolama | MinIO (S3 uyumlu, PDF raporlar için) |
| Fatura | GİB e-Arşiv (Türk e-Fatura sistemi) |

### Temel Özellikler

- Kan tahlili yükleme (metin, PDF, görsel)
- AI destekli analiz ve rapor üretimi
- PDF rapor oluşturma ve QR doğrulama
- Kullanıcı kayıt/giriş sistemi
- Ücretli planlar (tek seferlik, aylık, yıllık)
- Kurumsal (B2B) hastane/klinik yönetimi
- Admin paneli (kullanıcı, ödeme, kurum, blog, SEO yönetimi)
- Çoklu dil desteği
- Blog ve SEO içerikleri
- PWA desteği

---

## 2. Backend Mimarisi

### 2.1 Framework ve Başlatma

```python
# app/main.py
app = FastAPI(title="Norya API", description="Kan tahlili açıklama SaaS API", lifespan=lifespan)
```

**lifespan** fonksiyonu uygulama başlarken şunları yapar:
1. Veritabanı tablolarını oluşturur (`init_db()`)
2. Eksik sütunları ekler (ALTER TABLE migrasyonları)
3. Kurum kotalarını sıfırlar (eğer gün geldiyse)
4. Drip campaign daemon thread'ini başlatır (opsiyonel)

### 2.2 Middleware Sırası

1. **Static Cache-Control** — `/static/*` dosyalarına cache header ekler
   - CSS/JS/font: 1 yıl
   - Resimler: 30 gün
2. **SlowAPIMiddleware** (SlowAPI) — Rate limiting
3. **CORSMiddleware** — `settings.cors_origins` ile yapılandırılır
4. **ForceHTTPSRedirectMiddleware** — Production'da HTTP→HTTPS yönlendirme

### 2.3 Rate Limiting (SlowAPI)

| Endpoint | Limit |
|----------|-------|
| Global | 60/dakika (IP bazlı) |
| Login | 5/dakika, 20/saat |
| Register | 3/dakika, 100/saat |
| /analyze | 10/dakika |
| /api/chat | 15/dakika |

### 2.4 Router Yapısı

```python
# app/main.py içindeki router kayıtları
app.include_router(auth_router)              # /auth/* (register, login, me, profile, password)
app.include_router(auth_router, prefix="/v1") # /v1/auth/* (geriye uyumluluk)
app.include_router(institution_api_router)    # /api/institution/* (kurum API)
app.include_router(institution_page_router)   # /institution/join/* (davet sayfası)
app.include_router(enterprise_router)         # /enterprise/* (kurumsal dashboard)
app.include_router(new_admin_router)          # /admin/* (yeni modüler admin paneli)
app.include_router(admin_router)              # /admin (eski admin API)
```

### 2.5 Ana Sayfa Route'ları (decorator-based, main.py içinde)

| Route | Açıklama |
|-------|----------|
| `GET /` | Ana sayfa (multi-method: GET/HEAD/OPTIONS/POST) |
| `GET /tr, /en, /de` | Dil bazlı ana sayfalar |
| `GET /pricing` | Fiyatlandırma sayfası |
| `GET /pay` | Ödeme sayfası |
| `POST /paytr/init` | PayTR ödeme başlatma |
| `POST /paytr/callback` | PayTR webhook |
| `GET /analyze/*` | Analiz yükleme/sonuç sayfaları |
| `POST /api/analyze` | Analiz API endpoint'i |
| `POST /api/upload` | Dosya yükleme API'si |
| `GET /blog/*` | Blog yazıları |
| `GET /kurumsal` | Kurumsal sayfa |
| `GET /for-doctors` | Doktorlar için sayfa |
| `GET /enterprise/*` | Kurumsal dashboard sayfaları |
| `GET /admin/*` | Admin paneli sayfaları |
| `GET /health` | Sağlık kontrolü |
| `GET /robots.txt, /sitemap.xml, /llms.txt` | SEO dosyaları |

### 2.6 Admin Alt Router'ları (app/admin/routers/)

| Router | Prefix | Açıklama |
|--------|--------|----------|
| dashboard | /admin | Admin dashboard |
| users | /admin/users | Kullanıcı yönetimi |
| analyses | /admin/analyses | Analiz kayıtları |
| payments | /admin/payments | Ödeme yönetimi |
| institutions | /admin/institutions | Kurum yönetimi |
| coupons | /admin/coupons | Kupon yönetimi |
| pricing-plans | /admin/pricing-plans | Fiyat planları |
| revenue | /admin/revenue | Gelir analitiği |
| blog | /admin/blog | Blog yönetimi |
| seo | /admin/seo | SEO dashboard (GSC, IndexNow) |
| errors | /admin/errors | Hata logları |
| security | /admin/security | Güvenlik logları |
| uploads | /admin/uploads | Yükleme logları |
| queue | /admin/queue | Analiz kuyruğu |
| live | /admin/live | Canlı kullanıcı takibi |
| live_analytics | — | Canlı analitik |
| email-verifications | /admin/email-verifications | E-posta doğrulama |
| reports | /admin/reports | Rapor yönetimi |
| billing-links | /admin/billing-links | Faturalandırma linkleri |
| enterprise_leads | /admin/enterprise-leads | Kurumsal talep yönetimi |

### 2.7 Servisler (app/services/)

| Servis | Açıklama |
|--------|----------|
| `analyze.py` | Kan tahlili AI analizi (OpenAI) |
| `report_pdf.py` | PDF rapor üretimi (çoklu dil) |
| `report_verification.py` | QR doğrulama token'ı |
| `pdf_extract.py` | PDF'den metin çıkarma (pypdf) |
| `lab_parser.py` | Laboratuvar sonuçlarını parse etme |
| `risk_engine.py` | Risk göstergesi hesaplama |
| `pricing.py` | Fiyatlandırma mantığı |
| `coupon.py` | Kupon doğrulama ve uygulama |
| `paytr_refund.py` | PayTR iade işlemi |
| `invoice_earsiv.py` | GİB e-Arşiv fatura |
| `email_sender.py` | SMTP e-posta gönderimi |
| `drip_campaign.py` | Otomatik e-posta kampanyası |
| `storage.py` | MinIO (S3) dosya yükleme |
| `gsc.py` | Google Search Console API |
| `push_notification.py` | PWA push bildirimleri (VAPID) |
| `live_analytics.py` | Gerçek zamanlı analitik |

### 2.8 Arka Plan İşleri

Harici zamanlayıcı yok (APScheduler, cron yok). Daemon thread'ler kullanılır:

1. **Drip Campaign Loop** — Her 1 saatte çalışır, 50 lead işler
2. **Kurum Kota Sıfırlama** — Başlangıçta kontrol eder
3. **E-posta gönderimi** — `threading.Thread` ile asenkron
4. **PDF Cache** — 2 dakikalık TTL ile bellek içi cache

---

## 3. Veritabanı Yapısı

### 3.1 Genel Bilgiler

| Özellik | Değer |
|---------|-------|
| Veritabanı | SQLite (dev) / PostgreSQL (prod) |
| ORM | SQLModel (SQLAlchemy + Pydantic) |
| Migrasyon | Alembic (8 versiyon) + otomatik ALTER TABLE |
| Toplam Tablo | 27 (24 model + 3 token tablosu) |
| Toplam Sütun | ~230+ |
| Foreign Key | 20+ ilişki |
| Index | 50+ indekslenmiş sütun |

### 3.2 Tablolar ve İlişkiler

#### `user` — Kullanıcı Hesapları
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| email | str (UNIQUE, INDEX) | Kullanıcı e-postası |
| hashed_password | str | bcrypt ile hashlenmiş |
| full_name | str | Varsayılan: "" |
| email_verified_at | datetime | Doğrulama zamanı |
| plan | str | "free", "pro" |
| extra_credits | int | Ek kredi (tek seferlik analizler) |
| phone | str | Opsiyonel |
| country | str | Opsiyonel |
| created_at | datetime | Kayıt zamanı |
| is_banned | bool | Yasaklı kullanıcı |
| last_login_at | datetime | Son giriş |
| account_claimed_at | datetime | Hesap talep zamanı |

**İlişkiler:**
- `AnalysisRecord.user_id` → `user.id` (bir-çok)
- `AnalysisJob.user_id` → `user.id` (bir-çok)
- `InstitutionMembership.user_id` → `user.id` (çok-çok)
- `EnterpriseCase.uploaded_by_user_id` → `user.id`
- `EnterpriseCase.reviewed_by_user_id` → `user.id`
- `ReportVerification.user_id` → `user.id`
- `PushSubscription.user_id` → `user.id`
- `ReferralCode.user_id` → `user.id`

#### `analysisrecord` — Analiz Sonuçları
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| user_id | int (FK → user.id, INDEX) | Kullanıcı |
| input_text | str | Giriş metni (lab verileri) |
| result_text | str | AI üretimi rapor |
| source | str | "text", "pdf", "image" |
| doctor_notes | str | Doktor notları |
| created_at | datetime | Oluşturulma zamanı |
| original_filename | str | Orijinal dosya adı |
| original_stored_path | str | Saklanan dosya yolu |
| is_favorite | bool | Favori işareti |
| plan_type | str (INDEX) | "free", "single", "monthly", "yearly", "pro", "enterprise" |
| institution_id | int (FK → institutions.id, INDEX) | Kurum (opsiyonel) |

#### `analysis_jobs` — Asenkron Analiz Kuyruğu
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| user_id | int (FK → user.id) | Kullanıcı |
| analysis_record_id | int (INDEX) | Bağlı analiz kaydı |
| status | str | "pending", "processing", "done", "failed" |
| duration_ms | int | İşlem süresi (ms) |
| prompt_tokens | int | OpenAI prompt token sayısı |
| completion_tokens | int | OpenAI completion token sayısı |
| error_message | str | Hata mesajı |
| created_at | datetime | Oluşturulma |
| updated_at | datetime | Güncelleme |

#### `paymentorder` — Ödeme Siparişleri
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| merchant_oid | str (UNIQUE, INDEX) | Sipariş numarası (norya + uuid) |
| user_id | int | Kullanıcı |
| customer_email | str (INDEX) | Müşteri e-postası |
| product | str | "single", "monthly", "yearly" |
| amount_kurus | int | Tutar (EUR cent) |
| quantity | int | Adet |
| currency | str | "EUR" |
| status | str | "pending", "completed", "failed" |
| paytr_transaction_id | str (INDEX) | PayTR işlem ID |
| is_processed | bool | Webhook işlendi mi |
| processed_at | datetime | İşlem zamanı |
| coupon_code_used | str | Kullanılan kupon |
| created_at | datetime | Oluşturulma |
| paid_at | datetime | Ödeme onay zamanı |
| paytr_status | str | PayTR durum kodu |
| raw_callback_json | str | Ham webhook verisi |
| invoice_ettn | str (INDEX) | GİB e-Fatura ETTN |
| invoice_gib_no | str | GİB belge numarası |
| refunded_at | datetime | İade zamanı |
| refund_amount_kurus | int | İade tutarı |
| admin_note | str | Admin notu |

#### `institutions` — Kurumsal Kurumlar
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| name | str (INDEX) | Kurum adı |
| type | str | "hospital", "clinic", "lab", "network" |
| status | str | "pilot", "active", "suspended" |
| plan | str | "enterprise", "pro", "custom" |
| seat_limit | int | Kullanıcı limiti (varsayılan: 25) |
| monthly_quota | int | Aylık rapor limiti (varsayılan: 100) |
| quota_used_this_month | int | Bu ay kullanılan |
| quota_reset_day | int | Kota sıfırlama günü (1-28) |
| active_languages | str | Aktif diller "tr,en" |
| is_active | bool | Aktif mi |
| contract_start | datetime | Sözleşme başlangıcı |
| contract_end | datetime | Sözleşme bitişi |
| contact_email | str | İletişim e-postası |
| contact_phone | str | İletişim telefonu |
| notes | str | Notlar |
| onboarding_completed | bool | Onboarding tamamlandı mı |
| created_at | datetime | Oluşturulma |
| updated_at | datetime | Güncelleme |

#### `institution_memberships` — Kurum Üyelikleri
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| institution_id | int (FK → institutions.id) | Kurum |
| user_id | int (FK → user.id) | Kullanıcı |
| role | str | "owner", "admin", "reviewer", "staff", "member", "readonly" |
| invited_by | int | Davet eden kullanıcı |
| invited_at | datetime | Davet zamanı |
| accepted_at | datetime | Kabul zamanı |
| is_active | bool | Aktif mi |
| created_at | datetime | Oluşturulma |

#### `enterprise_cases` — Kurumsal Vakalar (Yüklenen Raporlar)
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| institution_id | int (FK → institutions.id) | Kurum |
| uploaded_by_user_id | int (FK → user.id) | Yükleyen kullanıcı |
| source_filename | str | Dosya adı |
| source_type | str | "pdf", "image", "text" |
| stored_path | str | Saklama yolu |
| input_text | str | Çıkarılmış metin |
| status | str (INDEX) | "new", "processing", "needs_review", "approved", "rejected", "archived" |
| reviewed_by_user_id | int (FK → user.id) | İnceleyen kullanıcı |
| reviewed_at | datetime | İnceleme zamanı |
| review_notes | str | İnceleme notları |
| analysis_record_id | int (FK → analysisrecord.id) | Bağlı analiz |
| created_at | datetime | Oluşturulma |
| updated_at | datetime | Güncelleme |

#### `enterprise_reports` — Kurumsal Raporlar
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| case_id | int (FK → enterprise_cases.id) | Vaka |
| language | str | Rapor dili |
| report_text | str | Rapor içeriği |
| approval_status | str | "pending", "approved", "rejected" |
| export_status | str | "none", "exported" |
| created_at | datetime | Oluşturulma |

#### `enterprise_subscriptions` — Kurumsal Abonelikler
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| institution_id | int (FK → institutions.id) | Kurum |
| plan_name | str | Plan adı |
| billing_status | str | "active", "trial", "cancelled", "past_due" |
| start_date | datetime | Başlangıç |
| end_date | datetime | Bitiş |
| quota_limit | int | Kota limiti |
| seat_limit | int | Koltuk limiti |
| notes | str | Notlar |
| created_at | datetime | Oluşturulma |

#### `discountcode` — Kuponlar ve Kampanyalar
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| code | str (UNIQUE, INDEX) | Kupon kodu |
| discount_type | str | "percent", "fixed" |
| discount_value | int | İndirim değeri |
| valid_from | date | Başlangıç tarihi |
| valid_until | date | Bitiş tarihi |
| valid_days_of_month | str | Geçerli günler |
| max_uses | int | Maksimum kullanım |
| use_count | int | Kullanım sayısı |
| products | str | Uygulanabilir ürünler |
| is_active | bool | Aktif mi |
| auto_show_on_checkout | bool | Checkout'ta gösterilsin mi |
| auto_apply | bool | Otomatik uygulansın mı |
| campaign_badge | str | Kampanya rozeti metni |
| old/new_price_*_cents | int | Eski/yeni fiyatlar (her plan için) |

#### `pricingplan` — Fiyat Planları
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| code | str (UNIQUE, INDEX) | Plan kodu (single_13eur, monthly_50eur, yearly_99eur) |
| product | str | "single", "monthly", "yearly" |
| price_cents | int | Fiyat (cent) |
| display_order | int | Gösterim sırası |

#### `blog_posts` — Blog Yazıları
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| slug | str (UNIQUE, INDEX) | URL slug |
| lang | str (INDEX) | Dil kodu |
| title | str | Başlık |
| meta_title | str | SEO başlığı |
| meta_description | str | SEO açıklaması |
| content_json | str | JSON içerik |
| cover_image | str | Kapak görseli |
| category | str (INDEX) | Kategori |
| tags_json | str | Etiketler |
| author_name | str | Yazar |
| published_at | datetime (INDEX) | Yayınlanma zamanı |
| is_published | bool (INDEX) | Yayında mı |
| is_featured | bool | Öne çıkan mı |
| reading_time_minutes | int | Okuma süresi |
| created_at | datetime (INDEX) | Oluşturulma |

#### `auditlog` — Denetim Kayıtları
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| event | str (INDEX) | Olay türü (login, register, analyze, payment, vb.) |
| user_id | int (INDEX) | Kullanıcı |
| ip | str | IP adresi |
| country | str | Ülke |
| city | str | Şehir |
| institution_id | int (INDEX) | Kurum |
| entity_type | str | Varlık türü |
| entity_id | int | Varlık ID |
| metadata_json | str | Ek meta veriler |
| created_at | datetime | Oluşturulma |

#### `securitylog` — Güvenlik Logları
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| event | str (INDEX) | Olay türü |
| user_id | int (INDEX) | Kullanıcı |
| ip | str | IP adresi |
| endpoint | str | Endpoint |
| detail | str | Detay |
| created_at | datetime | Oluşturulma |

#### `presence` — Canlı Kullanıcı Varlığı
| Sütun | Tip | Açıklama |
|-------|-----|----------|
| id | int (PK) | Otomatik artan |
| user_id | int (UNIQUE, INDEX) | Kullanıcı |
| last_seen_at | datetime | Son görülme |
| ip | str | IP adresi |
| country | str | Ülke |
| current_page | str | Mevcut sayfa |

#### Diğer Tablolar

| Tablo | Açıklama |
|-------|----------|
| `email_leads` | E-posta lead toplama + drip campaign takibi |
| `drip_email_logs` | Drip e-posta gönderim logları |
| `enterprise_leads` | Kurumsal demo talep formları |
| `referral_codes` | Kullanıcı referans kodları |
| `referral_usages` | Referans kullanım takibi |
| `report_verification` | QR tabanlı rapor doğrulama |
| `push_subscriptions` | PWA Web Push abonelikleri |
| `userregistration` | E-posta doğrulama kayıt takibi |
| `emailverifytoken` | E-posta doğrulama token'ları |
| `passwordresettoken` | Şifre sıfırlama token'ları |
| `sharetoken` | Analiz paylaşım token'ları |
| `guestlogintoken` | Tek kullanımlık misafir giriş token'ları |
| `error_logs` | Global hata takibi |
| `upload_logs` | Dosya yükleme logları |

### 3.3 İlişki Diyagramı (ER)

```
user (1) ────< analysisrecord
user (1) ────< analysis_jobs
user (1) ────< institution_memberships >──── (1) institutions
user (1) ────< enterprise_cases (uploaded_by / reviewed_by)
user (1) ────< report_verification
user (1) ────< referral_codes
user (1) ────< referral_usages (referrer ve referred olarak)
user (1) ────< push_subscriptions
user (1) ────< guest_login_token

institutions (1) ────< institution_memberships
institutions (1) ────< institution_invites
institutions (1) ────< enterprise_cases
institutions (1) ────< enterprise_subscriptions
institutions (1) ────< analysisrecord

analysisrecord (1) ────< sharetoken
analysisrecord (1) ────< report_verification (unique)
analysisrecord (1) ────< enterprise_cases

enterprise_cases (1) ────< enterprise_reports

referral_codes (1) ────< referral_usages
```
