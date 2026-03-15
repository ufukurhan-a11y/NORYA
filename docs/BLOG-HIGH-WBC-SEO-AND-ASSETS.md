# High WBC Blog Article — SEO, Görsel ve Implementasyon Notları

**Konu:** High WBC: infection or inflammation?  
**Slug:** `high-wbc-meaning` (tüm diller)  
**Yayın:** 2026-03-14

---

## 1. Teknik SEO Özeti

| Alan | Değer |
|------|--------|
| **Canonical** | `/{lang}/blog/high-wbc-meaning` (main.py otomatik) |
| **Hreflang** | BLOG_LANGS_PREMIUM (tr, en, es, de, fr, it, he, hi, ar) — blog detail route ile otomatik |
| **Category** | Kan sayımı / Complete blood count / Hemograma / Blutbild / Numération sanguine / Emocromo / ספירת דם / ब्लड काउंट / تحليل الدم |
| **JSON-LD** | BlogPosting + BreadcrumbList (main.py blog_detail ile otomatik) |
| **FAQ schema** | `faq_schema_qa` 9 dilde tanımlı; blog detail şablonunda FAQPage ld+json üretilir |

### Meta / OG (dil bazlı)

- **Meta title:** `{title} | Norya Blog` (örn. EN: "High WBC: infection or inflammation? | Norya Blog")
- **Meta description:** Her dilde kısa, niyet odaklı (örn. EN: "High WBC causes: infection or inflammation. For information only.")
- **OG title/description:** Aynı seo_title ve seo_description kullanılır (blog detail'de)
- **OG image:** Makale cover (şu an fallback: `lymphocytes-hero.png`; kalıcı: `high-wbc-hero.png`)

---

## 2. Hedef Anahtar Kelimeler (uygulandı)

- high WBC
- high white blood cells
- what does high WBC mean
- high leukocytes
- high white blood cell count
- infection or inflammation blood test
- WBC high causes

İçerik bu terimleri doğal biçimde kullanıyor; başlık ve bölümler diline göre yerelleştirildi.

---

## 3. Internal Linking (içerikte kullanılanlar)

- **CBC / WBC-RBC:** `/en/blog/how-to-understand-wbc-rbc-hgb-and-hct` (ve tr, es, de, fr, it, he, hi, ar slug’ları)
- **Platelets:** `/en/blog/what-do-low-or-high-platelets-mean` (ve diğer diller)
- **Lymphocytes:** `/en/blog/lymphocytes-high-or-low`
- **Monocytes:** `/en/blog/monocytes-high-meaning`
- **Analyze:** `/analyze`
- **Pricing:** `/pricing`

Tüm blog iç linkleri ilgili dil prefix’i ile (örn. `/tr/blog/...`, `/de/blog/...`) yazıldı.

---

## 4. Hero Görsel Promptu (High WBC)

Aşağıdaki prompt, **özgün bir premium blog hero görseli** üretmek için kullanılabilir. Görsel adı: `high-wbc-hero.png`, konum: `static/images/blog/high-wbc-hero.png`.

**Önerilen boyut:** 1200×630 px (OG/sosyal paylaşım); oran 16:10 veya 1.91:1. Mobil kırpımda ana mesaj ortada kalacak şekilde kompozisyon.

**Prompt (İngilizce):**

- Clinical but not cold: soft gradient background (teal #0EA5A4 and white or very light grey), no harsh shadows.
- Abstract representation of “high white blood cells” or immune activation: e.g. subtle stylised white blood cells or a soft “dashboard” feel with a single clear metric (e.g. a gentle curve or bar suggesting “elevated”) — avoid literal microscope imagery; prefer modern health-tech, clean and minimal.
- No text or numbers in the image.
- Norya branding: small Norya “N” logo or icon in one corner (e.g. bottom-right), teal, low opacity so it doesn’t dominate.
- Mood: reassuring, professional, informative — not alarming. Distinct from other blog heroes (e.g. lymphocytes, monocytes, eosinophils): different composition (e.g. focus on “elevation” or “immune response” rather than a single cell type).
- Safe area: keep the main visual focus in the centre third so that 16:9 or mobile crop still reads well.

**Kısa versiyon (görsel üretici için):**

“Premium blog hero image: abstract representation of elevated white blood cells / immune response. Soft teal (#0EA5A4) and white gradient, minimal and clinical but warm. No text. Small Norya N logo in corner. 1200×630px, centered composition for safe cropping. Modern health-tech style, not stock-photo generic.”

---

## 5. İkon

- **Yol:** `/static/images/blog/icons/high-wbc-meaning.svg`
- **Konsept:** WBC / leukocyte / beyaz küre temasında minimal çizgi ikon; Norya turkuaz rengiyle uyumlu. Örn. tek stilize hücre veya “yükseklik” hissi veren minimal grafik.

İkon eklenene kadar blog listesinde mevcut fallback (varsa) kullanılır; zorunlu değildir.

---

## 6. Implementasyon Notları

- **İçerik:** `app/blog_article_high_wbc_content.py` — tüm dillerde 12 bölüm (intro, what-is-wbc, what-high-means, infection-vs-inflammation, common-causes, temporary, result-alone, other-tests, when-to-see-doctor, how-norya-helps, cta, disclaimer) ve FAQ (`get_high_wbc_faq_schema_qa`).
- **Kayıt:** `app/blog_i18n.py` — `_article_high_wbc()`, `_ARTICLE_HIGH_WBC`, `ARTICLES` listesine eklendi.
- **Routing:** Mevcut `/{lang}/blog/{slug}` route’u kullanıyor; ek route gerekmedi.
- **CTA:** İçerik içinde en az 2 yerde `/analyze`, bir yerde `/pricing` linki var; CTA bölümü ve disclaimer net.
- **Hero:** Şu an `lymphocytes-hero.png` fallback. Kalıcı görsel eklendiğinde `blog_i18n._article_high_wbc()` içinde `cover` değişkeni `"/static/images/blog/high-wbc-hero.png"` yapılacak.

---

## 7. Test

- Blog listesi: `/{lang}/blog` (örn. `/en/blog`) — “High WBC: infection or inflammation?” kartı görünmeli.
- Detay: `/{lang}/blog/high-wbc-meaning` (örn. `/en/blog/high-wbc-meaning`) — 12 bölüm, FAQ, CTA, disclaimer ve ilgili makaleler görünmeli.
- Sitemap: `sitemap.xml` içinde tüm dillerde URL’ler otomatik yer alır (`iter_all_article_paths`).
