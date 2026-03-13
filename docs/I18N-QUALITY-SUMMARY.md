# NoryaAI i18n Kalite Özeti — Almanca Seviyesinin Tüm Dillere Yayılması

Bu doküman, landing, pricing, payment, how-it-works, blog, footer, trust ve legal alanlarında Almanca referans alınarak yapılan metin/i18n/SEO iyileştirmelerinin özetidir.

---

## 1. Düzenlenen Dosyalar

| Dosya | Değişiklik kapsamı |
|-------|--------------------|
| `app/landing_i18n.py` | EN, IT, TR hero/trust/FAQ/pricing/meta; LANDING_META (tr, en, it) SEO |
| `app/base_i18n.py` | ES dili eklendi; FR, IT, TR footer_tagline/title_suffix iyileştirildi |
| `app/how_it_works_i18n.py` | IT, FR, ES dilleri eklendi; EN, TR hero_sub/meta hafif sadeleştirme |
| `app/legal_i18n.py` | FR, ES, IT, HE, AR, HI, EL, CS, SR footer_desc, footer_disclaimer, nav_kvkk |
| `app/blog_i18n.py` | EN, TR, FR, IT, ES, HE, HI hero_title/desc, CTA, seo_title, meta_description, end_cta |
| `app/pay_i18n.py` | EN: pricing_page_title, pricing_meta_description, pay_meta_description, pay_trust_line, trust_*; FR, IT, ES: pricing meta + pay_trust_line |
| `app/main.py` | How-it-works dil açıklaması (it, fr, es eklendi) |

---

## 2. Hangi Dillerde Hangi Ana Metin Alanları Düzeltildi?

- **English (en):** Landing hero_sub, hero_title, hero_desc, trust badges, CTA, FAQ, pricing_eur, drawer_trust_meta, meta_title/meta_description. Pay: pricing_page_title, pricing_meta_description, pay_trust_line, trust_*. Blog: hero, CTA, seo_title, meta_description, end_cta.
- **Türkçe (tr):** Landing hero_sub, hero_title, hero_desc, trust badges, CTA, FAQ, pricing_eur, drawer_trust_meta, meta_title/meta_description. Base footer_tagline, title_suffix. Blog: hero, CTA, seo_title, meta_description, end_cta.
- **Italiano (it):** Landing hero_sub, hero_title, hero_desc, trust badges, CTA, FAQ, pricing_eur, drawer_trust_meta, meta_title/meta_description. Base footer_tagline, title_suffix. How-it-works: tam dil desteği (yeni). Legal footer_desc/disclaimer. Blog: hero, CTA, seo_title, meta_description, end_cta. Pay: pricing meta, pay_trust_line.
- **Español (es):** Base UI eklendi (nav, footer, cta_analyze, title_suffix). How-it-works: tam dil desteği (yeni). Legal footer_desc/disclaimer. Blog: hero, CTA, seo_title, meta_description, end_cta. Pay: pricing meta, pay_trust_line.
- **Français (fr):** Base footer_tagline, title_suffix. How-it-works: tam dil desteği (yeni). Legal footer_desc/disclaimer, nav_kvkk. Blog: hero, CTA, seo_title, meta_description, end_cta. Pay: pricing meta, pay_trust_line.
- **Deutsch (de):** Referans dil; metinler aynı bırakıldı.
- **עברית (he):** Legal footer_desc, footer_disclaimer, nav_kvkk. Blog: hero, CTA, seo_title, meta_description, end_cta.
- **हिन्दी (hi):** Legal footer_desc, footer_disclaimer, nav_kvkk. Blog: hero, CTA, seo_title, meta_description, end_cta.
- **العربية (ar):** Legal footer_desc, footer_disclaimer, nav_kvkk.
- **Ελληνικά (el), Čeština (cs), Srpski (sr):** Legal footer_desc, footer_disclaimer, nav_kvkk.

---

## 3. Önce / Sonra Örnekleri (Dil Bazlı)

### English
| Alan | Önce | Sonra |
|------|------|--------|
| hero_sub | Clinical Biomarker Platform | Lab results explained in plain language. Not a diagnosis—just clear guidance for your next doctor visit. |
| meta_title | Norya — Reliable AI Blood Test Analysis | Norya — Understand Your Blood Test Results in Minutes \| Lab Report Explained |
| trust_badge_kvkk_gdpr | KVKK & GDPR | GDPR compliant |
| pricing_eur | Prices are shown in your local currency based on your location. | Prices in your currency, transparent and no hidden fees. |
| drawer_trust_meta | KVKK & GDPR · 256-bit SSL · Secure payment | GDPR compliant · SSL encrypted · Secure payment (PayTR) |

### Türkçe
| Alan | Önce | Sonra |
|------|------|--------|
| hero_sub | Clinical Biomarker Platform | Laboratuvar sonuçları anlaşılır dilde açıklanır. Teşhis değil—sadece hekim görüşmenize hazırlık. |
| hero_title | Kan Tahlilinizi 60 Saniyede Anlayın | Kan Tahlilinizi Dakikalar İçinde Anlayın |
| meta_description | … PDF veya fotoğraf yükleyin, özet rapor ve PDF alın. 9 dilde, gizlilik odaklı. | … referans aralıkları ve önerilerle net rapor alın. KVKK uyumlu, teşhis yok—yalnızca bilgilendirme. 9 dil. |
| trust_badge_ssl | 256-bit SSL | SSL şifreli |
| pricing_eur | Fiyatlar konumunuza göre yerel para biriminde gösterilir. | Fiyatlar kendi para biriminizde, şeffaf ve gizli ücret yok. |

### Italiano
| Alan | Önce | Sonra |
|------|------|--------|
| hero_sub | Clinical Biomarker Platform | Referti di laboratorio spiegati in linguaggio chiaro. Nessuna diagnosi—solo orientamento per la prossima visita. |
| meta_title | Norya — Analisi del sangue con IA affidabile | Norya — Capire le analisi del sangue in pochi minuti \| Referto spiegato |
| trust_badge_kvkk_gdpr | KVKK & GDPR | Conforme GDPR |
| How-it-works | (yoktu, EN fallback) | Tam IT metinleri (hero, steps, trust, CTA, meta) |

### Español
| Alan | Önce | Sonra |
|------|------|--------|
| Base UI | (yoktu, EN fallback) | Nav, footer_tagline, title_suffix, cta_analyze eklendi |
| Legal footer_desc | Herramienta que explica los resultados de análisis de sangre. | Resultados de análisis explicados en lenguaje claro. Solo información — no sustituye el diagnóstico médico. |
| How-it-works | (yoktu) | Tam ES metinleri eklendi |

### Français
| Alan | Önce | Sonra |
|------|------|--------|
| Base footer_tagline | Résultats d'analyses expliqués simplement. Ne remplace pas un avis médical. | Résultats d'analyses expliqués en langage clair. À titre informatif uniquement — pas un diagnostic. |
| Legal footer_disclaimer | Cet outil est à but informatif. Consultez un professionnel de santé pour toute décision médicale. | Contenu à but informatif. Pour toute décision médicale, consultez un professionnel de santé. |
| How-it-works | (yoktu) | Tam FR metinleri eklendi |

### Blog (EN örnek)
| Alan | Önce | Sonra |
|------|------|--------|
| hero_title | AI Blood Test Analysis, Biomarker Guides, and Clear Lab Result Explanations | Blood Test Results Explained: Biomarker Guides and Clear Lab Interpretations |
| meta_description | Explore Norya AI blog for blood test interpretation guides… | Blood test interpretation guides and biomarker articles: ferritin, CRP, thyroid, cholesterol. Clear, educational—for your next doctor visit. |
| hero_cta_caption | Privacy-first, clear reports in minutes. | GDPR compliant. Clear reports in minutes. |

### Pay (EN örnek)
| Alan | Önce | Sonra |
|------|------|--------|
| pricing_page_title | (yoktu, "Pricing" fallback) | Pricing: Single Analysis & Subscription \| Understand Your Blood Test |
| pricing_meta_description | (yoktu) | Clear pricing for blood test analysis: single report or subscription. Secure payment, report in minutes. GDPR compliant. |
| pay_trust_line | 256-bit SSL · PayTR 3D Secure · Your card details are not stored | SSL encrypted · PayTR 3D Secure · Card details are not stored with us |

---

## 4. Karışık / Fallback Metin Sorunları

- **Çözülen:**  
  - **Español:** Base template’te dil “es” iken artık İngilizce fallback yerine `base_i18n` içindeki ES nav/footer/cta metinleri kullanılıyor (ES eklendi).  
  - **Italiano, Français, Español:** How-it-works sayfasında `?lang=it`, `?lang=fr`, `?lang=es` ile artık o dilde tam metin gösteriliyor; önceden EN fallback vardı.  
  - **Pricing/Pay:** EN, FR, IT, ES için `pricing_page_title` ve `pricing_meta_description` tanımlandı; böylece pricing sayfasında dil bazlı doğru SEO başlık/açıklama kullanılıyor, yanlış dilde genel “Pricing” kalmıyor.

- **Korunan:** Hi ve He pay/pricing için mevcut mantık aynı: `get_pay_ui("hi")` / `get_pay_ui("he")` EN sözlüğünü kullanıyor; EN metinleri güncellendiği için bu diller de güncel ve tutarlı metin görüyor.

---

## 5. SEO Title / Meta İyileştirmeleri

- **Landing (tr, en, it):**  
  - Her dilde **benzersiz** `meta_title` ve `meta_description`: arama niyeti odaklı (örn. “understand blood test / lab report / referto spiegato”), “teşhis yok / no diagnosis / nessuna diagnosi” vurgusu, GDPR/KVKK uyumu kısa ifade.  
  - Og:locale zaten vardı; metinler og:title/og:description ile uyumlu kullanılabilecek şekilde bırakıldı.

- **Blog:**  
  - Tüm BLOG_UI dillerinde (en, tr, de, fr, it, es, he, hi) `seo_title` ve `meta_description` diline özel, arama niyetiyle uyumlu (blood test results explained, kan tahlili sonuçları açıklaması, résultats expliqués, referti spiegati, resultados explicados, תוצאות מוסברות, रिज़ल्ट समझाए गए). Keyword stuffing yok; doğal ve tıklanabilir ifadeler.

- **Pricing/Pay:**  
  - EN, FR, IT, ES (ve zaten var olan DE) için `pricing_page_title` ve `pricing_meta_description` eklendi/güncellendi: “single report / subscription”, “secure payment”, “GDPR/RGPD compliant”, “report in minutes” gibi niyet odaklı, yerel dilde cümleler.

- **How-it-works:**  
  - IT, FR, ES için yeni meta_title / meta_description eklendi; EN ve TR mevcut yapı korunarak sadeleştirildi. Her dilde “3 steps / 3 passi / 3 étapes / 3 pasos” ve “no diagnosis” mesajı tutarlı.

---

## 6. Tone ve Locale Tutarlılığı

- **Tone (Almanca referans):**  
  - Tüm dillerde teşhis vaadi yok; “no diagnosis / not a substitute / only information / eğitim amaçlı / à titre informatif / solo informativo” ifadeleri korundu veya eklendi.  
  - Trust metinleri yerel: DSGVO (DE), GDPR (EN), RGPD (FR), Conforme GDPR (IT), Cumple GDPR (ES), KVKK (TR).  
  - CTA’lar kısa ve net: “Start analysis”, “Analizi Başlat”, “Avvia analisi”, “Lancer l'analyse”, “Iniciar análisis”.

- **Locale:**  
  - Aynı sayfada tek dil kullanımı korundu; dil seçimine göre ilgili sözlük (landing, base, pay, blog, legal, how_it_works) tek kaynak.  
  - RTL (ar, he): Sadece legal UI metinleri güncellendi; mevcut RTL yapı ve sıralama bozulmadı.  
  - Plan isimleri ve kısa açıklamalar pay_i18n’de zaten dil bazlı; EN/DE/FR/IT/ES trust ve pricing metinleri güncellendi, plan adları doğal kalmaya devam etti (Single analysis, Einzelanalyse, Analyse unique, Analisi singola, vb.).

Bu özet, yalnızca metin/i18n/SEO tarafında yapılan değişiklikleri kapsar; tasarım, component yapısı, routing ve backend mantığı değiştirilmedi.
