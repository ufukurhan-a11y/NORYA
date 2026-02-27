# Norya Admin Panel (Production)

Modüler, Jinja2 + Tailwind ile production admin paneli.

## Giriş

- **URL:** `/admin` → `/admin/dashboard` yönlendirir.
- **Kimlik:** ADMIN_SECRET ile giriş. İlk açılışta `/admin/login` sayfasına düşersiniz; şifreyi girince cookie ile oturum açılır.
- **Eski panel (API tabanlı):** Sidebar’dan “Eski panel (API)” veya doğrudan `/admin/legacy`.

## Klasör yapısı

```
app/
  admin/
    __init__.py          # admin_router, tüm modül router’ları burada toplanır
    deps.py              # require_admin (API), require_admin_cookie (panel), cookie imzalama
    routers/
      dashboard.py       # Dashboard, giriş, legacy link
      users.py           # Kullanıcı listesi, detay, ban/unban
      live.py            # Canlı kullanıcılar (Presence)
      payments.py        # Ödemeler (PayTR)
      errors.py          # Hata logları (ErrorLog)
      uploads.py        # Upload logları (UploadLog)
      queue.py           # Analiz kuyruğu (AnalysisJob)
      security.py        # Güvenlik (SecurityLog)
  templates/
    admin/
      base_admin.html    # Layout, sidebar, Tailwind CDN
      login.html
      dashboard.html
      users_list.html, user_detail.html
      live_list.html
      payments_list.html
      errors_list.html, error_detail.html
      uploads_list.html
      queue_list.html
      security_list.html
  models/
    error_log.py        # error_logs
    upload_log.py       # upload_logs
    analysis_job.py     # analysis_jobs
    security_log.py     # security_logs
```

## Modüller

| Modül | Route | Açıklama |
|-------|--------|----------|
| Dashboard | `/admin/dashboard` | Günlük/aylık satış, toplam/aktif kullanıcı, ortalama analiz süresi, başarısız ödeme, son 10 işlem |
| Kullanıcılar | `/admin/users` | Listeleme, e-posta arama, detay, ban/unban, analiz sayısı, son giriş |
| Canlı | `/admin/live` | Son 2 dk heartbeat atanlar; IP, ülke, sayfa (heartbeat’e `?page=/path` eklenirse) |
| Ödemeler | `/admin/payments` | Başarılı/hatalı/bekleyen, tutar, PayTR tx id. Webhook: `/payment/callback` veya `/api/paytr/webhook` |
| Hata logları | `/admin/errors` | error_logs; global exception handler her yakalanmayan hatayı buraya yazar |
| Upload logları | `/admin/uploads` | upload_logs; dosya adı, boyut, durum, süre |
| Analiz kuyruğu | `/admin/queue` | analysis_jobs; pending/processing/done/failed, süre |
| Güvenlik | `/admin/security` | security_logs; failed_login, rate_limit, suspicious |

## Auth

- **Panel:** Cookie `norya_admin` (HMAC ile imzalı). Eksik/geçersizse `/admin/login`’e yönlendirilir.
- **API (eski panel / script):** `X-Admin-Secret` header veya `?admin_secret=...` query.

## Veritabanı

- Yeni tablolar: `error_logs`, `upload_logs`, `analysis_jobs`, `security_logs`.
- User: `is_banned`, `last_login_at`.
- Presence: `ip`, `country`, `current_page`.
- PaymentOrder: `paytr_transaction_id` (opsiyonel).

`init_db()` bu sütunları ALTER ile eklemeye çalışır; yoksa sessizce atlanır.

## PayTR webhook

- Mevcut: `POST /payment/callback`
- Alias: `POST /api/paytr/webhook` (aynı işlem).

PayTR panelinde bildirim URL olarak ikisi de kullanılabilir.
