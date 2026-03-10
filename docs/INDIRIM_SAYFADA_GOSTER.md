# İndirimin ödeme sayfasında görünmemesi

Admin’den eklediğiniz indirim, ödeme sayfasında **kampanya şeridi** ve **indirim kodu** olarak ancak belirli koşullarda gösterilir.

---

## 1. Admin’de mutlaka işaretli olsun

- **Aktif** – Kupon kapalıysa hiç uygulanmaz.
- **Ödeme sayfasında kampanya olarak göster** – Bu **işaretli değilse** indirim sayfada **hiç görünmez**.  
  Kupon sadece “manuel kodu giren” kullanıcıya uygulanır; şerit/çubuk çıkmaz.

---

## 2. Ürünler (products)

- **Boş bırakırsanız:** İndirim **tüm planlarda** (Tek analiz, Aylık, Yıllık) kampanya olarak listelenir.
- **Dolu (örn. `yearly` veya `yearly_99eur`):** Sadece o plan seçiliyken kampanya gösterilir.  
  Hem ürün adı (`yearly`, `monthly`, `single`) hem plan kodu (`yearly_99eur`, `monthly_50eur`, `single_13eur`) yazılabilir.  
  Ödeme sayfası varsayılan olarak yıllık planla açılıyorsa, sadece `single` yazdıysanız yıllıkta kampanya görünmez.

İndirimin tüm planlarda görünmesini istiyorsanız **Ürünler** alanını boş bırakın.

---

## 3. Geçerlilik tarihleri

- **Geçerli from / Geçerli until** varsa, bugünün tarihi bu aralıkta olmalı.
- **Ayın günleri** (valid_days_of_month) doluysa, bugünün günü bu listede olmalı.
- **Kullanım limiti** (max_uses) doluysa, kullanım sayısı limite ulaşmamış olmalı.

---

## 4. Canlı / yerel veritabanı farkı

- İndirimi **canlı sitedeki admin** (örn. noryaai.com/admin) üzerinden eklediyseniz → Canlı veritabanında kayıtlı; ödeme sayfası da canlıyı kullandığı sürece görünmesi gerekir.
- İndirimi **yerel** (127.0.0.1/admin) üzerinden eklediyseniz → Kayıt sadece yerel veritabanında; **canlı ödeme sayfasında görünmez**.  
  Canlıda görünsün istiyorsanız indirimi **canlı admin**’den ekleyin/düzenleyin.

---

## Canlıda hâlâ görünmüyorsa

1. **Kampanyayı canlı admin’den ekleyin**  
   Yerel (localhost) değil, **https://noryaai.com/admin** → İndirim kodları → yeni/düzenle. Canlı veritabanı (Render’daki DB) ayrıdır.

2. **“Ödeme sayfasında kampanya olarak göster”** kutusu işaretli mi?  
   İşaretli değilse kampanya şeridi hiç çıkmaz.

3. **Tarayıcı önbelleği**  
   Sayfayı **sıkı yenile** (Ctrl+Shift+R / Cmd+Shift+R) veya gizli pencerede açın.

4. **API’yi doğrudan test edin**  
   Tarayıcıda açın:  
   `https://noryaai.com/api/campaigns/featured?lang=tr&_=1`  
   Yanıtta `"active": true` ve `"campaign": { ... }` görüyorsanız kampanya sunucuda var demektir; sorun önbellek veya frontend.  
   `"active": false` ise canlı veritabanında uygun (aktif + ödeme sayfasında göster) kampanya yok; admin’de ayarları kontrol edin.

5. **Deploy**  
   Son kod değişiklikleri (cache-busting, no-cache header) deploy edildi mi? Render’da son deploy’u kontrol edin.

---

## Hızlı kontrol listesi

| Kontrol | Açıklama |
|--------|----------|
| **Aktif** | İşaretli |
| **Ödeme sayfasında kampanya olarak göster** | İşaretli (en sık unutulan) |
| **Ürünler** | Boş (tüm planlar) veya görünmesini istediğiniz planlar |
| **Geçerli from / until** | Bugünü kapsıyor veya boş |
| **Admin** | Canlı sitede (noryaai.com) yapıldı mı? |

Bunlar tamamsa sayfa yenilendiğinde (ve plan değiştirildiğinde) kampanya şeridi ve kod alanı görünür.
