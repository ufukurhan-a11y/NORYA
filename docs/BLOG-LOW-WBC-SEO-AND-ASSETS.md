# Low WBC Blog Article — SEO, Görsel ve Implementasyon Notları

**Konu:** Low WBC: common causes explained  
**Slug:** `low-wbc-meaning` (tüm diller)  
**Yayın:** 2026-03-14

---

## 1. Teknik SEO Özeti

| Alan | Değer |
|------|--------|
| **Canonical** | `/{lang}/blog/low-wbc-meaning` (main.py otomatik) |
| **Hreflang** | BLOG_LANGS_PREMIUM (tr, en, es, de, fr, it, he, hi, ar) — blog detail route ile otomatik |
| **Category** | Kan sayımı / Complete blood count / Hemograma / Blutbild / Numération sanguine / Emocromo / ספירת דם / ब्लड काउंट / تحليل الدم |
| **JSON-LD** | BlogPosting + BreadcrumbList (main.py blog_detail ile otomatik) |
| **FAQ schema** | `faq_schema_qa` 9 dilde tanımlı; blog detail şablonunda FAQPage ld+json üretilir |

### Meta / OG (dil bazlı)

- **Meta title:** `{title} | Norya Blog` (örn. EN: "Low WBC: common causes explained | Norya Blog")
- **Meta description:** Her dilde kısa, niyet odaklı (örn. EN: "Low WBC causes explained. For information only.")
- **OG title/description:** Aynı seo_title ve seo_description kullanılır (blog detail'de)
- **OG image:** Makale cover (şu an fallback: `lymphocytes-hero.png`; kalıcı: `low-wbc-hero.png`)

---

## 2. Hedef Anahtar Kelimeler (uygulandı)

- low WBC
- low white blood cells
- what does low WBC mean
- low leukocytes
- leukopenia
- causes of low WBC
- why is my WBC low

İçerik bu terimleri doğal biçimde kullanıyor; başlık ve bölümler diline göre yerelleştirildi. Düşük WBC ≠ sadece “düşük nötrofil” vurgusu metinde yer alıyor.

---

## 3. Internal Linking (içerikte kullanılanlar)

- **CBC / WBC-RBC:** `/en/blog/how-to-understand-wbc-rbc-hgb-and-hct` (ve tr, es, de, fr, it, he, hi, ar slug'ları)
- **Platelets:** `/en/blog/what-do-low-or-high-platelets-mean` (ve diğer diller)
- **Lymphocytes:** `/en/blog/lymphocytes-high-or-low`
- **Monocytes:** `/en/blog/monocytes-high-meaning`
- **High WBC / infection-inflammation:** İlgili makalelere (related articles) ve bağlamda link
- **Analyze:** `/analyze` (en az 2 CTA)
- **Pricing:** `/pricing` (yumuşak CTA)

Tüm blog iç linkleri ilgili dil prefix'i ile (örn. `/tr/blog/...`, `/de/blog/...`) yazıldı.

---

## 4. Hero Görsel Promptu (Low WBC)

Aşağıdaki prompt, **özgün bir premium blog hero görseli** üretmek için kullanılabilir. Görsel adı: `low-wbc-hero.png`, konum: `static/images/blog/low-wbc-hero.png`.

**Önerilen boyut:** 1200×630 px (OG/sosyal paylaşım); oran 16:10 veya 1.91:1. Mobil kırpımda ana mesaj ortada kalacak şekilde kompozisyon.

**Prompt (İngilizce):**

- Clinical but not alarming: soft gradient background (teal #0EA5A4 and white or very light grey), no harsh shadows or dramatic imagery.
- Abstract representation of “low white blood cells” or balanced blood count: e.g. subtle stylised cells in a calm, minimal layout; or a soft “dashboard” feel with a gentle curve suggesting “within range” or “monitoring” — avoid literal microscope or alarming visuals; prefer modern health-tech, clean and reassuring.
- No text or numbers in the image.
- Norya branding: small Norya “N” logo or icon in one corner (e.g. bottom-right), teal, low opacity so it doesn’t dominate.
- Mood: reassuring, professional, informative — not scary. Distinct from high-WBC hero: focus on “understanding” and “causes” rather than elevation or alarm.
- Safe area: keep the main visual focus in the centre third so that 16:9 or mobile crop still reads well.

**Kısa versiyon (görsel üretici için):**

“Premium blog hero image: abstract representation of low white blood cells / understanding WBC. Soft teal (#0EA5A4) and white gradient, minimal and clinical but warm and reassuring. No text. Small Norya N logo in corner. 1200×630px, centered composition for safe cropping. Modern health-tech style, not alarming.”

---

## 5. İkon

- **Yol:** `/static/images/blog/icons/low-wbc-meaning.svg`
- **Konsept:** WBC / leukocyte temasında minimal çizgi ikon; “düşük” veya “takip” hissi — Norya turkuaz rengiyle uyumlu. High WBC ikonundan ayırt edilebilir (örn. farklı yön veya minimal grafik).

İkon eklenene kadar blog listesinde mevcut fallback (varsa) kullanılır; zorunlu değildir.

---

## 6. Implementasyon Notları

- **İçerik:** `app/blog_article_low_wbc_content.py` — tüm dillerde 12 bölüm (intro, what-is-wbc, what-low-means, common-causes, temporary, drugs-infections-immune, result-alone, other-params, when-to-see-doctor, how-norya-helps, cta, disclaimer) ve FAQ (`get_low_wbc_faq_schema_qa`) 9 dilde.
- **Kayıt:** `app/blog_i18n.py` — `_article_low_wbc()`, `_ARTICLE_LOW_WBC`, `ARTICLES` listesine eklendi.
- **Routing:** Mevcut `/{lang}/blog/{slug}` route'u kullanıyor; ek route gerekmedi.
- **CTA:** İçerik içinde en az 2 yerde `/analyze`, bir yerde `/pricing` linki var; CTA bölümü ve disclaimer net.
- **Hero:** Şu an `lymphocytes-hero.png` fallback. Kalıcı görsel eklendiğinde `blog_i18n._article_low_wbc()` içinde `cover` değişkeni `"/static/images/blog/low-wbc-hero.png"` yapılacak.

---

## 7. Test

- Blog listesi: `/{lang}/blog` (örn. `/en/blog`) — “Low WBC: common causes explained” kartı görünmeli.
- Detay: `/{lang}/blog/low-wbc-meaning` (örn. `/en/blog/low-wbc-meaning`) — 12 bölüm, FAQ, CTA, disclaimer ve ilgili makaleler görünmeli.
- Sitemap: `sitemap.xml` içinde tüm dillerde URL'ler otomatik yer alır (`iter_all_article_paths`).
