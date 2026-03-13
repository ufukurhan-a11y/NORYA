# Blog Konu 1: Globulin High or Low — Teslim Dokümanı

**Slug:** `globulin-high-or-low`  
**Konu:** Globulin High or Low Meaning  
**9 dil:** TR, EN, ES, DE, FR, IT, HE, HI, AR

---

## 1. Meta veriler (9 dil)

| Alan | TR | EN | ES | DE | FR | IT | HE | HI | AR |
|------|----|----|----|----|----|----|----|----|-----|
| **title** | Globulin yüksek veya düşük ne anlama gelir? | Globulin high or low: what it means | Globulina alta o baja: qué significa | Globulin zu hoch oder zu niedrig: Was bedeutet das? | Globuline haute ou basse : qu'est-ce que ça indique ? | Globuline alte o basse: cosa significa? | גלובולין גבוה או נמוך: מה המשמעות? | ग्लोब्युलिन हाई या लो का क्या मतलब? | الغلوبولين مرتفع أو منخفض: ماذا يعني؟ |
| **slug** | globulin-high-or-low | globulin-high-or-low | globulin-high-or-low | globulin-high-or-low | globulin-high-or-low | globulin-high-or-low | globulin-high-or-low | globulin-high-or-low | globulin-high-or-low |
| **category** | Biyobelirteçler | Biomarkers | Biomarcadores | Biomarker | Biomarqueurs | Biomarcatori | ביומרקרים | बायोमार्कर | المؤشرات الحيوية |
| **read time** | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min |

**Excerpt (kısa özet):**  
- TR: Globulin, total proteinde albümin dışında kalan proteinlerin toplamıdır; yüksek veya düşük nedenleri hekim tarafından albümin ve diğer tahlillerle birlikte değerlendirilir.  
- EN: Globulin is the sum of proteins in blood other than albumin. Causes of high or low are assessed by your doctor together with albumin and other results.  
- (Diğer diller `blog_i18n.py` içinde aynı yapıda.)

**Meta title:** Her dilde: ilgili title + " | Norya Blog"  
**Meta description:** Kısa, bilgilendirme amaçlı; teşhis vaadi yok.

---

## 2. Hero image prompt

**İngilizce prompt (görsel üretimi için):**  
Soft gradient background (light teal to white). Abstract representation of protein balance: two gentle bands or layers suggesting “albumin + globulin” (e.g. one slightly denser, one lighter) without text or literal molecules. Clean medical-infographic style; no faces, no stock-photo people. Subtle immune/protein hint in the background. Premium, calm, trustworthy. Norya teal accent allowed. Distinct from albumin (single droplet) and total protein (generic vial)—focus on “two-part balance”.

**Türkçe kısa:**  
Açık teal–beyaz gradient arka plan. Albumin + globulin hissini veren, iki yumuşak bant/katman; metin veya molekül çizimi yok. Sade, tıbbi-infografik; yüz/stock foto yok. Norya teal vurgu kullanılabilir.

---

## 3. Icon concept

**Konsept:** İki yatay bant veya iki halka (albumin + globulin ayrımını çağrıştıran); oran/denge hissi. Tek damla veya tek hücre değil; “total protein’in iki parçası” fikri. Basit, minimal; pasta grafik veya kesir sembolü kullanılmaz.

---

## 4. Internal links

Makale gövdesinde kullanılan dahili linkler (dile göre aynı yapıda):

- **Total protein:** `/{lang}/blog/total-protein-high-or-low`  
- **Albumin:** `/{lang}/blog/albumin-low-meaning`  

Örnek: TR için `/tr/blog/total-protein-high-or-low`, `/tr/blog/albumin-low-meaning`.  
CTA bölümünde: `/analyze`, `/{lang}/pricing` (ör. `/tr/pricing`, `/en/pricing`).

---

## 5. CTA metni (son blok / disclaimer)

Her dilde “bilgilendirme amaçlı”, teşhis/tedavi yerine geçmez; sonuçları hekimle görüşün. Analyze ve pricing linkleri BLOG_UI + makale disclaimer’ında kullanılıyor. Örnek:

- **TR:** Bilgilendirme amaçlıdır. Sonuçlarınızı hekimle görüşün. [Analiz](/analyze)  
- **EN:** For information only. Discuss your results with a doctor. [Analyze](/analyze)  
- **ES:** Solo informativo. Comenta tus resultados con un médico. [Analizar](/analyze)  
- (DE, FR, IT, HE, HI, AR: `blog_i18n.py` içindeki ilgili disclaimer metinleri.)

---

## 6. Full body yapısı (H2)

Kodda şu an `_make_short_article` ile **2 bölüm** (içerik + disclaimer) kullanılıyor. İsterseniz genişletilebilecek **tam metin yapısı**:

1. **Globulin nedir? / What is globulin?** — Total proteinin albümin dışında kalan kısmı; antikorlar, taşıma proteinleri; tek sonuç teşhis koymaz.  
2. **Globulin yüksek veya düşük çıkarsa / When globulin is high or low** — Yüksek: kronik iltihap, enfeksiyon, karaciğer, bağışıklık/kemik iliği. Düşük: karaciğer işlevi, protein alımı, doğuştan durumlar. Internal link: total protein, albumin.  
3. **Sonuç nasıl yorumlanır? / How is the result interpreted?** — Referans aralığı laboratuvara göre değişir; albümin, total protein, karaciğer, gerekirse elektroforez; belirgin sapma veya şikayette hekime başvuru.  
4. **Sonuçlarınızı netleştirin / Make sense of your results** — Analyze ve pricing’e doğal CTA.  
5. **Uyarı / Disclaimer** — Bilgilendirme amaçlı; teşhis/tedavi yerine geçmez.

Bu 5 bölümün 9 dilde tam metni `blog_i18n.py` için ayrı bir patch ile eklenebilir; şu an kısa 2 bölüm versiyonu yayında.

---

## 7. Yayın öncesi kontrol

- [x] Diller karışmamış (her dil kendi title/excerpt/body ile).  
- [x] Çeviri kokmuyor; yerel ifadeler kullanıldı.  
- [x] Tek bir sonucun tanı koymadığı vurgulandı; doktora yönlendirme var.  
- [x] Mevcut yasaklı konular listesinde globulin yok; çakışma yok.  
- [x] Görsel konsepti: protein dengesi / iki parça; albumin damlası veya total protein vial’dan farklı.  
- [x] CTA doğal; analyze ve pricing linkleri mevcut.

---

## 8. Teknik not

- **Dosya:** `app/blog_i18n.py`  
- **Fonksiyon:** `_article_globulin_high_low()`  
- **Sabit:** `_ARTICLE_GLOBULIN`  
- **Liste:** `ARTICLES` içinde `_ARTICLE_GLOBULIN` eklendi.  
- **Hero görsel yolu:** `/static/images/blog/globulin-hero.png` (görsel henüz eklenmedi; yukarıdaki prompt ile üretilebilir).
