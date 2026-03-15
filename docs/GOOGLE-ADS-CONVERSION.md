# Google Ads "Satın alma işlemi" dönüşümü – yapılandırma ve test

## Dönüşüm kodunun bulunduğu dosyalar

| Dosya | Açıklama |
|-------|----------|
| `app/main.py` | `/payment/success` sayfası HTML’i, `conversion_send_to` değeri, `gtag("event", "conversion", ...)` tetiklemesi (sadece `status=paid` veya `is_premium_active` olduğunda) |
| `app/core/config.py` | `google_ads_conversion_id` (AW-…), `google_ads_conversion_label` (dönüşüm etiketi) |
| `app/main.py` (middleware) | `/payment/success` için CSP: `_CSP_PAYMENT_SUCCESS` (Google tag / conversion isteklerine izin verir) |

## Conversion ID ve label

- **Conversion ID:** `AW-18004536281` (config: `google_ads_conversion_id`, env: `GOOGLE_ADS_CONVERSION_ID`)
- **Conversion label:** Varsayılan `RF4SCL78oIYcENnXnYlD`. Google Ads’teki "Satın alma işlemi" dönüşümünün **etiket değeri** ile birebir aynı olmalı. (config: `google_ads_conversion_label`, env: `GOOGLE_ADS_CONVERSION_LABEL`)

`send_to` formatı: `AW-18004536281/RF4SCL78oIYcENnXnYlD` (ID/label aynı ise değiştirmeyin).

## Tetiklenme koşulu

Dönüşüm **yalnızca** şu durumda tetiklenir:

1. Kullanıcı **`/payment/success?merchant_oid=...`** sayfasındadır (PayTR başarı yönlendirmesi).
2. Sayfa **`/api/orders/status?merchant_oid=...`** ile polling yapar.
3. API yanıtında **`status === "paid"`** gelir (ödeme backend'de tamamlandıktan sonra).

Yani dönüşüm sadece **başarılı ödeme sonrası teşekkür sayfasında**, sipariş “paid” olduktan sonra Conversion yalnızca status=paid ile tetiklenir (is_premium_active tek başına tetiklemez).

## Test için kontrol listesi

### 1. Hangi sayfada test edeceğim?

- **Sayfa:** `https://<siteniz>/payment/success?merchant_oid=<gerçek_veya_test_oid>`
- **Test siparişi:** `merchant_oid=test123` → Gerçek sipariş kaydı yoksa API hemen `status: "paid"` döner, conversion tetiklenir.

### 2. Sayfada neyi kontrol etmeliyim?

1. **Tarayıcı konsolu (F12 → Console):**
   - `[Norya payment success] polling will start in 500ms (gtag load grace); send_to=AW-18004536281/RF4SCL78oIYcENnXnYlD`
   - Ödeme “paid” olduğunda: `[Norya] Google Ads conversion fired` veya `[Norya] Google Ads conversion queued (gtag not ready)` (ikisi de başarılı)
   - Dönüşüm atlanırsa: `[Norya] Google Ads conversion skipped` (reason: already_fired / noryaConversionFired_set)
   - **Tetiklenmediği durumlar:** `[Norya] Google Ads conversion NOT fired: payment status=failed` (sadece paid tetikler), `... NOT fired: timeout before paid`, `... NOT fired: invalid or missing merchant_oid`

2. **Debug nesnesi:** Konsolda `window.__noryaPaymentDebug`:
   - `conversionTriggered: true` → conversion tetiklendi
   - `send_to: "AW-18004536281/..."` → kullanılan send_to değeri
   - `condition: "status=paid_only"` (tetiklendiyse; conversion sadece status=paid ile tetiklenir)
   - `conversionNotFiredReason: "status_failed" | "timeout" | "invalid_merchant_oid" | "status_not_paid"` (tetiklenmediyse sebep)
   - `value`, `currency`, `transaction_id` (tetiklendiyse gönderilen değerler)

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

---

## test123 ile hızlı doğrulama

**URL:** `https://<siteniz>/payment/success?merchant_oid=test123&lang=tr`

**İlk yüklemede "fired" görmek için:**  
- **Benzersiz test OID:** `merchant_oid=test123_1` veya `test123_` + timestamp (örn. `test123_1734567890`). Backend aynı test yanıtını döner; her farklı OID için `sessionStorage` anahtarı farklı olduğundan her açılışta conversion tetiklenir.  
- **Veya** aynı OID ile: URL'ye **`&conv_reset=1`** ekleyip yenile (`...?merchant_oid=test123&lang=tr&conv_reset=1`); sessionStorage temizlenir, bu yüklemede conversion yeniden tetiklenir.

### Konsolda görmen gereken log (sırayla)

1. `[Norya payment success] orderId=test123, guest_token=no, verify_tag=false`
2. `[Norya payment success] polling will start in 500ms (gtag load grace); send_to=AW-18004536281/RF4SCL78oIYcENnXnYlD`
3. `[Norya payment success] polling request started` (orderId: "test123")
4. `[Norya payment success] payment status=paid`
5. **Sırayla:** `[Norya] conversion event dispatch start` → `[Norya] conversion event dispatch attempted (gtag)` → `[Norya] already_fired set to true` → `[Norya] Google Ads conversion FIRED — event sent to Google Ads.` (objede: `send_to`, `transaction_id`, `value`, `currency`). Son satır: "Network: conversion request URL pattern — ..."

(Alternatif: gtag henüz yüklenmediyse **conversion event dispatch attempted (dataLayer push)** ve **Google Ads conversion QUEUED** görünür; event dataLayer'a push edilir, gtag yüklenince gönderilir.)

**SKIPPED görürsen:** "already sent in this session" — `sessionStorage` anahtarı `norya_conv_test123` önceki bir yüklemede set edilmiş. URL'ye `&conv_reset=1` ekleyip yenile veya gizli pencere kullan.

### Network’te beklenen istekler

**1. Orders status (polling)**  
- **URL:** `GET <api_base>/api/orders/status?merchant_oid=<oid>` (örn. `http://127.0.0.1:8000/api/orders/status?merchant_oid=test123`)  
- Konsol: `[Norya] orders status request sent` (url ile); `[Norya] orders status response received` (status ile); `[Norya] orders status response body` (status, merchant_oid).

**2. Google Ads conversion**  
- **URL pattern:** `*googleadservices.com/pagead/conversion*` veya `*doubleclick.net/pagead/conversion*`  
- **Beklenen:** `https://www.googleadservices.com/pagead/conversion/...` veya `https://googleads.g.doubleclick.net/pagead/conversion/...` — **Method: GET**, **Status: 200** (veya 204). Query string’de `awid=18004536281` ve label/conv parametreleri görünür.  
- **Zamanlama:** `conversion event dispatch attempted` log’undan 1–2 saniye sonra listelenir.

---

## Google Ads arayüzünde etiket doğrulama

1. **Google Ads** → **Araçlar ve Ayarlar** (üst sağ) → **Ölçüm** → **Dönüşümler**.
2. Listede **“Satın alma işlemi”** (veya bu dönüşümü verdiğin isim) dönüşümünü bul.
3. **Durum** sütununda **“Etkin”** ve **Kaynak** sütununda **“Web sitesi”** olmalı.
4. Dönüşümü tıkla → **Etiket kurulumu** bölümünde **“Google tag (gtag.js) kullanıyorum”** ve `send_to: AW-18004536281/RF4SCL78oIYcENnXnYlD` ile uyumlu olduğunu kontrol et.
5. **Son 30 gün** veya **Son 7 gün** döneminde **Dönüşüm sayısı** artıyorsa etiket çalışıyor demektir. Test için test123 ile bir kez tetikleyip 24–48 saat sonra bu sayıda +1 görebilirsin (bazen gecikmeli görünür).
6. **Tag Assistant (Chrome eklentisi):** `/payment/success?merchant_oid=test123` sayfasında tag’i açıp conversion tetiklendikten sonra **“Bu etiket tarafından gönderilen isabetler”** altında **conversion** isabeti görünmeli.
