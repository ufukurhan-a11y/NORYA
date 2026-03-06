# Canonical adres www.noryaai.com ise (noryaai.com → www yönlendirdiyseniz)

Cloudflare’da **noryaai.com** adresini **www.noryaai.com**’a yönlendirdiyseniz, kullanıcılar her zaman www ile açılır. Sorun çıkmaması için Render’daki ortam değişkenlerini www’ye göre güncelleyin.

## Render (Environment) ayarları

| Değişken | Önerilen değer (canonical www ise) |
|----------|-------------------------------------|
| `FRONTEND_URL` | `https://www.noryaai.com` |
| `CORS_ORIGINS` | `https://www.noryaai.com,https://noryaai.com` |
| `PAYTR_OK_URL` | `https://www.noryaai.com/payment/success` (veya `...#payment-ok`) |
| `PAYTR_FAIL_URL` | `https://www.noryaai.com/#pricing` (veya `.../payment/failed`) |
| `PAYTR_NOTIFICATION_URL` | `https://www.noryaai.com/paytr/callback` |

**Not:** Bildirim URL (callback) PayTR’nin sizin sunucunuza POST atacağı adres. Render’a gelen istekler genelde noryaai.com veya www ile gelir; Render her iki host’u da kabul eder. Yine de panelde ve env’de **www** kullanmak tutarlı olur.

## PayTR panel

- **Bildirim URL:** `https://www.noryaai.com/paytr/callback`
- **Başarı / Hata URL’leri:** www ile girin (yukarıdaki gibi).

## Özet

- **CORS:** `https://www.noryaai.com` mutlaka listede olsun (noryaai.com da kalabilir).
- **FRONTEND_URL:** E-postalardaki linkler (şifre sıfırlama vb.) doğrudan www’ye gitsin diye `https://www.noryaai.com` yapın.
- Bu ayarlardan sonra canonical www ile sorun yaşamazsınız.
