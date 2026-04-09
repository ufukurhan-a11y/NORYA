# Google Ads ile Norya’da Reklam Verme

Norya projesinde **GA4** ve **Google Ads (gtag)** zaten entegre. Aşağıdaki adımlarla canlıda reklam verebilirsin.

---

## 1. Google Ads hesabı açma

1. **ads.google.com** → “Reklam vermeye başla” veya “Hesap oluştur”.
2. E-posta (tercihen iş e-postası, örn. support@noryaai.com) ile giriş yap veya yeni Google hesabı oluştur.
3. **İşletme adı**: Norya / NoryaAI.
4. **Web sitesi**: `https://noryaai.com`
5. Kampanya türü: “Arama” (Search) veya “Performans” (Search + Display) ile başlamak yeterli.
6. Hedef: “Web sitesi trafiği” veya “Dönüşümler” (ödeme/satış takibi için).
7. Bölge ve dil: Türkiye, Türkçe (veya hedeflediğin ülkeler).
8. Ödeme bilgilerini ekle (kredi kartı / banka kartı). Reklam harcaması buradan düşer.

---

## 2. Dönüşüm (Conversion) tanımlama

Reklamların “tıklama” değil “satış / kayıt” getirip getirmediğini ölçmek için dönüşüm gerekir.

1. Google Ads → **Araçlar ve Ayarlar** (dişli) → **Ölçüm** → **Dönüşümler**.
2. **+ Yeni dönüşüm eylemi** → **Web sitesi**.
3. **Kategori**: “Satın alma” veya “Kayıt” (ödeme tamamlandı / e-posta doğrulandı).
4. **Ad**: örn. “Ödeme tamamlandı” veya “Analiz satın alma”.
5. **Değer**: Sabit (örn. ortalama sipariş tutarı) veya “Her dönüşüm için farklı değer kullan” (dinamik).
6. **Sayım**: “Bir” (aynı kullanıcıda tek sayım).
7. **Dönüşüm penceresi**: 30 gün (varsayılan uygun).
8. Kaydet → **Etiket kurulumu** kısmında **“Google tag (gtag.js) kullanıyorum”** seç.
9. **Dönüşüm kimliği** ve **Dönüşüm etiketi** (AW-XXXXXXXXX ve etiket kodu) burada görünür. Bunları not al.

---

## 3. Norya’da Google Ads ID’sini ayarlama

Projede zaten gtag ile GA4 + Google Ads destekleniyor. Sadece **Conversion ID**’yi ortam değişkenine yazman yeterli.

1. **Google Ads hesap kimliği** (Conversion ID): `AW-XXXXXXXXX` formatında (Araçlar → Dönüşümler’de veya hesap ayarlarında görürsün).
2. **.env** (ve canlıda Render/panel) içine ekle:
   ```env
   GOOGLE_ADS_CONVERSION_ID=AW-XXXXXXXXX
   ```
   (XXXXXXXXX kısmını kendi numaranla değiştir.)
3. İsteğe bağlı: GA4 ölçüm kimliği aynı kalabilir veya ayrı bir property kullanıyorsan:
   ```env
   GA_MEASUREMENT_ID=G-XXXXXXXXXX
   ```
4. Deploy sonrası sitenin sayfalarında gtag ile hem GA4 hem Google Ads yüklenecek; dönüşüm etiketini Google Ads arayüzünden “gtag kullanıyorum” ile eklediysen eşleşir.

---

## 4. Dönüşümü ödeme / kayıt sayfasına bağlama (isteğe bağlı)

Şu an sitede gtag **config** ile Google Ads yüklü; sayfa görüntüleme takibi otomatik. **Ödeme tamamlandı** gibi özel bir dönüşümü sayfada tetiklemek istersen:

- **Ödeme başarı sayfası** (PayTR’dan yönlendiğin URL) üzerinde, o sayfada bir kez çalışacak şekilde `gtag('event', 'conversion', { 'send_to': 'AW-XXXXXXXXX/YYYYYYYYY' });` eklenebilir.  
- `AW-XXXXXXXXX` = Conversion ID, `YYYYYYYYY` = Google Ads’te oluşturduğun dönüşüm eyleminin **Conversion Label**’ı (Dönüşümler → ilgili eylem → Etiket kurulumu).

Bunu ileride istersen “ödeme başarı” şablonuna bu event’i ekleyecek şekilde genişletebiliriz.

---

## 5. İlk kampanyayı oluşturma (Arama)

1. Google Ads giriş → **Kampanyalar** → **+ Yeni kampanya**.
2. **Hedef**: “Satışlar” veya “Web sitesi trafiği”.
3. **Kampanya türü**: **Arama** (Search).
4. **Anahtar kelimeler**:  
   Örn. “kan tahlili yorumlama”, “laboratuvar sonucu analiz”, “kan testi değerlendirme”, “biyobelirteç analiz”, “sağlık raporu akıllı analiz”.
5. **Teklif**: “Tıklama başına ödeme” (CPC). Başlangıç için **manuel teklif** ile günlük bütçe (örn. 50–100 TL) ver; sonra “Maksimum tıklama” veya “Dönüşüm” odaklı stratejiye geçebilirsin.
6. **Reklam grupları**: Her grup 5–15 anahtar kelime, ortak reklam metni. Örn. bir grup “kan tahlili” varyasyonları, bir grup “laboratuvar sonucu” varyasyonları.
7. **Reklam metni**: Başlık (30 karakter), açıklama (90 karakter). Örn: “Kan Tahlili Yorumlama | Norya AI” / “Laboratuvar sonuçlarınızı anında akıllı analiz ile değerlendirin. Deneyin.”
8. **Hedef URL**: `https://noryaai.com` veya doğrudan `https://noryaai.com/upload`, `https://noryaai.com/payment` gibi sayfalar (kampanya hedefine göre).

---

## 6. Bütçe ve optimizasyon

- **Günlük bütçe**: Küçük başla (50–150 TL); 1–2 hafta veri topla.
- **Dönüşüm takibi** açıksa, bir süre sonra “Dönüşüm odaklı” teklif stratejisi kullan (örn. “Hedef CPA” veya “Maksimum dönüşüm”).
- **Arama terimleri raporu**: Hangi aramalarda reklamın çıktığını incele; gereksiz terimleri “negatif anahtar kelime” olarak ekle.
- **Coğrafya**: Sadece Türkiye veya hedef ülkeler; gereksiz bölgeleri kapat.

---

## 7. Özet kontrol listesi

| Adım | Yapıldı mı? |
|------|-------------|
| Google Ads hesabı açıldı | |
| Dönüşüm eylemi oluşturuldu (Web, gtag) | |
| `.env` / canlıda `GOOGLE_ADS_CONVERSION_ID=AW-XXXXXXXXX` ayarlandı | |
| Site deploy edildi, sayfada gtag yükleniyor | |
| İlk arama kampanyası + anahtar kelimeler + reklam metni yazıldı | |
| Günlük bütçe belirlendi | |

---

## Faydalı linkler

- [Google Ads Yardım — İlk kampanyanız](https://support.google.com/google-ads/answer/6367)
- [Dönüşümleri gtag ile kurma](https://support.google.com/google-ads/answer/7548399)
- Norya’da gtag: `app/main.py` (inject_tracking_ids), `app/templates/base.html`, `static/index.html` (GA enjeksiyonu)

Bu doküman proje içinde güncellenebilir; reklam stratejisi (Display, YouTube, Remarketing) ileride aynı mantıkla eklenebilir.
