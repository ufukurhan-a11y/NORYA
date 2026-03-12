# NoryaAI — Almanya Pazarı Odaklı SEO Audit

**Tarih:** Mart 2025  
**Kapsam:** Teknik SEO, içerik SEO, dönüşüm odaklı SEO (DE/Blutwerte odaklı)

---

## 1. Kontrol edilen dosyalar

| Kategori | Dosyalar |
|----------|----------|
| **Landing / meta** | `app/landing_i18n.py`, `app/main.py` (_landing_response, _inject_canonical), `static/index.html` (head, T.de, hreflang) |
| **Pricing / payment** | `app/pay_i18n.py`, `app/templates/pricing.html`, `app/templates/payment_page.html`, `app/main.py` (pricing_landing, payment) |
| **Blog** | `app/blog_i18n.py`, `app/templates/blog/index.html`, `app/templates/blog/detail.html`, `app/main.py` (blog_index, blog_detail) |
| **Sitemap / robots** | `app/main.py` (robots_txt, sitemap_xml) |
| **Legal** | `app/legal_i18n.py`, `app/templates/legal/base_legal.html`, `app/main.py` (legal routes) |
| **Yapı / başlıklar** | `static/index.html` (H1/H2/H3, sections id="..."), blog templates (H1, H2) |
| **Structured data** | `static/index.html` (Organization ld+json), `app/main.py` (BlogPosting, FAQPage), `app/templates/blog/detail.html` |
| **Internal links** | `static/index.html` (nav, drawer, footer, CTA), blog templates (CTA href) |

---

## 2. En kritik SEO sorunları (önem sırasına göre)

### P0 — Yüksek öncelik

1. **Root "/" sayfası her zaman Türkçe meta/title**
   - `/` için `_index_response` kullanılıyor; title/description static index.html’de sabit (TR). Canonical `"/"`.
   - **Risk:** DE veya EN kullanıcı root’a gelirse TR başlık görür; dil sinyali karışır, DE hedef sayfa olarak güçlenmez.
   - **Öneri:** Root için Accept-Language veya tek bir “default” dil (örn. EN) ile title/meta enjekte etmek veya `/` → `/en` 302 ile yönlendirmek.

2. **Blog CTA linkleri locale-aware değil**
   - Blog index ve detail’de CTA `href="/upload"`. DE kullanıcı `/de/blog`’dan tıklayınca `/upload`’a gidiyor; dil bağlamı kaybolabiliyor.
   - **Öneri:** Blog şablonunda CTA’yı `/{lang}/upload` veya `/{lang}#analyze` (SPA varsa) yapmak; `current_lang` zaten mevcut.

3. **Landing’de “Preise” linki /payment’a gidiyor**
   - Nav’da “Fiyatlandırma/Preise” → `/payment`. SEO ve kullanıcı niyeti açısından plan karşılaştırma sayfası `/pricing` daha uygun; ödeme tek adım önce.
   - **Risk:** “Preise” araması veya crawler /pricing’i bulamayabilir; internal link sinyali /pricing’e zayıf.
   - **Öneri:** En azından footer’da “Preise & Pakete” ile `/pricing` linki eklemek; nav’ı /pricing + sonra checkout’a yönlendirme şeklinde düşünmek.

### P1 — Orta-yüksek

4. **Organization schema sadece TR**
   - `static/index.html` içinde ld+json Organization: `addressCountry: TR`, `areaServed: Türkiye`. DE/global kullanıcı için dil/ülke uyumsuz.
   - **Öneri:** Locale’e göre farklı schema (veya `areaServed` çoklu ülke) enjekte etmek; DE için `de` / Germany eklenebilir.

5. **/analyze yönlendirmesi locale kaybettiriyor**
   - `GET /analyze` → `/#analyze` (302). DE kullanıcı `/de` kontekstindeyken blog’dan “Analysieren” ile `/analyze`’e giderse root’a düşer.
   - **Öneri:** Referer veya cookie ile dil bilgisi varsa `/{locale}#analyze`’e redirect (veya blog CTA’yı doğrudan `/{lang}#analyze` / `/{lang}/upload` yapmak).

6. **Pricing sayfasında hreflang yok**
   - `/pricing` tek URL; dil `Accept-Language` / cookie ile. Canonical doğru (`/pricing`) ama dil versiyonları için hreflang tanımlı değil.
   - **Öneri:** DE odak için `hreflang="de"` + `x-default` eklenebilir (veya dil parametreli alternatifler).

7. **Landing’de birden fazla H1 riski (SPA)**
   - Tek sayfa içinde hero (hero_title), rapor önizlemesi (report_hero_title), profil (profile) gibi bölümler var. Görünür H1 sadece hero; diğerleri farklı “view”larda. Mevcut yapı kabul edilebilir ama “How it works” bölümünde ikinci bir H2 benzeri başlık yapısı kontrol edilmeli (şu an H2/H3 tutarlı).

### P2 — Orta

8. **WebSite / BreadcrumbList schema yok**
   - Organization var; WebSite (potentialAction, sitelinks) veya BreadcrumbList (blog, legal) eklenmemiş. DE blog için breadcrumb faydalı olur.

9. **Twitter kartları statik**
   - `twitter:title` / `twitter:description` static index’te sabit (TR). Landing locale’e göre güncellenmiyor.

10. **Legal sayfalar tek URL + ?lang**
    - `/legal/{page}` tek URL; dil `?lang=de` veya Accept-Language. DE için ayrı path yok; duplicate risk düşük ama “Almanca hukuki sayfa” sinyali path’ten gelmiyor.

---

## 3. Quick wins (hemen yapılabilecekler)

| # | Öneri | Dosya / yer | Etki |
|---|--------|-------------|------|
| 1 | Blog CTA linklerini locale-aware yap: `href="/upload"` → `href="/{{ current_lang }}/upload"` (veya SPA’da `/{{ current_lang }}#analyze`) | `app/templates/blog/index.html`, `app/templates/blog/detail.html` | DE blog → DE analiz akışı, dönüşüm sinyali |
| 2 | Footer’a “Preise & Pakete” / “Pricing” ile `/pricing` linki ekle (mevcut nav’a dokunmadan) | `static/index.html` (footer) | /pricing internal link, “Preise” niyeti |
| 3 | Twitter meta’yı landing locale’e göre set et (title/description) | `app/main.py` (_landing_response) + static index’te replace | Paylaşımda doğru dil |
| 4 | Organization schema’ya DE için `areaServed` ekle veya locale’e göre ikinci bir areaServed (Germany) ekle | `static/index.html` veya server enjeksiyonu | DE/global güven sinyali |
| 5 | Root `/` için: EN veya Accept-Language’a göre tek bir default dil ile title/meta enjeksiyonu (veya basitçe `/` → `/en` redirect) | `app/main.py` | Root’ta yanlış dil başlığı riski azalır |

---

## 4. Orta vadeli geliştirmeler

| # | Öneri | Açıklama |
|---|--------|----------|
| 1 | /analyze redirect’i locale-aware yap | Referer path’ten veya cookie’den dil çıkarıp `/{locale}#analyze` veya `/{locale}/upload`’a yönlendir. |
| 2 | Pricing’e hreflang ekle | `/pricing` için alternatif olarak `?lang=de` veya ileride `/de/pricing` path’leri + hreflang. |
| 3 | WebSite + BreadcrumbList schema | Ana sayfa için WebSite (url, name, potentialAction); blog/legal için BreadcrumbList. |
| 4 | Landing’de FAQ schema | SSS bölümünde FAQPage ld+json (locale’e göre) — zaten blog’da var, landing’de tekrarlanabilir. |
| 5 | Ayrı DE “Preise”-odaklı landing blok | /de sayfasında pricing bölümüne “Blutwerte auswerten — Preise” gibi ek H2 + kısa açıklama (içerik SEO). |
| 6 | Blog “Blutwerte online analysieren” makalesi | DE’de bu niyete özel tek bir kısa rehber (örn. “Blutwerte online analysieren: So geht’s”) + internal link /de ve /de/blog’a. |

---

## 5. Almanya pazarı için içerik ve landing önerileri

### Anahtar niyetler (mevcut durum)

| Niyet | Landing / blog durumu | Öneri |
|-------|------------------------|--------|
| **Blutwerte verstehen** | DE meta_title, hero_title, blog seo_title’da kullanılıyor. | Yeterli; ek olarak H2 altında 1 cümle “Blutwerte verstehen” geçebilir. |
| **Laborwerte verstehen** | Meta ve blog’da var. | Blog “Blutbefund lesen” meta_description’da “Laborwerte einordnen” eklendi; iyi. |
| **Blutbild verstehen** | who_3_desc, pdf_header, doctor_header’da “Blutbild”. | Tutarlı kullanım; ek sayfa gerekmez. |
| **Bluttest auswerten** | pricing_page_title’da “Blutwerte auswerten”. | Güçlü; pricing bölümünde 1 cümle “Bluttest auswerten” geçebilir. |
| **Laborergebnisse verstehen** | Meta, blog, hero’da sık. | İyi dağılım. |
| **Blutwerte online analysieren** | Doğrudan cümle yok; “analysieren” / “Auswertung” var. | DE landing veya blog’da “Blutwerte online analysieren” ifadesiyle kısa paragraf veya başlık eklenebilir. |

### Landing sayfası (DE)

- **Mevcut:** Hero “Blutwerte in Minuten verstehen”, meta güçlü, CTA “Analyse starten”, trust, pricing, SSS, Infrastruktur & Sicherheit bölümü i18n’li.
- **Öneriler:**
  - “How it works” bölümünde (DE) bir alt başlık: “Blutwerte online analysieren — in drei Schritten.”
  - Pricing kartı üstünde kısa satır: “Blutwerte auswerten: Einzelbericht oder Abo.”
  - SSS’te bir soru: “Kann ich meine Laborwerte bei Norya auswerten?” (cevap evet + kısa açıklama).

### Blog (DE)

- **Mevcut:** LDL, Ferritin, CRP, Vitamin D, “Blutwerte lesen”, “Blutwerte erklärt” gibi makaleler; seo_title/meta DE için düzenli.
- **Öneriler:**
  - “Blutwerte online analysieren” veya “Laborergebnisse online verstehen” odaklı tek bir kısa rehber (how-to).
  - Her DE makalede son paragrafta “Blutwerte bei Norya auswerten” CTA + `/de` veya `/de#analyze` linki (locale-aware).

---

## 6. Kısa puanlama ve değerlendirme

| Alan | Puan (1–10) | Not |
|------|-------------|-----|
| **Teknik SEO** | **7,5** | Canonical, hreflang (landing + blog), sitemap, robots, noindex payment iyi. Eksik: root dil, pricing hreflang, Organization locale, blog CTA locale. |
| **İçerik SEO** | **7,5** | DE meta/hero/blog niyetleri iyi dağıtılmış; “Blutwerte/Laborwerte verstehen” güçlü. Eksik: “Blutwerte online analysieren” odaklı sayfa/makale, landing’de 1–2 ek DE cümle. |
| **Dönüşüm SEO** | **6,5** | CTA metinleri net; fakat blog CTA /upload locale kaybettiriyor, nav “Preise” → /payment (pricing sayfası zayıf link alıyor), /analyze redirect dil kaybettiriyor. Düzeltmelerle 7,5+ hedeflenebilir. |

**Genel:** Almanya pazarı için temel (URL yapısı, DE meta, blog, sitemap, canonical, hreflang) sağlam. En büyük kazanım: blog ve analiz akışını locale-aware yapmak, root’u dil açısından netleştirmek, /pricing’i internal link ve (isteğe) hreflang ile güçlendirmek. Bu audit’te sadece tespit ve öneri yapıldı; büyük yapısal/routing değişikliği önerilmedi.

---

## Güncelleme: 10'a yaklaşan iyileştirmeler (uygulandı)

Aşağıdaki maddeler uygulandı; puanlar güncellendi.

| Yapılan | Dosya / yer |
|--------|-------------|
| Root `/` EN meta + Twitter meta | `app/main.py` _index_response |
| Blog CTA locale-aware | `app/templates/blog/index.html`, `detail.html` → `/{lang}/upload` |
| Nav/drawer Fiyatlandırma → `/pricing` | `static/index.html` nav + drawer linkleri |
| Footer Preise/Pricing → `/pricing` | `static/index.html` footer |
| Organization schema + Germany | `static/index.html` ld+json areaServed |
| **/analyze redirect locale-aware** | `app/main.py` analyze_landing: Referer'dan locale, `/{locale}#analyze` |
| **Pricing hreflang** | `app/templates/pricing.html` tr, de, en, x-default |
| **WebSite schema** | `static/index.html` ld+json WebSite (url, name) |
| **Landing FAQPage schema** | `app/main.py` _landing_response: locale'e göre FAQ ld+json enjeksiyonu |
| DE landing: „Blutwerte online analysieren“ | `static/index.html` DE how_section_desc |

**Güncel puanlar (uygulama sonrası):**

| Alan | Önceki | Sonra | Not |
|------|--------|-------|-----|
| **Teknik SEO** | 7,5 | **8,5** | /analyze locale, pricing hreflang, WebSite schema. |
| **İçerik SEO** | 7,5 | **8,0** | DE cümle, landing FAQ schema. |
| **Dönüşüm SEO** | 6,5 | **8,0** | Nav/drawer → /pricing, /analyze dil koruması, blog CTA locale. |

10/10 yerine 8–8,5 bandı hedeflendi; tam 10 genelde overclaim sayılır, audit güveni için gerçekçi puan tercih edildi.

---

## 9'a çıkarmak için ne kaldı?

Aşağıdakiler yapılırsa her alan **9** bandına çekilebilir.

### Teknik SEO (8,5 → 9)

| # | Yapılacak | Açıklama |
|---|-----------|----------|
| 1 | BreadcrumbList schema | Blog ve legal sayfalarda breadcrumb ld+json (örn. Ana Sayfa > Blog > Makale). |
| 2 | WebSite potentialAction | Ana sayfa WebSite schema'ya SearchAction ekle (site içi arama varsa). |
| 3 | Core Web Vitals / sayfa hızı | LCP, FID, CLS ölçümü; gerekirse görsel/JS optimizasyonu, CDN. |
| 4 | Legal veya pricing path | İsteğe bağlı: `/de/legal/datenschutz` gibi dil path'leri + hreflang. |

### İçerik SEO (8,0 → 9)

| # | Yapılacak | Açıklama |
|---|-----------|----------|
| 1 | DE “Blutwerte online analysieren” makalesi | Blog’da bu niyete özel tek rehber + internal link /de, /de#analyze. |
| 2 | DE landing’de ek cümleler | Pricing bölümünde “Blutwerte auswerten: Einzelbericht oder Abo.”; SSS’te “Kann ich meine Laborwerte bei Norya auswerten?”. |
| 3 | DE blog makalelerinde son CTA | Her DE makalede “Blutwerte bei Norya auswerten” + `/de` veya `/de/upload` linki. |
| 4 | FAQ genişletme | DE için 1–2 ek soru (Laborwerte, Preise, Datenschutz). |

### Dönüşüm SEO (8,0 → 9)

| # | Yapılacak | Açıklama |
|---|-----------|-------------|
| 1 | CTA’ların locale tutarlılığı | Rapor sayfası “Upgrade” / “Preise” linklerinin locale’e göre `/de/pricing` vb. olması (SPA’da base path). |
| 2 | Conversion tracking | Ödeme tamamlama, plan seçimi, analiz sayısı için event/GA4 veya benzeri. |
| 3 | A/B test (isteğe bağlı) | Hero CTA metni veya buton rengi (küçük kazanım). |
| 4 | Funnel metrikleri | Pricing → payment → thank-you sayfa bazlı dönüşüm oranı takibi. |

Öncelik: Teknik için 1–2, içerik için 1–2, dönüşüm için 1–2 madde seçilerek 9’a yaklaşılabilir; hepsi yapılırsa 9+ bandı hedeflenebilir.

---

## Uygulanan (9'a yönelik iyileştirmeler)

Aşağıdaki maddeler uygulandı (Mart 2025).

| Madde | Yapılan |
|-------|---------|
| **BreadcrumbList schema** | Blog detay: Ana Sayfa > Blog > Makale ld+json. Legal sayfalar: Ana Sayfa > Legal > Sayfa ld+json. |
| **WebSite potentialAction** | WebSite schema'ya SearchAction eklendi (blog?q={search_term}). |
| **DE landing ek cümleler** | pricing_hero_sub: „Blutwerte auswerten: Einzelbericht oder Abo.“ (TR/EN/DE/IT). SSS 6. soru: „Kann ich meine Laborwerte bei Norya auswerten?“ (faq_q6/faq_a6). |
| **DE blog son CTA** | Blog detayda DE için ek satır: „Blutwerte bei Norya auswerten — Jetzt starten“ + /de/upload. |
| **FAQ genişletme** | 6. soru TR, EN, DE, IT landing_i18n + static index SSS bölümü + FAQ schema 1–7. |
| **Rapor CTA locale** | NORYA_PAYMENT_REPORT_URL(), __noryaApplyReportPaymentUrls(); tüm rapor upgrade/payment linkleri locale prefix ile (/de/payment?from=report vb.). |

**Henüz yapılmadı (içerik / opsiyonel):** DE „Blutwerte online analysieren“ odaklı yeni blog makalesi (blog_i18n); Core Web Vitals; conversion tracking.
