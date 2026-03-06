# Ödeme Altyapısı — Uygunluk Özeti

Projeniz **ödeme (PayTR) altyapısı ile uyumlu** ve canlı ödeme almaya uygun şekilde kurgulanmış. Aşağıda ne var, ne eksik ve canlıya geçerken nelere dikkat etmeniz gerektiği özetleniyor.

---

## ✅ Mevcut ve Uygun Olanlar

### 1. PayTR entegrasyonu
- **Token / iFrame:** `/paytr/init`, `/payment/get-token`, `/payment/get-token-guest` ile token alınıp PayTR iFrame gösteriliyor.
- **Bildirim (callback):** `/paytr/callback`, `/payment/callback`, `/api/paytr/webhook` — PayTR’den gelen POST işleniyor.
- **Hash doğrulama:** Callback’te `merchant_oid + merchant_salt + status + total_amount` ile HMAC-SHA256 kontrolü yapılıyor; sahte/yanlış istekler reddediliyor.
- **Idempotent işleme:** Aynı sipariş iki kez işlenmiyor (`is_processed`).
- **Paketler:** Tek analiz, aylık, yıllık ve kupon kodu destekleniyor.
- **Para birimi:** EUR veya TL (paytr_eur_to_try_rate ile) seçeneği var.
- **Test modu:** `PAYTR_TEST_MODE=1` ile test ödemesi yapılabiliyor.

### 2. Veritabanı ve sipariş
- `PaymentOrder`: merchant_oid, user_id, product, amount_kurus, status, paytr_transaction_id, is_processed, paytr_status, paytr_payment_amount, raw_callback_json, e-arşiv fatura alanları mevcut.
- Sipariş durumu: pending → completed / failed; callback ile güncelleniyor.

### 3. Yasal ve tüketici bilgilendirme
- **Mesafeli satış:** PayTR, fiyat, cayma/iade hakkı metinlerde belirtilmiş.
- **Ödeme sayfasında satıcı bilgisi:** E-posta (support@noryaai.com) ve “İletişim sayfası” linki açıkça gösteriliyor (PayTR’nin talebi karşılanmış).
- **İade / iletişim:** İade ve İptal Politikası, İletişim sayfası, KVKK/GDPR ve Kullanım Şartları sayfaları var.

### 4. Admin panel
- Ödemeler listesi (filtre: completed / failed / pending), sipariş detayı, admin notu, e-arşiv fatura kesimi mevcut.

### 5. Müşteri akışı
- Ödeme sayfası → plan seçimi → PayTR iFrame → başarı/hata sayfaları; durum için `/api/orders/status` ile polling yapılıyor.

---

## ⚠️ Canlıya Geçmeden Önce Yapılacaklar

| Konu | Ne yapmalı |
|------|-------------|
| **PayTR panel** | Bildirim URL: `https://noryaai.com/paytr/callback` (veya kullandığınız domain) mutlaka girilmeli. |
| **Ortam değişkenleri** | `PAYTR_MERCHANT_ID`, `PAYTR_MERCHANT_KEY`, `PAYTR_MERCHANT_SALT` host’ta (örn. Render) tanımlı olmalı. |
| **URL’ler** | `PAYTR_OK_URL`, `PAYTR_FAIL_URL`, `PAYTR_NOTIFICATION_URL` canlı domain ile güncellenmeli. |
| **Test modu** | Canlı ödeme için `PAYTR_TEST_MODE=0` yapılmalı. |
| **HTTPS** | Site tamamen HTTPS’te çalışmalı (PayTR ve tarayıcı güvenliği). |

---

## ✅ İade (Refund) Altyapısı

PayTR İade API entegre edildi. Admin panelinden tam veya kısmi iade yapılabilir.

| Ne var? | Açıklama |
|--------|----------|
| **İade politikası** | `/iade-iptal` sayfası, yasal metinler ve “support@noryaai.com ile sipariş no ile iade talebi” metni mevcut. |
| **Admin notu** | Sipariş detayında “Admin notu (iade / açıklama)” alanı var; sadece not için. |
| **Eksik** | PayTR **İade API** entegrasyonu yok. Yani admin panelinden “İade yap” butonu veya API çağrısı **yok**. |

**Şu anki iade süreci:** Müşteri e-posta ile talep ediyor → siz PayTR panelinden veya banka/kart işlemleriyle **manuel** iade yapıyorsunuz. Uygulama içinden otomatik iade tetiklenmiyor.

**İsterseniz eklenebilir:** PayTR’nin İade API’si (`https://www.paytr.com/odeme/iade`) kullanılarak admin panele “Tam iade” / “Kısmi iade” aksiyonu eklenebilir; `merchant_oid`, `return_amount` ve `paytr_token` (HMAC-SHA256) ile istek atılır.

---

## 📋 Özet

- **Ödeme altyapısı:** Proje, PayTR ile çalışacak şekilde **uygun** ve **hazır**.
- **İade altyapısı:** PayTR İade API entegre; admin panelinden **Tam iade** / **Kısmi iade** yapılabiliyor.
- **Eksik kritik kod yok (tahsilat için);** canlıya geçiş için: PayTR panel ayarları, `.env`/ortam değişkenleri ve HTTPS.

Detaylı panel adımları için: `docs/PAYTR-PANEL-AYARLARI.md` ve `docs/RENDER-DEPLOY.md`.
