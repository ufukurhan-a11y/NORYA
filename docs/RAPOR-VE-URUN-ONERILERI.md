# Rapor ve Ürün — Eklenebilecek Öneriler

Rapor şu an çok iyi durumda. Aşağıdaki fikirler hem PDF’i hem ürünü bir adım ileri taşıyabilir; istediğiniz maddeleri seçip uygulayabilirsiniz.

---

## 1. PDF raporuna eklenebilecekler (hızlı / orta)

| Öneri | Açıklama | Zorluk |
|-------|----------|--------|
| **Sayfa numarası zaten var** | `Sayfa 1 / 4` mevcut; istenirse “Norya · Rapor No: …” gibi footer metni eklenebilir. | Kolay |
| **“Sonraki adımlar” kutusu** | Raporda 1 kutu: “Öneriler: … / Kontrol: X hafta sonra tekrar / Doktorunuzla paylaşın.” AI özetinden veya sabit metin. | Kolay |
| **Referans aralığı kartlarda** | Lab kartında “Referans: 70–100” zaten var; “Birim” (mg/dL vb.) her kartta net yazılabilir. | Kolay |
| **Önceki ölçümle karşılaştırma** | Aylık/yıllık pakette “Geçen sefer: 98 → Bu sefer: 95” gibi tek satır; trend verisi varsa gösterilir. | Orta |
| **Risk rozetleri** | Parametre kartında “Düşük / Normal / Yüksek” renkli küçük etiket (yeşil/sarı/kırmızı). | Orta |
| **İçindekiler (TOC)** | İlk sayfada tıklanabilir “Özet, Skor, Biyobelirteçler, Sonuçlar, Öneriler” linkleri (PDF bookmark). | Orta |
| **Erişilebilirlik** | PDF etiketleri (başlık, bölüm, tablo) ekleyerek ekran okuyucu uyumu. | Orta |
| **Kısa “tek cümle” özet** | İlk sayfanın en üstünde kalın: “Genel durum iyi; D vitamini takviye edilebilir.” gibi. | Kolay |

---

## 2. Ürün / kullanıcı deneyimi

| Öneri | Açıklama |
|-------|----------|
| **Rapor sonrası CTA** | PDF indirdikten sonra: “Raporu doktorunuzla paylaşın” / “X hafta sonra tekrar tahlil yaptırın” hatırlatması. |
| **E-posta özeti** | Aylık/yıllık: “Bu ay X analiz yaptınız; en son skor: Y” kısa e-posta. |
| **Tekrarlayan hatırlatma** | “3 ay önce tahlil yaptınız; tekrar yüklemeniz faydalı olabilir.” (tercihe bağlı). |
| **Güvenli paylaşım** | “Raporu link ile paylaş” → süre sınırlı, şifreli link (mevcut verify sayfasına benzer). |
| **Aile / çok profil** | Hesapta “Annem”, “Babam” gibi profiller; her biri kendi analiz geçmişi ve PDF’i. |
| **Mobil: kamera ile tahlil** | Telefonda lab sonuç kâğıdının fotoğrafından analiz (OCR + mevcut pipeline). |

---

## 3. İçerik / metin

| Öneri | Açıklama |
|-------|----------|
| **Parametre açıklaması** | Kartta “D vitamini” yanında 1 cümle: “Kemik ve bağışıklık için önemli; güneş ve besinle desteklenir.” |
| **Güvenilir kaynak linki** | Raporda “Daha fazla bilgi: [NHS / Mayo vb.]” tek link (küçük font, disclaimer ile). |
| **Beslenme önerisi eşlemesi** | “Düşük D vitamini” → raporda beslenme bölümünde “D vitamini içeren gıdalar” vurgusu. |

---

## 4. Teknik / kalite

| Öneri | Açıklama |
|-------|----------|
| **Test PDF’inde “ÖRNEK” damgası** | `test_premium_pdf.py` ile üretilen PDF’de sol üst veya filigran: “ÖRNEK – Gerçek hasta verisi değildir.” |
| **PDF boyutu** | Görseller sıkıştırılıyor mu kontrol; gerekirse font alt kümesi (subset) ile dosya küçültme. |
| **PDF/A (arşiv)** | Uzun süre saklama için PDF/A-1b veya PDF/A-2 (isteğe bağlı, daha sonra). |

---

## Öncelik önerisi (hemen yapılabilir)

1. **Tek cümle özet** — İlk sayfada en üstte kalın bir cümle (AI’dan veya sabit).  
2. **“Sonraki adımlar” kutusu** — Öneriler + “Doktorunuzla paylaşın” + “X hafta sonra kontrol.”  
3. **Test PDF’inde ÖRNEK damgası** — Yanlışlıkla gerçek rapor sanılmasın.  
4. **Risk rozetleri** — Kartlarda renkli “Normal / Düşük / Yüksek” etiket.

İstediğiniz maddeyi söylerseniz, o madde için adım adım (hangi dosya, hangi kod) uygulama planı çıkarabilirim.
