# 30 günlük hızlandırma planı (NoryaAI — SEO & büyüme)

Bu dosya, projede tutarlı takip için **30 günlük / fazlı büyüme planının** özetidir. Ana hedef: Google ve AI cevap motorlarında **blood test interpretation / kan tahlili yorumlama** niyetinde görünürlüğü artırmak; teknik temel + içerik + güven (YMYL) + ölçüm.

> **Not:** Çalışma bazen bu tablo yerine kısa sprint’lere (ör. Day 1–8) veya dil dalgalarına bölündü; aşağıdaki çerçeve “ana harita” olarak kullanılmalıdır.

---

## 0) Nerede kaldık? (güncel durum — 2025-03)

İki paralel izleme var: **orijinal 30 günlük faz tablosu** (üst seviye yol haritası) ve **uygulamada yürütülen sprint günleri** (Day  …). Sprint’te gün numarası ilerledikçe bazı işler **dalga (wave)** olarak 9 dile yayılma şeklinde kapatıldı.

### Sprintte tamamlananlar (özet)

| Sprint günü | Konu | Durum |
| --- | --- | --- |
| Day 1–3 | Para sayfaları, pillar rehberler, ilk biomarker intent (İngilizce odak) | Tamam |
| Day 4 | Trust cluster görünürlük + iç linkler | Tamam |
| Phase 2–4 | Ek İngilizce cluster’lar (ör. ikinci dalga biomarker, metabolic/protein, answer-ready/compare) | Tamam |
| Day 5–7 | Mobil güven, görsel alaka standardı, compare görselleri | Tamam |
| Day 8 | Claim / metrik tutarlılığı + OG uyumu | Tamam |
| Day 9 | Otorite sayfaları (science/press vb.) + CTR odaklı meta | Tamam |
| Day 10 | Blog hub “Start here” + araç sayfalarından para/trust köprüleri | Tamam |
| Day 11 | Blog’da “Quick definitions” (sözlük benzeri keşif) | Tamam |
| Day 12 | Böbrek / karaciğer / elektrolit cluster + hub’da tanımlar | Tamam |
| Day 13 | Seçili sayfalarda FAQ + `FAQPage` / answer-ready katmanı | Tamam |
| Locale fix | Kök `/` locale yönlendirme + locale’siz “Home” / `/#analyze` zincirinin toparlanması | Tamam |
| Day 14 | Kısa intent sayfalarından `explained` / `upload` / `analyzer` money-page köprüleri | Tamam |
| Day 15 | “Normal / hafif / net sapma / acil pattern” mini karşılaştırma blokları | Tamam |
| Day 16–20 | Schema doğruluğu + blog güven yüzeyi; `metabolic-panel-results-explained`; `/en/tools` hub; blog keşif genişlemesi; `urine-acr-microalbumin-meaning` | Tamam (kodda mevcut) |
| Wave 1–3 | Yeni EN-first içeriklerin **tr/de → fr/es/it → he/hi/ar** yayılımı | Sohbet özeti: tamam |
| Day 20 | **ApoB** — 9 dil standalone makale + hub/cluster | Tamam |
| Day 21 | **Lp(a)** — aynı mimari | Tamam |
| Day 22 | **Press** — “Linkable resources” içinde ApoB / Lp(a) EN rehber linkleri | Tamam |
| Day 23 | ApoB/Lp(a) için **sitemap + hreflang/canonical + FAQ schema** spot kontrolü | Tamam |
| Day 24 | **Press** — 98.7% ifadesinin claims kuralına uygun netliği; JSON-LD’de sabit URL yerine şablondan `canonical_url` / `base_url` | Tamam |
| Day 25 | **`llms.txt` / `llms-full.txt`** — güven sayfaları + ApoB/Lp(a) EN keşif linkleri | Tamam |
| Day 26 | Lipid cluster **iç link** (LDL / LDL–HDL / kolesterol türleri → ApoB & Lp(a)); kırık iç link düzeltmesi (`ldl-vs-hdl` slug) | Tamam |
| Day 27 | **Trigliserid** makalesi (`blog_article_triglycerides_content.py`) — 9 dilde LDL / LDL vs HDL + ApoB & Lp(a) köprüsü; eski ` /blog/...` LDL–HDL linklerinin locale’li gerçek slug’lara taşınması | Tamam |
| Day 28 | **PLT** makalesi → MPV iç linkleri: yanlış slug (`mpv-blood-test`) → `mpv-high-or-low` + `/{lang}/blog/`; **Magnezyum (EN)** kalsiyum/potasyum linkleri → `calcium-high-meaning` / `potassium-high-meaning` | Tamam |

**Repo içi hızlı doğrulama:** `/en/blog/metabolic-panel-results-explained`, `/en/blog/urine-acr-microalbumin-meaning`, `/en/tools`, `/en/blog/apob-meaning`, `/en/blog/lpa-meaning`, `/llms.txt` ve `app/main.py` içi LLM metinleri mevcut.

### Orijinal 30 günlük faz tablosu ile ne kadar örtüşüyor?

| Orijinal faz | Pratikte |
| --- | --- |
| Gün 1–3 teknik SEO | Büyük ölçüde tamam (+ sonradan locale kök düzeltmesi) |
| Gün 4–7 money pages | Tamam |
| Gün 8–12 pillar + cluster | Güçlü ilerleme; yeni hub’lar (blog, tools, metabolic panel) eklendi |
| Gün 13–18 long-tail | Sürekli genişletildi (çoklu cluster dalgaları) |
| Gün 19–22 trust/YMYL | Trust sayfaları + makale yüzeyinde güven + claim disiplini |
| Gün 23–26 answer-ready / AI | FAQ, quick answer, mini bloklar, definitions hub |
| Gün 27–30 otorite ve büyütme | **Site içi kısım güçlü; dış otorite (backlink, PR, mention) hâlâ ana büyüme kaldıracı** |

### Sıradaki ne? (Day 29+)

1. **Day 29+ (öneri):** Kalan `href="/blog/..."` (locale’siz) taraması ve cluster içi köprüler; veya yeni yüksek niyetli biomarker sayfası.
2. **Off-page / dış sinyal:** Kaliteli referring domain, marka mention’ları, tool & rehber alıntıları (spam paket backlink değil).
3. **Ölçüm döngüsü:** Search Console’da düşük CTR + yüksek impression sayfalarında title/meta revizyonu.
4. **Operasyon:** Anlamlı commit grupları + deploy.

---

## 1) Fazlı genel tablo (gün aralıkları)

| Faz / gün aralığı | Amaç | Yapılacaklar |
| --- | --- | --- |
| Gün 1–3 | Temel SEO altyapısı | `hreflang`, `canonical`, `sitemap`, `robots`, `llms.txt`, teknik indexlenme, dil yapısı |
| Gün 4–7 | Money page güçlendirme | `blood test interpretation`, AI blood test analyzer, upload blood test results vb. para sayfalarını SEO ve dönüşüm için sertleştirme |
| Gün 8–12 | Pillar content | “How to read blood test results”, CBC rehberi, ana rehberler, geniş intent sayfaları |
| Gün 13–18 | Long-tail cluster | Ferritin, CRP, hemoglobin, TSH, vitamin D, platelet, WBC/RBC/HGB/HCT vb. biomarker içerikleri |
| Gün 19–22 | Trust / YMYL | Methodology, medical review, transparency, security, legal-trust bağlantıları |
| Gün 23–26 | Answer-ready / AI optimizasyonu | FAQ, sample reports, compare pages, kısa net cevap blokları, şema mantığı |
| Gün 27–30 | Otorite ve büyütme | Internal link sistemi, cluster tamamlama, backlink/PR hazırlığı, cite edilebilir içerik |

---

## 2) Ana başlıklar (ne yapılacaktı?)

| Başlık | İçerik |
| --- | --- |
| Teknik SEO | Çok dilli yapı, indexlenme, canonical, hreflang, sitemap |
| İçerik otoritesi | Pillar + cluster + biomarker bazlı içerik ağı |
| Trust | Metodoloji, tıbbi inceleme, şeffaflık, güvenlik, yasal netlik |
| AI platform optimizasyonu | Kısa net cevaplar, FAQPage, answer-ready bloklar |
| Dönüşüm | Upload CTA, sample report, fiyatlandırma / ürün yolunu içerikten bağlama |
| Global büyüme | İngilizce öncelik, sonra diğer dillerde yerelleştirme ve cluster genişletme |

**Özet cümle:** Teknik temel + güçlü İngilizce money pages + biomarker cluster + trust sayfaları + AI-answer-ready yapı + global çok dilli otorite.

---

## 3) Alternatif takvim (haftalık aksiyon listesi)

Daha “günlük iş listesi” formatı:

### 0–3 gün (teknik tamamlama)

- Google Search Console’da property doğrula.
- `sitemap.xml` gönder; indexed / discovered / errors takibi.
- 9 dilde hedef URL’leri kontrol et: canonical, hreflang, 200, indexlenebilirlik.
- Robots ve istenmeyen `noindex` hatası olmadığını doğrula.

### 4–10 gün (sayfa-içi SEO)

Her dil için 2 ana landing (`blood-test-results` / `understand-lab-results` ve yerel karşılıkları):

- Title, meta description, H1 — arama niyetiyle uyumlu.
- İlk ~150 kelime: niyeti doğrudan karşılasın.
- FAQ (3–5 soru), uygun şema.
- İç link: landing ↔ ilgili blog; blog → ana para sayfa.

### 11–20 gün (dil bazlı içerik)

- Dil başına 3 destek içerik örneği: “how to read blood test”, “normal ranges by marker”, “high/low marker meaning”.
- Aynı intent-cluster yapısı: bilgilendirici → blog; dönüşüm → landing.

### 21–30 gün (otorite + ölçüm)

- Hedef dillarda kaliteli dış bağlantı / iş birliği (sağlık, tech, blog).
- CTR: düşük CTR ama yüksek impression sayfalarında title/meta revizyonu.
- Search Console: haftalık rapor (sorgu, ülke, sayfa).

---

## 4) KPI (30. gün sonunda)

- Indexlenen sayfa sayısı (tercihen dil bazlı).
- Top 10’a giren sorgu sayısı (ülke bazlı faydalı).
- Ortalama pozisyon (özellikle yoğun diller).
- CTR değişimi.
- Landing organik giriş ve dönüşüm.

---

## 5) Başlangıç anahtar kelime seti (örnek)

Her dilde 2 ana sorgu ekseninde ilerle:

| Dil | Örnek ana sorgular |
| --- | --- |
| EN | blood test results, understand lab results |
| DE | blutwerte verstehen, laborwerte verstehen |
| FR | comprendre analyse de sang, resultats analyse de sang |
| ES | entender analisis de sangre, resultados analisis de sangre |
| IT | capire analisi del sangue, risultati analisi del sangue |
| TR | kan tahlili sonucu, kan değerleri anlama |
| AR / HI / HE | Yerel karşılıklar (aynı intent) |

---

## 6) Sonraki pratik adımlar (checklist)

- Dil × 2 landing için title/meta önerilerini tek tek `seo_landing_i18n` / şablonlarla hizala.
- Search Console’da haftalık kontrol: **[SEARCH-CONSOLE-HAFTALIK-KONTROL.md](./SEARCH-CONSOLE-HAFTALIK-KONTROL.md)** (performans, dizin, haftada en fazla 3 snippet denemesi).
- Dış sinyal için hazır e-postalar: **[OUTREACH-3-HAZIR-EMAIL.md](./OUTREACH-3-HAZIR-EMAIL.md)**
- Idida ve sayılar için projedeki **[claims consistency](../.cursor/rules/claims-consistency.mdc)** kuralına uy (tek canonical metrik seti).

Bu plan, sohbette üretilen **30 günlük hızlandırma** çerçevesinin repoda kalıcı kopyasıdır; ilerleme notlarını buraya veya ayrı bir “durum” satırına ekleyerek güncel tutabilirsiniz.
