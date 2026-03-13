# Google Ads "Satın alma işlemi" dönüşümü – yapılandırma ve test

## Dönüşüm kodunun bulunduğu dosyalar

| Dosya | Açıklama |
|-------|----------|
| `app/main.py` | `/payment/success` sayfası HTML’i, `conversion_send_to` değeri, `gtag("event", "conversion", ...)` tetiklemesi (sadece `status=paid` veya `is_premium_active` olduğunda) |
| `app/core/config.py` | `google_ads_conversion_id` (AW-…), `google_ads_conversion_label` (dönüşüm etiketi) |
| `app/main.py` (middleware) | `/payment/success` için CSP: `_CSP_PAYMENT_SUCCESS` (Google tag / conversion isteklerine izin verir) |

## Conversion ID ve label

- **Conversion ID:** `AW-18004536281` (config: `google_ads_conversion_id`, env: `GOOGLE_ADS_CONVERSION_ID`)
- **Conversion label:** Varsayılan `RF4SCL78oIYcENnXnYID`. Google Ads’teki "Satın alma işlemi" dönüşümünün **etiket değeri** ile birebir aynı olmalı. (config: `google_ads_conversion_label`, env: `GOOGLE_ADS_CONVERSION_LABEL`)

`send_to` formatı: `AW-18004536281/RF4SCL78oIYcENnXnYID` (ID/label aynı ise değiştirmeyin).

## Tetiklenme koşulu

Dönüşüm **yalnızca** şu durumda tetiklenir:

1. Kullanıcı **`/payment/success?merchant_oid=...`** sayfasındadır (PayTR başarı yönlendirmesi).
2. Sayfa **`/api/orders/status?merchant_oid=...`** ile polling yapar.
3. API yanıtında **`status === "paid"`** veya **`is_premium_active === true`** gelir (ödeme backend’de tamamlandıktan sonra).

Yani dönüşüm sadece **başarılı ödeme sonrası teşekkür sayfasında**, sipariş “paid” olduktan sonra **bir kez** tetiklenir.

## Test için kontrol listesi

### 1. Hangi sayfada test edeceğim?

- **Sayfa:** `https://<siteniz>/payment/success?merchant_oid=<gerçek_veya_test_oid>`
- **Test siparişi:** `merchant_oid=test123` → Gerçek sipariş kaydı yoksa API hemen `status: "paid"` döner, conversion tetiklenir.

### 2. Sayfada neyi kontrol etmeliyim?

1. **Tarayıcı konsolu (F12 → Console):**
   - `[Norya payment success] polling will start in 500ms (gtag load grace); send_to=AW-18004536281/RF4SCL78oIYcENnXnYID`
   - Ödeme “paid” olduğunda: `[Norya] Google Ads conversion fired` veya `[Norya] Google Ads conversion queued (gtag not ready)` (ikisi de başarılı)
   - Dönüşüm atlanırsa: `[Norya] Google Ads conversion skipped` (reason: already_fired / noryaConversionFired_set)

2. **Debug nesnesi:** Konsolda `window.__noryaPaymentDebug`:
   - `conversionTriggered: true` → conversion tetiklendi
   - `send_to: "AW-18004536281/..."` → kullanılan send_to değeri
   - `condition: "status=paid_or_premium"`

3. **Tag Assistant (Chrome eklentisi):**
   - `/payment/success` sayfasında Google tag (AW-18004536281) listelenmeli.
   - Conversion tetiklendikten sonra bu etiket için **en az bir isabet (hit)** görünmeli (“Bu etiket tarafından hiçbir isabet gönderilmedi” kaybolmalı).
   - İsabet türü: **conversion** (veya purchase).

### 3. Label’ı Google Ads’te doğrulama

- Google Ads → **Araçlar ve Ayarlar** → **Ölçüm** → **Dönüşümler**.
- “Satın alma işlemi” dönüşümünü aç → **Etiket / Tag kurulumu** veya **snippet** bölümünde `send_to` içindeki **label** (AW-…/’dan sonraki kısım) görünür.
- Bu label, config’teki `google_ads_conversion_label` (veya env `GOOGLE_ADS_CONVERSION_LABEL`) ile **aynı** olmalı. Farklıysa `.env` veya config’te düzeltin.

## Yapılan düzeltmeler (özet)

1. **Conversion label yapılandırılabilir:** `config.google_ads_conversion_label` ve env `GOOGLE_ADS_CONVERSION_LABEL` eklendi; "Satın alma işlemi" etiketi Ads’tekiyle eşleştirilebilir.
2. **Debug logları:** Konsola conversion tetiklenmesi / atlanması ve `send_to` değeri yazılıyor; `__noryaPaymentDebug` ile condition ve durum izlenebilir.
3. **gtag yükleme:** İlk poll 500 ms gecikmeyle başlıyor; gtag.js’in yüklenmesi için kısa süre tanınıyor.
4. **Fallback:** `gtag` henüz tanımlı değilse conversion event’i `dataLayer`’a push ediliyor; gtag.js yüklendiğinde işlenir.
5. **CSP:** `/payment/success` için zaten uygun CSP vardı; değişiklik yapılmadı.

## Hâlâ “Hatalı yapılandırılmış” / “Etkin değil” görünüyorsa

- Google Ads’te bu dönüşümün **durumunun** “Etkin” ve **kaynağının** “Web sitesi” olduğundan emin olun.
- **Etiket** bölümünde gösterilen conversion label’ı kopyalayıp `GOOGLE_ADS_CONVERSION_LABEL` (veya config) ile aynı yapın.
- Tag Assistant’ta **sayfa yükü** “payment/success” ve **ödeme tamamlandıktan sonra** (polling “paid” döndükten sonra) isabetlerin göründüğünü kontrol edin.
- Reklam engelleyici / gizlilik eklentileri conversion isteğini engelliyor olabilir; testi eklentileri kapatarak tekrarlayın.
