# QR Kod ile Rapor Doğrulama Sistemi

Müşteri, indirdiği PDF raporundaki **QR kodu** okutarak raporun **doğruluğunu** ve **orijinalliğini** teyit edebilir. Sistem tek analiz, aylık ve yıllık paketlerde çalışır.

---

## Nasıl çalışır?

1. **PDF indirildiğinde** (Tek Analiz / Aylık / Yıllık):
   - Her rapor için benzersiz bir **report_id** ve **doğrulama kodu** (verification_code) üretilir veya mevcut kayıt kullanılır.
   - **İmzalı token** (HMAC) ile doğrulama URL’i oluşturulur:  
     `https://site.com/verify/{report_id}?token=...`
   - Bu URL, **QR kod** olarak PDF’e gömülür; ayrıca PDF’te insan okunabilir **Doğrulama Kodu** gösterilir.

2. **Müşteri QR’ı okuttuğunda**:
   - Tarayıcı `/verify/{report_id}?token=...` sayfasına gider.
   - Sunucu token’ı doğrular (report_id + verification_code ile imza kontrolü).
   - **Geçerli** ise: “Orijinal ve doğrulanmış rapor” mesajı, rapor no, tarih, paket tipi, doğrulama kodu (ve istenirse sınırlı özet) gösterilir.
   - **Geçersiz** ise: “Bu rapor doğrulanamadı” uyarısı gösterilir.

3. **Güvenlik**:
   - Token tahmin edilemez (secret_key ile HMAC).
   - Doğrulama sayfasında **hassas sağlık verisi gösterilmez**; sadece raporun orijinal ve Norya’ya ait olduğu teyit edilir.

---

## Teknik özet

| Bileşen | Açıklama |
|--------|----------|
| **Model** | `app/models/report_verification.py` — ReportVerification (report_id, analysis_id, verification_code, package_type, …) |
| **Servis** | `app/services/report_verification.py` — get_or_create_verification(), _qr_png_base64() |
| **Güvenlik** | `app/core/security.py` — create_report_verification_token(), verify_report_verification_token() |
| **Endpoint** | `GET /verify/{report_id}?token=...` — Doğrulama sayfası (HTML) |
| **PDF** | `app/templates/report_premium.html` — QR ve Doğrulama Kodu alanı (verification_info doluysa) |

**Hangi planlarda QR çıkar?**  
Tek Analiz (single), Aylık (monthly), Yıllık (yearly). Ücretsiz kullanıcıya premium PDF açıksa bile doğrulama kaydı yalnızca single/monthly/yearly için oluşturulur.

---

## Müşteriye anlatım (kısa)

- “Raporunuzun PDF’inde bir **QR kod** ve **Doğrulama Kodu** bulunur.”
- “QR’ı telefonunuzla okutun veya doğrulama linkini tarayıcıda açın.”
- “Açılan sayfada **‘Geçerli – Orijinal ve doğrulanmış rapor’** görüyorsanız, rapor Norya tarafından üretilmiş orijinal rapordur.”

---

## QR okutunca 404 çıkıyorsa

QR’daki link **/verify/{report_id}** sayfasına gider; bu sayfa **backend’de** (FastAPI) tanımlıdır. Frontend (norya.com) ile backend (örn. api.norya.com) ayrı host’lardaysa, QR linkinin **backend adresini** göstermesi gerekir.

**Yapılacaklar:**

1. **Ortam değişkeni:** Backend’in dışarıdan erişildiği adresi ayarlayın:
   ```bash
   BACKEND_PUBLIC_URL=https://api.norya.com
   ```
   (Backend tek domain’deyse, örn. `https://norya.com`, bu değişkeni boş bırakabilirsiniz; istek geldiği host kullanılır.)

2. **Proxy:** Backend ayrı bir subdomain’deyse (api.norya.com), QR zaten `https://api.norya.com/verify/...` olur. Ana sitede (norya.com) `/verify` isteklerini backend’e yönlendiriyorsanız, `BACKEND_PUBLIC_URL=https://norya.com` da kullanılabilir; o zaman QR `https://norya.com/verify/...` olur ve proxy’nin `/verify`’ı backend’e iletmesi gerekir.

**Özet:** 404 alıyorsanız, QR’ın gittiği adresin `/verify/{report_id}` path’ini **sizin FastAPI uygulamanızın** sunması gerekiyor. Ya `BACKEND_PUBLIC_URL` ile QR’ı backend URL’ine yönlendirin, ya da mevcut domain’de `/verify`’ı backend’e proxy’leyin.

---

## Test

- QR’lı örnek PDF: `python3 scripts/test_premium_pdf.py --qr` → `test_premium_report.pdf` (içinde mock QR; canlıda gerçek verify URL’i kullanılır).
- Canlı doğrulama: Ödeme sonrası bir analiz yapıp PDF indirin; PDF’teki QR’ı okutun veya “Doğrulama Kodu”nu ve rapor no’yu not alıp `/verify/{report_id}?token=...` linkini (PDF’teki QR’ın hedefi) tarayıcıda açın.
