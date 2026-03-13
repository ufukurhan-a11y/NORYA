# Blog İkinci Dalga İçerikleri — Özet

Bu doküman, NoryaAI blog ikinci dalga (long-tail, görselli, SEO odaklı) içeriklerinin eklenmesini ve görsel/marka tutarlılığını özetler.

---

## 1. Eklenen / düzenlenen dosyalar

| Dosya | Değişiklik |
|-------|------------|
| `app/blog_i18n.py` | B12 low ve Vitamin D interpret makalelerine he, hi, ar dilleri eklendi. Demir eksikliği, ALT/AST makalelerine he, hi, ar eklendi. Platelets kapak görseli `vitamin-b12-hero.png` olarak farklılaştırıldı (CBC ile aynı görsel kullanılmıyor). Tüm ikinci dalga makaleler ARTICLES listesine kayıtlı. |
| `docs/BLOG-SECOND-WAVE-SUMMARY.md` | Bu özet doküman eklendi. |

**Not:** Urea, platelets, WBC/RBC, fasting glucose, HbA1c meaning, cholesterol types makaleleri şu an tr, en, de, fr, it, es dillerinde tam; he, hi, ar için isteğe bağlı genişletme yapılabilir (aynı yapı ile).

---

## 2. Hangi dillerde hangi içeriklerin eklendiğı

- **Tüm premium diller (tr, en, de, fr, it, es, he, hi, ar):**
  - B12 düşüklüğü ne anlama gelir?
  - D vitamini sonucu nasıl yorumlanır?
  - Demir eksikliği hangi kan değerlerinde görülür?
  - ALT ve AST yüksekliği neyi gösterir?

- **TR, EN, DE, FR, IT, ES (6 dil):**
  - Üre yüksekliği ne anlama gelir?
  - Trombosit yüksekliği ve düşüklüğü ne demek?
  - WBC, RBC, HGB, HCT nasıl okunur?
  - Açlık kan şekeri sonucu nasıl değerlendirilir?
  - HbA1c sonucu ne anlama gelir?
  - Kan tahlilinde kolesterol türleri nasıl anlaşılır?

---

## 3. Örnek başlık + slug + meta description (dil bazlı)

### Türkçe (örnek 3)
- **B12 düşüklüğü ne anlama gelir?**  
  Slug: `b12-dusuklugu-ne-anlama-gelir`  
  Meta: B12 düşüklüğü nedenleri, referans aralıkları ve ne zaman doktora gidilmeli. Sadece bilgilendirme amaçlı.

- **Demir eksikliği hangi kan değerlerinde görülür?**  
  Slug: `demir-eksikligi-hangi-kan-degerlerinde-gorulur`  
  Meta: Ferritin, hemoglobin ve MCV ile demir eksikliği. Bilgilendirme amaçlı.

- **ALT ve AST yüksekliği neyi gösterir?**  
  Slug: `alt-ve-ast-yuksekligi-neyi-gosterir`  
  Meta: Karaciğer enzimleri ALT ve AST yüksekliği nedenleri. Bilgilendirme amaçlı.

### Almanca (örnek 3)
- **Was bedeutet ein niedriger Vitamin-B12-Wert?**  
  Slug: `was-bedeutet-niedriger-vitamin-b12-wert`  
  Meta: Ursachen für niedriges B12, Referenzbereiche und wann zum Arzt. Nur zur Information.

- **Eisenmangel im Blutbild erkennen**  
  Slug: `eisenmangel-im-blutbild-erkennen`  
  Meta: Ferritin, Hämoglobin und MCV bei Eisenmangel. Nur zur Information.

- **Was bedeuten erhöhte ALT- und AST-Werte?**  
  Slug: `was-bedeuten-erhoehte-alt-und-ast-werte`  
  Meta: Ursachen für erhöhte Leberenzyme ALT und AST. Nur zur Information.

### İngilizce (örnek 3)
- **What does a low vitamin B12 level mean?**  
  Slug: `what-does-low-vitamin-b12-mean`  
  Meta: Causes of low B12, reference ranges, and when to see a doctor. For information only.

- **How to spot iron deficiency in blood results**  
  Slug: `how-to-spot-iron-deficiency-in-blood-results`  
  Meta: Ferritin, haemoglobin and MCV in iron deficiency. For information only.

- **What do high ALT and AST levels mean?**  
  Slug: `what-do-high-alt-and-ast-levels-mean`  
  Meta: Causes of high ALT and AST liver enzymes. For information only.

---

## 4. Görsel sisteminde yapılanlar

- **Kapak görselleri:** Her ikinci dalga makalesi için farklı kapak görseli atandı (mevcut `static/images/blog/` varlıkları kullanıldı):
  - B12 low → `vitamin-b12-hero.png`
  - Vitamin D interpret → `vitamin-d-hero.png`
  - Demir eksikliği → `ferritin-hero.png`
  - ALT/AST → `crp-hero.png`
  - Üre → `creatinine-egfr-hero.png`
  - Trombosit → `vitamin-b12-hero.png` (CBC’den farklı: CBC `how-to-read-blood-test-results.png`)
  - WBC/RBC/HGB/HCT → `how-to-read-blood-test-results.png`
  - Açlık kan şekeri → `hba1c-hero.png`
  - HbA1c sonucu → `hba1c-hero.png`
  - Kolesterol türleri → `ldl-hdl-hero.png`

- **Norya marka imzası:** Detay şablonunda (`blog/detail.html`) kapak görseli üzerinde sağ alt köşede “N” + “NoryaAI” rozeti kullanılıyor; tüm makalelerde aynı marka imzası geçerli. Görsel dosyalarının içine ikon gömülmedi; overlay şablon ile uygulanıyor (CLS riski olmadan, tutarlı konum).

- **Alt metinler:** Her makale için `cover_alt` ilgili dilde tanımlı (ör. TR: "B12 vitamini kan tahlili — Norya", EN: "Vitamin B12 blood test — Norya").

---

## 5. Farklı görsellerin yönetimi

- Her makale `Article` nesnesinde `cover_image` ile tek bir kapak yoluna bağlı.
- Aynı görsel dosyası farklı makalelerde kullanılabiliyor (örn. hba1c-hero hem açlık kan şekeri hem HbA1c sonucu makalesinde); konuya göre farklı görseller tercih edildi (vitamin, karaciğer, böbrek, kan sayımı, glukoz, kolesterol).
- Yeni görsel eklemek için: `static/images/blog/` altına yeni dosya eklenip `cover_image` bu dosyaya güncellenir. Norya ikonu şablondaki overlay ile kalır; görsellerde ayrıca ikon eklenmesi gerekmez.

---

## 6. Mobil uyum

- Mevcut blog şablonları mobil uyumlu bırakıldı; ek bir tasarım değişikliği yapılmadı.
- `blog/index.html` ve `blog/detail.html` içinde:
  - Kapak ve kart görselleri `clamp(220px, 50vw, 320px)` benzeri kurallarla sınırlandı.
  - Görsellerde `loading="lazy"`, `width`/`height` ve `sizes` kullanılıyor; CLS önleniyor.
- İkinci dalga içerikleri bu mevcut yapıyı kullanıyor; ek mobil düzeltme yapılmadı.

---

## 7. İç link ve SEO tarafında güçlendirmeler

- **İç linkler:** Her makalenin disclaimer/CTA bölümünde:
  - `/analyze` (analiz başlat),
  - Dil bazlı landing/blog linkleri (örn. TR: `/tr/kan-tahlili-sonucu`, `/tr/hemogram-sonucu`, EN: `/en/blood-test-results`, `/en/understand-lab-results`, DE: `/de/blutwerte-verstehen`, `/de/laborwerte-verstehen`),
  - `/pricing` (kolesterol türleri gibi ilgili makalelerde) kullanılıyor.
- **SEO:** Her makale için dil bazlı `seo_title`, `seo_description`, benzersiz `slug` ve `cover_alt` tanımlı. Sitemap ve hreflang mevcut blog altyapısı ile otomatik üretiliyor; routing ve backend değiştirilmedi.

---

## 8. İkinci dalga trafik büyümesi için hazırlık

- İkinci dalga konu kümeleri (B12, D vitamini, demir, ALT/AST, üre, trombosit, WBC/RBC/HGB/HCT, açlık kan şekeri, HbA1c sonucu, kolesterol türleri) aktif dillerde içerik ve slug/meta ile eklendi.
- Tasarım, routing ve backend korundu; mevcut blog altyapısı kullanıldı.
- İçerikler bilgilendirici, teşhis/aşırı vaat yok; her makalede uyarı ve CTA var.
- Görseller konuya göre ayrıldı, Norya marka imzası şablon overlay ile tutarlı uygulanıyor.
- Blog listesi ve detay sayfaları mobil uyumlu ve lazy loading ile performans dostu kaldı.

**Sonuç:** Bloglar ikinci dalga long-tail trafik büyümesi için hazırdır; gerekirse he/hi/ar için kalan 6 makale de aynı yapı ile genişletilebilir.
