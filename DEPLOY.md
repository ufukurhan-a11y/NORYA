# Norya — Yayına Hazırlık (Production Checklist)

Bu dosya canlıya (production) geçmeden önce kontrol edilmesi gerekenleri listeler.

## Zorunlu (.env)

| Değişken | Açıklama | Production |
|----------|----------|------------|
| `ENVIRONMENT` | `production` yapın | `production` |
| `SECRET_KEY` | JWT ve oturum için güçlü key (`openssl rand -hex 32`) | Varsayılanı **değiştirin**; yoksa uygulama başlamaz |
| `OPENAI_API_KEY` | Analiz için OpenAI anahtarı | Tanımlı olmalı; yoksa uygulama başlamaz |
| `DATABASE_URL` | SQLite yerine PostgreSQL önerilir | `postgresql://...` (isteğe bağlı; SQLite da çalışır) |
| `FRONTEND_URL` | Şifre sıfırlama / e-posta linklerinin temel adresi | `https://alandiniz.com` |
| `CORS_ORIGINS` | İzin verilen origin’ler | `https://alandiniz.com,https://www.alandiniz.com` |

## Ödeme (PayTR)

| Değişken | Açıklama | Production |
|----------|----------|------------|
| `PAYTR_MERCHANT_ID` / `KEY` / `SALT` | PayTR panelinden | Doldurun |
| `PAYTR_NOTIFICATION_URL` | Webhook adresi | `https://alandiniz.com/api/payment/callback` |
| `PAYTR_OK_URL` / `PAYTR_FAIL_URL` | Ödeme sonrası yönlendirme | `https://alandiniz.com/#payment-ok` vb. |
| `PAYTR_TEST_MODE` | Test modu | `0` (canlı ödeme için) |

## E-posta (şifre sıfırlama)

| Değişken | Açıklama | Production |
|----------|----------|------------|
| `SMTP_HOST`, `SMTP_USER`, `SMTP_PASSWORD` | SMTP sunucusu | Doldurun; yoksa şifre sıfırlama maili gitmez |
| `SMTP_FROM` | Gönderen adres | `noreply@alandiniz.com` |

## Güvenlik (otomatik)

- **Production’da** (`ENVIRONMENT=production`): HSTS, CSP, X-Frame-Options, X-Content-Type-Options eklenir.
- **Rate limit**: `RATE_LIMIT_PER_MINUTE` (varsayılan 60). Gerekirse artırın.
- **500 hatalar**: Stack trace kullanıcıya dönmez; sadece log ve ErrorLog tablosuna yazılır.
- **Debug endpoint**: `/debug/rate-test` sadece development’ta açık.

## Sunucu / Hosting

1. **HTTPS** zorunlu (PayTR ve tarayıcı güvenliği için).
2. **Çalıştırma**: `gunicorn` ile örnek:  
   `gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000`
3. **Reverse proxy**: Nginx/Caddy ile SSL sonlandırma ve `X-Forwarded-For` / `X-Forwarded-Proto` iletin.
4. **Veritabanı**: SQLite tek sunucu için yeterli; yük artarsa PostgreSQL’e geçin.
5. **Yüklenen dosyalar**: `data/uploads/` dizini kalıcı olmalı (volume/persistent disk).

## Kontrol listesi (kısa)

- [ ] `ENVIRONMENT=production`
- [ ] `SECRET_KEY` değiştirildi (varsayılan değil)
- [ ] `OPENAI_API_KEY` tanımlı
- [ ] `FRONTEND_URL` ve `CORS_ORIGINS` alan adınıza göre
- [ ] PayTR: URL’ler ve test modu kapalı (isteğe bağlı)
- [ ] SMTP ayarlı (şifre sıfırlama için)
- [ ] HTTPS ve reverse proxy
- [ ] `data/uploads` kalıcı
- [ ] İsteğe bağlı: `GA_MEASUREMENT_ID=G-XXX` (Google Analytics 4); Cloudflare/DNS: `docs/CLOUDFLARE-VE-GOOGLE-ANALYTICS.md`

Bu adımlar tamamsa uygulama yayına hazırdır.
