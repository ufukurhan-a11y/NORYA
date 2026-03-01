# E-posta doğrulama (kayıt sonrası) — Gerçek müşteri

Kayıt olan kullanıcıya otomatik bir **e-posta doğrulama linki** gider. Müşteri bu linke tıklayınca hesabı “doğrulanmış” olur. Bu sayede geçerli e-posta adresi kullanıldığından emin olursunuz.

---

## Akış (zaten kodda var)

1. **Kayıt:** Kullanıcı e-posta, şifre, ad, telefon, ülke ile kayıt olur.
2. **Backend:** Kullanıcı oluşturulur, 24 saat geçerli bir doğrulama token’ı üretilir ve **e-posta gönderilir** (SMTP ayarlıysa).
3. **E-posta:** Müşteri “E-posta adresinizi doğrulayın” konulu maili alır; içinde **Doğrula** butonu/linki vardır. Link: `https://siteniz.com/?verify-email=TOKEN`
4. **Tıklama:** Müşteri linke tıklar → site açılır → sayfa yüklenirken `?verify-email=TOKEN` API’ye iletilir → hesap doğrulanır (`email_verified_at` set edilir).
5. **Sonuç:** Toast ile “E-posta adresiniz doğrulandı.” mesajı gösterilir.

SMTP ayarlı değilse kayıt yine başarılı olur ama **e-posta gitmez**; log’da “SMTP not configured” uyarısı görünür.

---

## Gerçek müşteri için: SMTP ayarları

E-postanın gerçekten gitmesi için **SMTP** tanımlanmalı.

### 1. Yerel (.env)

`.env` dosyasına ekleyin (Gmail, Yandex, SendGrid, Mailgun vb. kullanabilirsiniz):

```env
# E-posta (kayıt doğrulama + şifre sıfırlama)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_FROM=noreply@noryaai.com
SMTP_FROM_NAME=Norya
SMTP_USE_TLS=1

# Doğrulama linkinin açılacağı adres (canlı domain)
FRONTEND_URL=https://noryaai.com
```

- **Gmail:** Uygulama şifresi kullanın (normal şifre değil). Hesap → Güvenlik → 2 adımlı doğrulama → Uygulama şifreleri.
- **FRONTEND_URL:** Canlı sitede mutlaka `https://noryaai.com` (veya kendi domain’iniz) olmalı; yoksa e-postadaki link yanlış sayfaya gider.

### 2. Render (canlı sunucu)

Render Dashboard → **norya** servisi → **Environment**:

| Key           | Value (örnek)                    |
|---------------|-----------------------------------|
| `SMTP_HOST`   | `smtp.gmail.com` (veya kullandığınız SMTP) |
| `SMTP_PORT`   | `587`                             |
| `SMTP_USER`   | Gönderen e-posta                  |
| `SMTP_PASSWORD` | SMTP / uygulama şifresi         |
| `SMTP_FROM`   | `noreply@noryaai.com`             |
| `SMTP_FROM_NAME` | `Norya`                        |
| `SMTP_USE_TLS` | `1`                             |
| `FRONTEND_URL` | `https://noryaai.com`            |

Kaydedip **Manual Deploy** (veya bir commit push) ile yeniden deploy edin.

---

## Test

1. SMTP ve `FRONTEND_URL` doğru ayarlayın.
2. Siteden yeni bir e-posta ile kayıt olun.
3. Gelen kutusunu (ve gerekiyorsa **spam** klasörünü) kontrol edin; “Norya — E-posta adresinizi doğrulayın” maili gelmeli.
4. Maildeki **Doğrula** linkine tıklayın → site açılmalı ve “E-posta adresiniz doğrulandı.” toast’ı çıkmalı.

E-posta gelmiyorsa:

- Render **Logs**’ta “SMTP not configured” veya “Failed to send email” var mı bakın.
- Gmail kullanıyorsanız “Daha az güvenli uygulama” kapalı olmalı; bunun yerine **Uygulama şifresi** kullanın.

---

## İsteğe bağlı: Girişi doğrulamaya bağlama

Şu an kullanıcı **e-postayı doğrulamadan da** giriş yapıp siteyi kullanabiliyor. Sadece “doğrulanmış mı?” bilgisi tutuluyor.

İleride “önce doğrula, sonra giriş” isterseniz:

- `app/api/auth.py` içinde **login** endpoint’inde `user.email_verified_at` kontrolü eklenir.
- `email_verified_at` boşsa `403` veya `401` dönüp mesajda “Lütfen e-posta adresinizi doğrulayın. Size gönderilen linke tıklayın.” denir.
- Frontend’de bu durumda kullanıcıya aynı mesaj gösterilir.

Bu zorunlu doğrulama şu an kodda **yok**; sadece e-posta gönderimi ve link ile doğrulama akışı vardır.

---

## Özet

| Ne yapılır? | Nerede? |
|-------------|--------|
| SMTP bilgilerini girmek | `.env` (yerel) ve Render **Environment** (canlı) |
| Doğrulama linkinin doğru siteye gitmesi | `FRONTEND_URL=https://noryaai.com` (canlıda mutlaka https ve doğru domain) |
| E-postanın gitmesi | SMTP ayarları dolu olunca otomatik (kayıt sırasında) |
| Müşteri ne yapar? | Kayıt olur → maili açar → “Doğrula” linkine tıklar → hesap doğrulanır |

Mevcut kod bu akışı destekliyor; gerçek müşteri için sadece **SMTP + FRONTEND_URL** ayarlarını canlıda doğru yapmanız yeterli.
