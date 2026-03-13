# NoryaAI Çok Dilli Teknik SEO – Analiz ve Uygulama Planı

**Hedef diller:** TR, EN, ES, DE, FR, IT, HE, HI, AR (9 dil)  
**Amaç:** Her dil için temiz URL, hreflang, canonical, sitemap; dil karışması yok; mevcut tasarım ve backend korunacak.  
**Teslim:** Sadece analiz ve değişiklik planı (henüz kod yazılmadı).

---

## 1. Mevcut routing yapısı özeti

| Sayfa tipi | Mevcut URL yapısı | Dil seçimi | Not |
|------------|-------------------|------------|-----|
| Ana sayfa | `/`, `/tr`, `/en`, `/en-ca`, `/de`, `/it` | Path (ayrı route) | Sadece 5 dil; ES, FR, HE, HI, AR yok |
| SPA catch-all | `/{lang}`, `/{lang}/{path:path}` | Path | `SUPPORTED_LOCALES`: en, de, it, fr, es, tr, ar, hi, he, el, sr — blog ile çakışmadan önce tanımlı |
| Blog index | `/blog` → 302 `/en/blog`, `/{lang}/blog` | Path | `BLOG_LANGS_PREMIUM`: tr, en, es, de, fr, it, he, hi, ar (9 dil ✓) |
| Blog detay | `/{lang}/blog/{slug}` | Path | Aynı 9 dil |
| SEO landing | `/tr/kan-tahlili-sonucu`, `/en/blood-test-results`, `/de/...` | Path | Sadece TR, EN, DE; slug dil bazlı |
| How it works | `/how-it-works` | Query `?lang=` | Tek URL; diller: de, en, tr, it, fr, es (HE, HI, AR yok) |
| Pricing | `/pricing` | Cookie / `?lang=` | Tek URL; `PAYMENT_LANGS`: tr, en, de, fr, it, es |
| Legal | `/legal/{page}`, `/iade-iptal` | Query `?lang=` | Tek URL; `legal_hreflang_langs`: tr, en, de, fr, it, es |
| Kurumsal | `/kurumsal` | Cookie / Accept-Language | Tek URL; hreflang yok |
| Pay / Payment | `/pay`, `/payment` | Cookie / query | Tek URL; canonical var, hreflang yok |
| Report / Analyze | `/report`, `/analyze` | Query / hash | SPA; canonical enjekte |

**Özet:** Landing ve blog path tabanlı; how-it-works, legal, pricing query tabanlı veya tek URL. Hedef 9 dil için landing’de 4 dil eksik (ES, FR, HE, HI, AR); how-it-works ve legal’da 3 dil eksik (HE, HI, AR).

---

## 2. URL yapısı önerisi (hedef 9 dil ile uyum)

- **Korunacak (zaten temiz):**
  - Ana sayfa: `/{locale}` → `tr`, `en`, `es`, `de`, `fr`, `it`, `he`, `hi`, `ar` (en-ca istenirse ayrı tutulabilir veya en ile birleştirilebilir).
  - Blog: `/{lang}/blog`, `/{lang}/blog/{slug}` — 9 dil zaten tanımlı.
  - SEO landing: `/{lang}/{slug}` — yapı aynı kalacak; yeni dillere slug eklenebilir.
- **Path’e taşınması önerilen (isteğe bağlı, büyük değişiklik):**
  - How-it-works: `/how-it-works` (mevcut) kalabilir; alternatif: `/{lang}/how-it-works` ile her dil için ayrı URL (sitemap’e dil bazlı eklenir, hreflang path’e göre).
  - Legal: `/legal/{page}` kalabilir; hreflang `?lang=` ile devam eder. İstenirse `/{lang}/legal/{page}` path yapısına geçilebilir (daha büyük refactor).
- **Pricing:** Tek URL `/pricing` kalabilir; hreflang’e tüm 9 dil eklenir (aynı URL, `?lang=xx` ile dil; veya ileride `/{lang}/pricing`).
- **Kural:** Aynı sayfada tek dil; dil path veya `?lang=` ile belirlenir, karışma olmaz.

**Öneri (minimal değişiklik):**  
- Landing: 9 dil için route + meta + hreflang (ES, FR, HE, HI, AR ekle; en-ca ayrı kalabilir).  
- How-it-works / Legal / Pricing: Mevcut tek URL + query/cookie; sadece hreflang listesini 9 dile çıkar (ve x-default).  
- Path’e geçiş (örn. `/{lang}/how-it-works`) ikinci aşamada yapılabilir.

---

## 3. rel=canonical durumu ve yapılacaklar

| Sayfa | Mevcut canonical | Yapılacak |
|-------|------------------|-----------|
| `/` | Enjekte: `base_url + request.url.path` → `base_url/` | Root için sabit `base_url/` veya dil yönlendirmesi politikasına göre tek canonical (örn. `base_url/en` x-default ise root’u en’e yönlendirip canonical’i `/en` yapmak isteğe bağlı). |
| `/{locale}` (landing) | `base_url/{locale}` | Doğru; 9 dil route’larına geçince aynı mantık. |
| `/{lang}/blog` | `base_url/{lang}/blog` | Doğru; değişiklik yok. |
| `/{lang}/blog/{slug}` | `base_url/{lang}/blog/{slug}` | Doğru; değişiklik yok. |
| SEO landing | `base_url/{lang}/{slug}` | Doğru; yeni dil/slug’lar eklendiğinde aynı. |
| How-it-works | `base_url/how-it-works` | Tek canonical doğru; path’e geçilirse `base_url/{lang}/how-it-works`. |
| Legal / iade-iptal | `base_url/legal/{page}`, `base_url/iade-iptal` | Doğru. |
| Pricing / Pay / Payment | `base_url/pricing`, `/pay`, `/payment` | Doğru. |
| Report | `base_url/report` | Doğru. |
| SPA `/{lang}/...` | `base_url + request.url.path` | Doğru; path dil içeriyor, canonical aynı path. |

**Yapılacak:** Yeni landing dilleri eklendiğinde canonical’in her zaman `base_url/{locale}` veya ilgili path olduğundan emin olmak (zaten _landing_response ve _inject_canonical ile yapılıyor).

---

## 4. hreflang durumu ve yapılacaklar

| Sayfa | Mevcut hreflang | Eksik / yanlış | Yapılacak |
|-------|------------------|----------------|-----------|
| static/index.html (ham) | tr, en, en-CA, de, it, x-default (en) | ES, FR, HE, HI, AR | 9 dile çıkar; x-default = en; en-ca istenirse ayrı kalır veya kaldırılır. |
| _landing_response (enjekte) | tr, en, en-CA, de, it, x-default | ES, FR, HE, HI, AR | Aynı 9 dil (ve isteğe bağlı en-ca) bloğu ile değiştir. |
| Blog index/detail | BLOG_LANGS_PREMIUM (9 dil) | x-default blog detail’da ayrı döngü ile en | Mevcut yapı doğru; x-default’un her sayfada tek ve doğru olduğunu doğrula. |
| SEO landing | get_seo_landing_hreflang: sadece alternatif eşleşen diller + self + x-default | Bazı sayfalarda sadece 1–2 dil | Tüm 9 dilde içerik yoksa sadece mevcut dil varyantları + x-default doğru; yeni landing’ler eklenirken hreflang matrisi güncellenecek. |
| How-it-works | HOW_IT_WORKS_LANGS (6 dil) + x-default | HE, HI, AR | 9 dile çıkar (içerik eklenmeli) veya mevcut 6’da bırakıp x-default’u koru. |
| Legal / iade-iptal | 6 dil (tr, en, de, fr, it, es) | HE, HI, AR | İçerik varsa 9 dil; yoksa 6’da bırakılabilir. |
| Pricing | tr, de, en, x-default (4 link) | ES, FR, IT, HE, HI, AR | 9 dil + x-default; URL aynı `/pricing` (veya ileride `/{lang}/pricing`). |
| Kurumsal | Yok | Tümü | 9 dil hreflang ekle (URL tek `/kurumsal` veya `?lang=`). |

**x-default:**  
- Ana sayfa / landing: x-default = EN (uluslararası varsayılan).  
- Blog: x-default = EN (mevcut).  
- Diğer sayfalar: x-default = EN tutulacak.

---

## 5. Sitemap durumu ve yapılacaklar

- **Mevcut sitemap.xml içeriği:**
  - `/`, `/{locale}` (LANDING_ROUTES: tr, en, en-ca, de, it)
  - `/pricing`, `/how-it-works`, `/kurumsal`
  - `/legal/{page}` (her sayfa 1 URL, dil yok)
  - SEO landing: iter_seo_landing_urls() → (lang, slug)
  - Blog: BLOG_LANGS_PREMIUM için `/{lang}/blog`; iter_all_article_paths() ile `/{lang}/blog/{slug}` + lastmod

- **Yapılacaklar:**
  1. LANDING_ROUTES 9 dile genişletilince sitemap’teki landing listesini aynı sabitten türetmek (es, fr, he, hi, ar eklenir).
  2. How-it-works: Tek URL kalıyorsa mevcut gibi 1 giriş; path’e geçilirse `/{lang}/how-it-works` için 9 giriş eklemek.
  3. Legal: Mevcut tek URL kalacak; dil path’e taşınırsa `/{lang}/legal/{page}` eklenir.
  4. Blog: Zaten dil bazlı; BLOG_LANGS_PREMIUM değişmeyecek, testler tr, en, es, de, fr, it, he, hi, ar index’lerini kontrol edecek şekilde güncellenebilir.
  5. SEO landing: Yeni (lang, slug) eklendikçe iter_seo_landing_urls() zaten sitemap’e dahil ediyor; ek iş yok.

---

## 6. Blog ve landing SEO metadata

- **Blog:**  
  - Dil bazlı seo_title, meta description, og:*, hreflang, canonical zaten var.  
  - Yapılacak: Sadece 9 dil tutarlılığı (zaten BLOG_LANGS_PREMIUM 9 dil); yeni dil eklendiğinde BLOG_UI ve makale available_langs kontrolü.

- **Landing (ana sayfa):**  
  - get_landing_meta(locale), get_landing_ui(locale) ile title/description/og enjekte.  
  - Yapılacak: ES, FR, HE, HI, AR için LANDING_META ve landing UI sözlükleri eklemek; LANDING_ROUTES’u 9 dile çıkarmak.

- **SEO landing (kan-tahlili-sonucu vb.):**  
  - get_seo_landing_meta, get_seo_landing_content, get_seo_landing_hreflang mevcut.  
  - Yapılacak: Yeni diller için sayfa ve slug’lar eklenirken SEO_LANDING_ROUTES ve SEO_LANDING_HREFLANG güncellenecek; metadata ve hreflang otomatik uyumlu.

---

## 7. Aynı sayfada dil karışması

- **Mevcut:**  
  - Landing: Her URL’de tek locale (path); __LANDING_LOCALE__ ve __LANDING_T__ ile SPA aynı dili kullanıyor.  
  - Blog: Path ile dil sabit; içerik tek dil.  
  - Legal/How-it-works/Pricing: Tek sayfa, ?lang= veya cookie ile tek dil seçili.

- **Kural:**  
  - İçerik ve meta (title, description, og:locale) her zaman tek dil kodu ile üretilecek.  
  - Nav/footer linkleri: SPA’da mevcut `/pricing`, `/blog` gibi; /blog zaten /en/blog’a yönlendiriyor. İstenirse nav’de “Blog” linki locale’e göre `/{current_lang}/blog` yapılabilir (crawl edilebilir linkler için `/{lang}/blog` sitemap’te zaten var).

- **Yapılacak:**  
  - Yeni landing dilleri eklerken LANDING_META ve get_landing_ui’da sadece o dilde metin kullanmak.  
  - Dil seçici (varsa) tüm 9 dili gösterebilir; seçim path veya query ile tek sayfada tek dil kalacak şekilde yapılacak.

---

## 8. İç linklerin taranabilirliği

- **Mevcut:**  
  - Sitemap’te `/{lang}/blog`, `/{lang}/blog/{slug}` tüm dillerde listeleniyor.  
  - Ana sayfa ve landing’den `/pricing`, `/how-it-works`, `/analyze` gibi linkler var; bunlar tek URL olduğu için zaten crawl edilebilir.  
  - Blog’dan get_related_articles ve CTA linkleri base_url ile absolute; dil prefix’i template’te veriliyor.

- **Yapılacak:**  
  - Nav/drawer’daki “Blog” linkini locale’e göre `/{lang}/blog` yapmak (SPA’da __LANDING_LOCALE__ veya benzeri ile). Böylece her dil sayfasından o dilin blog index’ine link çıkar.  
  - Footer’da “Blog” için aynı mantık veya genel `/en/blog` (x-default) bırakılabilir.  
  - Tüm önemli sayfalar sitemap’te olduğu sürece crawl edilebilirlik korunur.

---

## 9. Mevcut backend ve tasarımı bozmama

- **Backend:**  
  - Yeni route’lar sadece eklenmeli (örn. `/es`, `/fr`, `/he`, `/hi`, `/ar` landing).  
  - Var olan endpoint’lerin imzası ve response formatı değiştirilmeyecek; sadece LANDING_ROUTES, HOW_IT_WORKS_LANGS, legal_hreflang_langs, PAYMENT_LANGS gibi sabitler genişletilecek.  
  - _landing_response ve _index_response’ta sadece hreflang listesi ve locale sayısı artacak; HTML enjeksiyon mantığı aynı kalacak.

- **Tasarım:**  
  - Yeni dil için aynı index.html ve aynı template’ler kullanılacak; sadece metin kaynakları (landing_i18n, how_it_works_i18n, legal_i18n, pay_i18n) genişletilecek.  
  - CSS ve layout değişmeyecek; RTL (AR, HE) için ileride ayrı bir görev açılabilir (bu planda zorunlu değil).

---

## 10. Uygulama adımları (sıra ile)

1. **Sabit dil listesi (tek kaynak)**  
   - `app/core/config.py` veya `app/base_i18n.py` içinde `SEO_TARGET_LANGS = ("tr", "en", "es", "de", "fr", "it", "he", "hi", "ar")` tanımla.  
   - LANDING_ROUTES’u bu listeye göre genişlet (en-ca ayrı kalabilir: LANDING_ROUTES = SEO_TARGET_LANGS veya tuple’a en-ca ekle).

2. **Landing: 4 yeni dil (ES, FR, HE, HI, AR)**  
   - `app/landing_i18n.py`: LANDING_ROUTES’a es, fr, he, hi, ar ekle; LANDING_META ve get_landing_ui için bu dillerde metin ekle (ve gerekirse get_landing_ui’da fallback).  
   - `app/main.py`: `/es`, `/fr`, `/he`, `/hi`, `/ar` route’larını ekle (_landing_response(locale, request) ile).  
   - static/index.html: head’deki hreflang bloğunu 9 dil + x-default olacak şekilde güncelle (veya tamamen backend enjeksiyonuna bırak; landing’de zaten enjekte ediliyor).  
   - _landing_response içinde hreflang_lines’ı 9 dile (ve isteğe bağlı en-ca) çıkar.

3. **Canonical**  
   - Root ve landing: Mevcut mantık aynı; yeni route’lar için canonical `base_url/{locale}` olacak.  
   - Diğer sayfalarda değişiklik yok.

4. **hreflang**  
   - Landing: Adım 2’de.  
   - Pricing: `app/templates/pricing.html` — 9 dil + x-default linkleri ekle (URL `/pricing` kalabilir).  
   - How-it-works: HOW_IT_WORKS_LANGS’ı 9 dile çıkarmak için önce içerik ekle; sonra hreflang listesini 9 dil + x-default yap.  
   - Legal / iade-iptal: legal_hreflang_langs’ı 9 dile çıkar (içerik varsa); yoksa 6’da bırak.  
   - Kurumsal: 9 dil hreflang ekle (URL `/kurumsal` veya `?lang=`).  
   - Blog: Mevcut; x-default’un her detay sayfasında doğru eklendiğini doğrula.  
   - SEO landing: get_seo_landing_hreflang tüm alternatifleri içeriyor; yeni sayfa eklerken SEO_LANDING_HREFLANG’i güncelle.

5. **x-default**  
   - Tüm hreflang setlerinde x-default = EN (veya ana sayfa için tercih edilen varsayılan) olacak şekilde kontrol et.

6. **Sitemap**  
   - LANDING_ROUTES genişlediği için sitemap_xml’deki landing döngüsü otomatik 9 dili ekleyecek.  
   - How-it-works path’e taşınmazsa 1 URL kalır; taşınırsa 9 URL eklenir.  
   - Test: tests/test_sitemap.py — blog için 9 dil index kontrolü (tr, en, es, de, fr, it, he, hi, ar) eklenebilir.

7. **Blog ve landing SEO metadata**  
   - Blog: BLOG_LANGS_PREMIUM zaten 9 dil; metadata sistemi aynı.  
   - Landing: LANDING_META ve get_landing_ui 9 dil için doldurulacak.  
   - SEO landing: Yeni dil/slug eklenirken get_seo_landing_meta ve get_seo_landing_content ile uyumlu eklemek.

8. **İç linkler**  
   - SPA’da “Blog” linkini `/{current_locale}/blog` yap (opsiyonel ama önerilen).  
   - Footer/nav’de pricing, how-it-works mevcut haliyle bırakılabilir (zaten crawl edilebilir).

9. **Testler**  
   - test_sitemap: 9 dil blog index, 9 dil landing (veya yeni LANDING_ROUTES), SEO landing, how-it-works, legal.  
   - Manuel: Her dilde bir landing + blog sayfası açıp canonical ve hreflang’in doğru olduğunu kontrol et.

10. **Dokümantasyon**  
    - Bu plan uygulandıktan sonra DEPLOY.md veya README’de “Çok dilli SEO” bölümü güncellenebilir; sitemap ve hreflang kuralları özetlenir.

---

## 11. Kısa özet tablo

| Bileşen | Mevcut | Hedef (9 dil) | Değişiklik türü |
|---------|--------|----------------|-----------------|
| Landing routes | 5 (tr, en, en-ca, de, it) | 9 (+ es, fr, he, hi, ar) | Yeni route + i18n |
| Landing hreflang | 5 + x-default | 9 + x-default | Liste ve enjeksiyon |
| Blog | 9 dil | 9 dil | Kontrol / test |
| SEO landing | TR, EN, DE | İsteğe bağlı genişletme | Yeni slug + hreflang |
| How-it-works | 6 dil ?lang= | 9 dil veya 6’da kal | hreflang listesi / içerik |
| Legal | 6 dil ?lang= | 9 veya 6 | hreflang listesi |
| Pricing | 4 hreflang | 9 + x-default | Şablon |
| Kurumsal | hreflang yok | 9 hreflang | Şablon + context |
| Sitemap | LANDING_ROUTES + blog + … | Aynı kaynak, 9 dil | Otomatik |
| Canonical | Doğru | Aynı | Doğrulama |

Bu doküman sadece analiz ve plandır; kod değişikliği bir sonraki adımda uygulanacaktır.
