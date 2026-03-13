# NoryaAI Canlı İyileştirme — Analiz Raporu

**Tarih:** 13 Mart 2025  
**Amaç:** Siteyi daha güven veren, temiz, profesyonel ve yüksek dönüşüm alacak hale getirmek; dil karışmasını bitirmek; SEO ve satış akışını temizlemek.  
**Kısıt:** Mevcut tasarım/backend/routing/payment/blog altyapısı kırılmadan, kontrollü ve aşamalı değişiklik.

---

## Kısa Genel Değerlendirme

Proje **FastAPI + statik SPA (static/index.html)** yapısında; dil **path** (`/tr`, `/en`, …) ve **server-side enjeksiyon** (`__LANDING_T__`) ile yönetiliyor. Blog, pricing, payment, legal ayrı şablonlarda. **Kritik noktalar:** (1) Aynı sayfada TR/EN karışan **fallback metinler** ve **i18n eksik/yanlış eşleşmeler**, (2) **index.html** varsayılan başlık/açıklama Türkçe iken `lang="en"` ve `og:locale="en_US"` — Google için tutarsız, (3) Örnek rapor ve özellik kartlarındaki **sabit İngilizce** (data-i18n var ama fallback EN), (4) Pricing/payment tarafında **tek URL + fallback key** (“failed_pricing”, “Pricing”) profesyonellik hissini düşürüyor. Çok dilli SEO altyapısı (sitemap, hreflang, canonical) büyük ölçüde doğru; eksikler dokümandaki planla uyumlu (ES, FR, HE, HI, AR landing/hreflang). Yorumlar bölümü i18n ile destekleniyor ama **“Trusted Reviews”** gibi tek başlık TR sayfada İngilizce kalabiliyor; sağlık uyarıları ve güven metinleri dağınık. **Mobil** için CSS’te overflow/safe-area düzenlemeleri mevcut; risk alanları aşağıda.

---

## A) KRİTİK SORUNLAR

### 1. Dil karışması

| Konum | Sorun | Örnek |
|-------|--------|--------|
| **static/index.html** (fallback içerik) | data-i18n fallback’leri: bazıları TR, bazıları EN; aynı sayfa DOM’da karışık dil. | `feature_5_desc`: "Track changes over time…" (EN); `feature_6_desc`: "Practical lifestyle…" (EN); `enterprise_infra_label`: "Trusted Infrastructure" (EN). Diğer kartlar TR. |
| **Örnek rapor kartı** (health-preview) | Başlık ve madde listesi sabit; data-i18n yok. | "Örnek rapor", "Norya Health Report", "• Health Score", "• Diyabet Riski", "• Kalp Riski" — aynı blokta TR+EN. |
| **Hero başlık tutarsızlığı** | index.html fallback: "60 Saniyede"; landing_i18n TR: "Dakikalar İçinde". | Sunucu TR için "Dakikalar" gönderir; statik HTML/erken render "60 Saniyede" gösterir; JS sonrası dil değişince tutarsızlık. |
| **customer_section_badge** | TR locale’de bile "Trusted Reviews" (EN) görünebilir. | landing_i18n TR: "Güvenilir Yorumlar"; index inline tr: "Güvenilir Yorumlar"; EN: "Trusted Reviews". Fallback HTML’de "Trusted Reviews" yazıyor. |
| **Pricing şablonu** | `t.get("brand_trust_line", "Clinical-style blood test reports.")` — fallback EN. | Dil yüklenmezse İngilizce cümle çıkar. |
| **Verify sayfası** | Sabit "Blood Test Report Verification" (main.py). | brand_sub tek dil. |

### 2. Test / staging / ham UI metinleri

| Konum | Sorun |
|-------|--------|
| **app/main.py** | Yorum: "Şimdilik ücretsiz kullanıcı da premium grafikleri ve PDF'i görsün (test için; sonra False yapın)" — iş mantığı test amacıyla açık. |
| **app/main.py** | `/debug/rate-test` endpoint’i — canlıda kapatılmalı veya korumalı. |
| **main.py** | "Tag yüklü olmalı. Realtime test için gizli sekmede…" — HTML içinde kullanıcıya çıkmaması için kontrol edilmeli. |
| **PayTR test_mode** | production’da `test_mode = "0"` yapılıyor; dokümante edilmiş. Görünür “test” etiketi yok; sadece mantık kontrolü. |

### 3. Güven zedeleyen veya dağınık başlık/bölümler

- **Örnek rapor** bölümü: "Örnek rapor" + "Norya Health Report" + karışık TR/EN madde listesi — tek dilde değil.
- **"Trusted Infrastructure"** (EN) TR sayfada kalabiliyor (fallback).
- **HIPAA:** Metin rozeti kullanılıyor (TRUST_SECTION_FIX); açıklama "Norya HIPAA kapsamında kayıtlı değildir" — doğru ama yer yer "HIPAA uyumlu" gibi abartılı algı yaratmamak için ton tutarlı olmalı.
- **Verify sayfası** tamamen EN ("Blood Test Report Verification") — dil seçimi yok.

### 4. SEO açısından problemli alanlar

- **static/index.html (ham):** `<html lang="en">`, `<title>` ve `<meta name="description">` Türkçe, `og:locale` "en_US". Root `/` için sunucu enjeksiyonu yok; dil path’e göre (`/tr`, `/en`…) enjekte ediliyor. **Root (/) için:** title/description/hreflang dil ile değişmiyor; varsayılan TR metin + en → Google tutarsız sinyal.
- **Pricing hreflang:** Sadece tr, de, en, x-default; ES, FR, IT vb. yok (docs/COK-DILLI-TEKNIK-SEO-ANALIZ-VE-PLAN.md ile uyumlu).
- **Landing hreflang:** ES, FR, HE, HI, AR eksik (mevcut dokümanla aynı tespit).

### 5. Pricing ve payment tarafında profesyonellik

- **pricing.html:** Başlık `t.get("pricing_page_title", t.get("failed_pricing", "Pricing"))` — "failed_pricing" anahtarı hata/fallback çağrışımı yapıyor; key adı ve kullanım sadece fallback için netleştirilmeli.
- **Tek URL `/pricing`:** Tüm diller aynı URL; dil cookie/query ile. Hreflang’de dil parametreli URL yok (örn. `?lang=tr`); arama motorları için dil sinyali zayıf.
- **PayTR:** test_mode production’da 0; akış dokümante. Ödeme sayfası metinleri pay_i18n ile çok dilli; "brand_trust_line" gibi alanlar var — tutarlı kullanıldığında profesyonel.

---

## B) HIZLI KAZANÇ SAĞLAYACAK DÜZELTMELER

### Dönüşüm (5)

1. **Hero CTA netliği:** "Hemen Al — Yıllık Plan" / "Örnek Raporu Gör" butonlarının görünürlük ve metin tutarlılığı; dil değişince hep doğru dilde CTA.
2. **Örnek rapor kartı:** Tüm metinleri data-i18n + landing_i18n ile tek dile çekmek; "Health Score" vb. çevirileri eklemek.
3. **Pricing sayfası:** "failed_pricing" yerine sadece "pricing_page_title" (ve gerekirse genel "pricing" key) kullanmak; fallback metni nötr/profesyonel.
4. **Sticky/drawer CTA:** "Fiyatları Gör — Satın Al" / "View pricing — Buy" gibi tek mesaj; mobil drawer’da aynı dil.
5. **Blog → analiz/pricing CTA:** Blog sonu CTA linklerinin dil ve hedef sayfa ile uyumu (mevcut yapı korunup metin/URL dil eşleşmesi).

### Güven (5)

1. **Trust bölümü dil tutarlılığı:** customer_section_badge, enterprise_infra_label ve özellik kartı açıklamalarının fallback’lerini sayfa diline göre yapmak (TR sayfada TR fallback).
2. **Örnek rapor bölümü:** "Norya Health Report" ve madde listesini tam i18n; tek dilde görünmesi.
3. **Sağlık uyarısı / disclaimer:** "Bu rapor teşhis yerine geçmez" benzeri ifadelerin tek bir yerde, görünür ve dil ile uyumlu olması.
4. **Verify sayfası:** En azından brand_sub ve temel metinlerin dil parametresine göre (veya hreflang/canonical ile) sunulması.
5. **HIPAA/güvenlik metni:** Tüm dillerde aynı netlikte (“uyumlu ilkeler / kayıtlı değil”) kullanımı.

### SEO (5)

1. **index.html varsayılan head:** Root için de sunucudan title/description/og:locale enjeksiyonu veya statik olarak en azından lang + og:locale tutarlılığı (ör. varsayılan x-default = en ise title/description da EN).
2. **Landing hreflang:** ES, FR, HE, HI, AR eklenmesi (route + LANDING_META + hreflang bloğu).
3. **Pricing hreflang:** Tüm payment dilleri (tr, en, de, fr, it, es) için hreflang linkleri; URL aynı kalabilir, `?lang=` ile.
4. **Blog CTA sayfaları:** Blogdan /analyze veya /pricing’e giden linklerde dil parametresi veya locale path (mevcut yapıya uygun).
5. **Sitemap:** Yeni landing dilleri ve pricing/legal varyantları (gerekirse) sitemap’e eklenmesi.

---

## C) UYGULAMA SIRASI

### Faz 1 — Hemen yapılacak kritik temizlik

- **Dil karışması:** index.html’deki feature_5_desc, feature_6_desc, enterprise_infra_label fallback’lerini TR yapmak (veya locale’e göre doğru fallback).
- **Örnek rapor kartı:** "Örnek rapor", "Norya Health Report", "Health Score", "Diyabet Riski" vb. tüm metinleri data-i18n + landing_i18n (veya mevcut JSON) ile bağlamak; aynı blokta tek dil.
- **Hero tutarlılık:** landing_i18n TR "Dakikalar" ile index fallback "60 Saniyede" uyumu — tek kaynak (sunucu) kullanılıyorsa fallback’i "Dakikalar" yapmak veya tersini standartlaştırmak.
- **customer_section_badge:** HTML fallback’ini "Güvenilir Yorumlar" (TR) yapmak; EN sayfada EN kalacak şekilde i18n zaten var.
- **Pricing fallback:** "failed_pricing" kullanımını sadece gerçek hata durumunda bırakıp başlık için "pricing_page_title" + tek nötr fallback ("Fiyatlandırma" / "Pricing").
- **Test/staging:** /debug/rate-test’i production’da devre dışı veya auth ile korumak; test amaçlı yorumları kısaltmak veya kaldırmak.

### Faz 2 — Güven ve dönüşüm iyileştirmeleri

- Trust bölümü ve enterprise_infra metinlerinin tüm dillerde eksiksiz ve tutarlı olması.
- Verify sayfası dil desteği (veya en azından brand_sub i18n).
- Sağlık uyarısı/disclaimer’ın tek bir şablon/blokta toplanması ve her dilde aynı mesaj gücü.
- Yorumlar/testimonial metinlerinin doğal ve dil bazlı kontrolü (zaten i18n var; ton gözden geçirme).
- Pricing/payment sayfalarında "brand_trust_line" ve güven satırının tüm dillerde görünür ve tutarlı kullanımı.

### Faz 3 — Çok dilli SEO ve blog büyüme

- Landing: ES, FR, HE, HI, AR route + meta + hreflang (docs planıyla uyumlu).
- Pricing/legal/how-it-works hreflang genişletmesi.
- Blogdan satış/analiz sayfalarına CTA linklerinde dil/locale tutarlılığı.
- Sitemap güncellemesi (yeni URL’ler).

---

## D) DOSYA VE BİLEŞEN BAZLI YAKLAŞIM

| Dosya / bileşen | Yapılacak (özet) |
|------------------|-------------------|
| **static/index.html** | Fallback metinleri (feature_5/6_desc, enterprise_infra_label, customer_section_badge, hero_title) tek dil veya locale’e uyumlu; örnek rapor kartı tüm metinler data-i18n; varsayılan &lt;title&gt;/meta/hreflang (root için) tutarlı. |
| **app/landing_i18n.py** | Yeni key’ler: örnek rapor kartı (sample_report_label, sample_report_title, sample_report_bullet_1..5 vb.); hero_title ile index fallback uyumu; TR’de "Dakikalar" standart. |
| **app/main.py** | Root (/) için title/meta/hreflang enjeksiyonu veya yönlendirme politikası; _landing_response hreflang’e ES, FR, HE, HI, AR ekleme (Faz 3); /debug/rate-test kapatma/koruması; verify sayfası brand_sub i18n. |
| **app/templates/pricing.html** | Başlık için failed_pricing fallback kaldırma/nötrleştirme; brand_trust_line fallback; hreflang genişletme (Faz 3). |
| **app/pay_i18n.py** | Verify sayfası metinleri (brand_sub vb.) dil bazlı kullanım; pricing sayfası key adları (failed_pricing sadece hata). |
| **app/templates/verify.html** | brand_sub ve ilgili metinlerin şablonda t dilinden gelmesi. |
| **app/blog_i18n.py / app/templates/blog/** | Blog CTA buton/link metinleri ve href’lerin current_lang ile uyumu (mevcut yapı korunur). |
| **Inline JSON (index.html)** | tr/en/... bloklarında örnek rapor ve feature_5/6, enterprise_infra için eksik çevirilerin eklenmesi; customer_section_badge TR’de "Güvenilir Yorumlar". |

---

## E) RİSKLER

| Alan | Risk | Önlem |
|------|------|--------|
| **Routing** | Root `/` ile `/{locale}` çakışması; blog `/{lang}/blog` ile landing path çakışması. | Sadece head enjeksiyonu veya redirect; yeni route eklemeden mevcut sıra korunur. |
| **Localization** | __LANDING_T__ ile client-side JSON farklı key/çeviri içerirse sayfa yarı TR yarı EN kalır. | Fallback ve server UI aynı key setini kullanmalı; tek kaynak (landing_i18n) referans. |
| **Metadata** | Canonical/hreflang yanlış enjekte edilirse duplicate content veya yanlış dil ataması. | _inject_canonical ve hreflang regex’lerinin path/locale ile testi; sitemap ile çapraz kontrol. |
| **Payment** | PayTR hash, success/fail URL, test_mode değişirse ödeme bozulur. | Sadece metin/i18n değişikliği; hash ve URL mantığına dokunulmaz. |
| **Blog** | list_articles_for_lang, get_article, slug matrisi değişirse 404 veya yanlış dil. | Sadece CTA link ve metin; blog API ve slug yapısı aynı kalır. |
| **Layout / mobil** | index.html’de yeni class veya DOM değişikliği taşma/bozulma yapabilir. | Sadece metin/i18n değişiklikleri; grid/flex yapısı değiştirilmez; mobil CSS mevcut kurallarla uyumlu kalır. |

---

## Önce Hangi 3 İş Yapılsın?

1. **Dil karışmasını kaldır (index.html + örnek rapor)**  
   feature_5_desc, feature_6_desc, enterprise_infra_label fallback’lerini TR yapıp; örnek rapor kartındaki tüm sabit metinleri data-i18n + landing_i18n (ve inline JSON) ile bağlamak. Böylece aynı sayfada tek dil görünür, güven ve profesyonellik artar.

2. **Hero ve pricing başlık/fallback tutarlılığı**  
   Hero başlığında "60 Saniyede" vs "Dakikalar" tek kaynağa indirgemek; pricing sayfasında "failed_pricing" yerine net başlık key’i ve nötr fallback kullanmak. Hem SEO hem ilk izlenim düzelir.

3. **Root ve varsayılan head tutarlılığı (SEO)**  
   Root (/) için title/description/og:locale’ü dil ile uyumlu hale getirmek (sunucu enjeksiyonu veya varsayılanı EN yapıp x-default ile uyumlu hale getirmek). Böylece Google’da dil sinyali netleşir.

Bu üçü yapıldıktan sonra Faz 2 (güven/testimonial/verify) ve Faz 3 (hreflang genişletme, blog CTA) aşamalı ilerletilebilir.
