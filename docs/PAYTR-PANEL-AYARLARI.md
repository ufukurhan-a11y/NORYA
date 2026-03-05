# PayTR Panel Ayarları (noryaai.com)

PayTR Üye İşyeri Paneli’nde aşağıdaki adresleri mutlaka girin.

## 1. Bildirim (Callback) URL

Ödeme onaylandığında veya iptal edildiğinde PayTR bu adrese **POST** isteği gönderir. Norya bu istekle siparişi “ödendi” yapar ve kullanıcıya hak tanır.

| Paneldeki alan | Değer |
|----------------|--------|
| **Bildirim URL** / **Callback URL** | `https://noryaai.com/paytr/callback` |

- Sadece **HTTPS** kabul edilir.
- Adres tam olarak bu olmalı; sondaki `/` eklemeyin.

## 2. Başarılı / Başarısız sayfa (müşteri yönlendirmesi)

Ödeme tamamlanınca veya iptal edilince müşteri tarayıcıda bu sayfalara yönlendirilir. İsterseniz panelde boş bırakıp Norya’nın kendi URL’lerini kullanabilirsiniz; uygulama zaten aşağıdakileri kullanıyor:

| Amaç | Norya’da kullanılan adres |
|------|---------------------------|
| Ödeme başarılı | `https://noryaai.com/payment/success` |
| Ödeme iptal / hata | `https://noryaai.com/payment/failed` |

Panelde “Başarılı ödeme URL” / “Hata URL” gibi alanlar varsa bunları da aynı şekilde doldurabilirsiniz; böylece PayTR’nin yönlendirmesi de bu sayfalara gider.

## 3. Entegrasyon bilgileri

Panelden aldığınız değerleri **Render** (veya kullandığınız host) **Environment** değişkenlerine yazın:

- `PAYTR_MERCHANT_ID`
- `PAYTR_MERCHANT_KEY`
- `PAYTR_MERCHANT_SALT`

Opsiyonel (isteğe göre):

- `PAYTR_OK_URL=https://noryaai.com/payment/success`
- `PAYTR_FAIL_URL=https://noryaai.com/payment/failed`
- `PAYTR_TEST_MODE=1` (test) veya `0` (canlı)

## Özet

1. Panelde **Bildirim URL**: `https://noryaai.com/paytr/callback`
2. Host’ta (Render) `PAYTR_MERCHANT_ID`, `PAYTR_MERCHANT_KEY`, `PAYTR_MERCHANT_SALT` dolu olsun.
3. Deploy sonrası ödeme akışını test edin; loglarda `PAYTR_CALLBACK:` satırlarını kontrol edin.
