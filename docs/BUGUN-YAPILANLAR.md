# Bugün Yapılanlar (1 Mart 2026)

Kısa özet: PDF indirme (özellikle canlıda), admin logları, deploy, Cloudflare ve dokümantasyon.

---

## Özet: SEO, çoklu dil landing, GA4, legal hreflang, mobil (13 Mart 2026)

**Kısa özet:** Tüm dil/landing sayfalarında 6. FAQ ve pricing alt metni eklendi (TR, EN, DE, IT, ES, FR, HE, AR, HI, EL, CS, SR). GA4’e `pricing_view`, `payment_start`, `analysis_complete` event’leri ve Core Web Vitals (LCP, FCP, CLS) gönderimi eklendi. Legal sayfalara hreflang (tr, en, de, fr, it, es + x-default) kondu. FAQ accordion’da mobil için 44px touch target sağlandı. Blog tarafında og_locale, Twitter card, ItemList schema, locale-aware report CTA ve DE makale zaten yapılmıştı.

---

### 1. Landing: Tüm dillerde FAQ 6 + pricing satırı

- **Static index.html:** Her dil için `faq_q6`, `faq_a6`, `pricing_hero_sub` eklendi.
- **Diller:** TR, EN, DE, IT, ES, FR, HE, AR, HI, EL, CS, SR (T.tr, T.en, T.de, …).
- **FR:** Apostrof eşleşmesi düzeltildi (Unicode apostrophe).
- **Landing i18n:** tr, en, de, it zaten vardı; en-ca `_en_ui()` kullandığı için otomatik uyumlu.

### 2. GA4 conversion event’leri

- **pricing_view:** `#fiyatlandirma` bölümü görünür olduğunda veya hash `#pricing` / `#fiyatlandirma` olduğunda, oturumda bir kez.
- **payment_start:** `goToCheckout(planKey)` çağrıldığında (single/monthly/yearly), `plan` parametresiyle.
- **analysis_complete:** Rapor ilk kez render edildiğinde bir kez (`renderReport` sonunda).
- gtag placeholder sonrası inline script; `sessionStorage` ile pricing_view tekrarsız.

### 3. Core Web Vitals → GA4

- **LCP:** `PerformanceObserver` ile `largest-contentful-paint`.
- **FCP:** `performance.getEntriesByType('paint')` ile First Contentful Paint.
- **CLS:** `layout-shift` observer, kümülatif değer; `pagehide` ile bir kez gönderim.
- Event isimleri: `LCP`, `FCP`, `CLS`; `value`, `non_interaction: true`.

### 4. Legal sayfalar hreflang

- **`/legal/{page}`** ve **`/iade-iptal`** için `<link rel="alternate" hreflang="..." href="...">` eklendi.
- **Diller:** tr, en, de, fr, it, es + x-default (en).
- **URL:** `.../legal/{page}?lang=tr` vb.
- **Şablon:** `app/templates/legal/base_legal.html` içinde `hreflang_alternates` döngüsü.
- **Backend:** `app/main.py` içinde `legal_page` ve `iade_iptal_page` context’e `hreflang_alternates` ekleniyor.

### 5. Mobil uyumluluk

- **Mevcut:** Viewport, safe-area-inset, touch-action, 44/48px buton yükseklikleri, pricing grid mobil tek sütun zaten vardı.
- **FAQ (SSS):** Tüm 6 maddenin `<summary>` öğesine mobil dokunma alanı eklendi:
  - `min-h-[44px]`, `touch-manipulation`, `-webkit-tap-highlight-color: transparent`.
- **Analytics:** IntersectionObserver, sessionStorage, PerformanceObserver mobil tarayıcılarda destekleniyor.

### 6. Blog ve diğer (önceki oturumlardan)

- Blog index/detail: `og_locale`, Twitter card, ItemList schema, CTA ve “back to landing” tüm dillerde.
- Report CTA: locale-aware payment URL (`NORYA_PAYMENT_REPORT_URL`), `__noryaApplyReportPaymentUrls`.
- DE makale: “Blutwerte online analysieren” eklendi.
- Landing: nav/drawer/footer → `/pricing`, pricing sayfası hreflang, FAQ schema 1–7, WebSite + SearchAction.

**Değişen / eklenen dosyalar:**  
`static/index.html`, `app/main.py`, `app/landing_i18n.py`, `app/blog_i18n.py`, `app/templates/legal/base_legal.html`, `app/templates/blog/index.html`, `app/templates/blog/detail.html`, `app/templates/pricing.html`, `docs/SEO_AUDIT_DE_2025.md`.

---

## 1. PDF indirme (local + canlı)

**Sorun:** Lokalda PDF açılıyordu, canlıda (noryaai.com) “Önce analiz yapın” veya tıklanınca hareket yoktu.

**Yapılanlar:**
- **Backend:** Analiz cevabında her zaman `analiz_id` dönüyor (test modunda da kayıt oluşturulup id dönüyor). PDF için tek kullanımlık token: `POST /analyze/history/{id}/pdf-token` → `access_token`; `GET .../pdf?access_token=...` ile PDF açılıyor (proxy Authorization keserse bile çalışır).
- **Frontend:** “Raporu İndir” önce token alıyor, sonra `?access_token=...` ile PDF URL’ini yeni sekmede açıyor. `rid` yoksa son analiz `/analyze/history?limit=1` ile alınıp URL `?rid=...` ile güncelleniyor. Hata mesajı: sadece gerçekten rid yoksa “Önce analiz yapın”; sunucu hatasında HTTP kodu ve gerçek mesaj gösteriliyor.
- **Console log:** `[PDF] Raporu İndir tıklandı, getReportId()= ...`, Token URL, Token response status — Network/Console’dan takip için.
- **CSP:** `script-src`’e cdnjs ve cloudflareinsights, `img-src`’e `blob:` eklendi. Kullanılmayan jsPDF/html2canvas script’leri kaldırıldı (PDF artık sunucuda).
- **PDF 500:** Backend’de PDF hatası olunca `log.exception` ile tam traceback yazılıyor. Prod’da WeasyPrint için `Dockerfile` (cairo/pango) ve RENDER-DEPLOY’da “PDF 500” bölümü eklendi.

**Dosyalar:** `app/main.py`, `app/core/security.py`, `static/index.html`, `app/services/report_pdf.py`, `Dockerfile`, `docs/RENDER-DEPLOY.md`

---

## 2. Admin: Upload ve Hata logları

- Sol menü: “Dosya Upload Logları”, “Hata Logları”; metin tek satırda düzgün görünsün diye `white-space: nowrap`, sidebar `w-60`.
- Backend’de hata mesajı kısaltması kaldırıldı (`uploads.py` ve `errors.py`’deki `[:100]` / `[:200]`).
- Şablonda hata sütunu: `truncate` kaldırıldı, `break-words`, `whitespace-pre-wrap`, `max-w-xl`, `title` (tooltip) eklendi.

**Dosyalar:** `app/templates/admin/base_admin.html`, `app/templates/admin/uploads_list.html`, `app/templates/admin/errors_list.html`, `app/admin/routers/uploads.py`, `app/admin/routers/errors.py`

---

## 3. PDF rapor içeriği (grafik, diyet, takviye)

- Bölüm başlığı tanıma genişletildi: “Diyet planı”, “Takviye”, “Kalp” vb. ayrı bölüm olarak `raw_sections`’a düşüyor.
- Biyobelirteç satırı için esnek regex (`BIOMARKER_LINE_RELAXED`) eklendi; tablo ve range bar grafiklerinin daha sık üretilmesi hedeflendi.

**Dosyalar:** `app/services/report_pdf.py`

---

## 4. Deploy ve sunucu

- **Deploy:** `deploy/deploy.sh` (commit + push; Render otomatik build), `deploy/README-DEPLOY.md`.
- **Sunucu yeniden başlatma:** `./portu-kapat-ve-baslat.sh` veya `./restart-server.sh`; kullanım notları verildi.

**Dosyalar:** `deploy/deploy.sh`, `deploy/README-DEPLOY.md`, `restart-server.sh`

---

## 5. Cloudflare

- **docs/CLOUDFLARE-VE-GOOGLE-ANALYTICS.md** güncellendi: PDF ve sitenin açılması için kısa liste:
  - SSL/TLS: Full (+ Always Use HTTPS).
  - Speed → Rocket Loader: Kapalı.
  - Security → Security Level: Medium veya Low.
  - Authorization / CSP header’ları değiştirilmesin.
  - Tarayıcıda noryaai.com için pop-up izni.

---

## 6. Dokümantasyon

- RENDER-DEPLOY: PDF 500 ve Docker/WeasyPrint bölümü.
- Cloudflare: sadece yapılacaklar listesi, gereksiz detay azaltıldı.

---

**Canlıda PDF’in düzelmesi için:** Bu değişikliklerin hepsi deploy edilmeli (`./deploy/deploy.sh`), Render build bitmeli, sayfa sert yenilenmeli (Cmd+Shift+R). Cloudflare’de Rocket Loader kapalı, Security Level makul olmalı.
