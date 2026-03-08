# PayTR "Geçersiz istek" Hatası

Ödeme sayfasında PayTR’ye yönlendirildikten sonra **"Üzgünüz – Geçersiz istek, lütfen gönderilen değerleri kontrol edin"** görüyorsanız aşağıdakileri kontrol edin.

## 1. Detaylı hata mesajını açın

PayTR, `debug_on=1` gönderildiğinde hangi alanın hatalı olduğunu döndürür.

- `.env` içine ekleyin:
  ```env
  PAYTR_DEBUG_ON=1
  ```
- Uygulamayı yeniden başlatıp ödemeyi tekrar deneyin.
- Hata artık Norya tarafında (veya PayTR’nin döndürdüğü mesajda) daha net görünecektir; örn. "Zorunlu alan degeri gecersiz: merchant_id".
- Test bitince güvenlik için `PAYTR_DEBUG_ON=0` yapın veya satırı kaldırın.

## 2. Mağaza bilgileri (BİLGİ sayfası)

PayTR panel → **BİLGİ** sayfasındaki değerlerle `.env` aynı olmalı:

- `PAYTR_MERCHANT_ID` = Mağaza numarası
- `PAYTR_MERCHANT_KEY` = Parola
- `PAYTR_MERCHANT_SALT` = Gizli anahtar

Boşluk, fazladan karakter veya yanlış kopyalama hash hatasına yol açar.

## 3. Para birimi ve tutar

- **EUR kullanıyorsanız:** PayTR mağaza ayarlarında **EUR** hesabı açık olmalı. Açık değilse TL’ye çevirip gönderin:
  - `PAYTR_EUR_TO_TRY_RATE=35` (veya güncel kur) verin; uygulama tutarı TL (kuruş) olarak PayTR’ye gönderir.
- **payment_amount:** PayTR’ye **tam sayı** (kuruş/cent) gidiyor; örn. 14,04 € → 1404. Kod bunu otomatik yapıyor; ekstra bölme/çarpma yapmayın.

## 4. Bildirim / OK / Fail URL’leri

- **Bildirim URL:** PayTR panelde tanımlı **Bildirim URL** ile `.env` içindeki `PAYTR_NOTIFICATION_URL` birebir aynı olmalı (https, sonunda slash olup olmaması dahil).
- **merchant_ok_url / merchant_fail_url:** Müşterinin yönlendirileceği adresler. Canlı ortamda **https** olmalı; PayTR panelde izin verilen alan adlarına uygun olmalı.

## 5. IP (local test)

PayTR dokümanı: **Sunucuda değil kendi bilgisayarınızda** deniyorsanız, PayTR’ye giden istekte **dış IP** kullanılmalı. Sunucuda çalıştırırken bu sorun genelde olmaz. Local’de "geçersiz paytr_token" benzeri hata alırsanız, geçici olarak testi sunucuda yapın veya PayTR’nin IP ile ilgili kısıtlarını kontrol edin.

## 6. Hash ve parametre sırası

Entegrasyon, PayTR iFrame API 1. adım dokümanındaki sırayla uyumludur:

- Hash metni: `merchant_id + user_ip + merchant_oid + email + payment_amount + user_basket + no_installment + max_installment + currency + test_mode`
- Sonra: `HMAC-SHA256(merchant_key, hash_str + merchant_salt)` → Base64 = `paytr_token`

`user_basket`: Base64(JSON([[ "Ürün adı", "fiyat (örn. 13.00)", adet ], ...])). Fiyat string, iki ondalıklı.

## 7. Test / canlı mod

- Panelde mağaza **test** modundaysa `PAYTR_TEST_MODE=1`, **canlı** moddaysa `PAYTR_TEST_MODE=0` kullanın. Mod uyumsuzluğu bazen "Geçersiz istek" veya işlemin reddedilmesine neden olur.

## Özet kontrol listesi

| Kontrol | Açıklama |
|--------|----------|
| `PAYTR_DEBUG_ON=1` | Detaylı hata için (test sonrası 0 yapın) |
| merchant_id / key / salt | Panel BİLGİ ile birebir aynı |
| Para birimi | EUR kullanılıyorsa mağazada EUR açık; değilse TL + kur |
| Bildirim URL | Panel ile .env aynı |
| OK/Fail URL | https, panel ayarlarına uygun |
| test_mode | Panel modu ile .env uyumlu |

Bu adımlardan sonra hata devam ederse, `PAYTR_DEBUG_ON=1` ile alınan **tam hata metnini** (PayTR’nin döndürdüğü `reason`) PayTR destek veya teknik dokümanla eşleştirerek ilgili alanı düzeltebilirsiniz.
