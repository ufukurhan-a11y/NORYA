# İndirim Kodu – Nereden Girilir ve Test

## 1. Admin panele giriş

1. Tarayıcıda aç: **http://127.0.0.1:8000/admin**  
   (Sunucu kapalıysa proje klasöründe `./start.sh` çalıştır.)

2. `/admin` sizi otomatik **http://127.0.0.1:8000/admin/login** sayfasına yönlendirir.

3. **Admin şifresi:** `.env` dosyasındaki `ADMIN_SECRET` değeri (şu an: `ufK.1521`).  
   Bu değeri girip **Giriş**’e tıkla.

4. Girişten sonra sol menüde **İndirim Kodları** linkine tıkla  
   veya doğrudan aç: **http://127.0.0.1:8000/admin/coupons**

---

## 2. Yeni indirim kodu ekleme

1. **İndirim Kodları** sayfasında **+ Yeni kod** butonuna tıkla.

2. Formu doldur:
   - **Kod:** örn. `indirim20`
   - **İndirim tipi:** Yüzde (%)
   - **Değer:** 20
   - **Sadece ayın bu günlerinde geçerli:** boş bırak (her gün) veya örn. `1-7` (ayın 1–7’si)
   - Diğer alanlar isteğe bağlı

3. **Oluştur**’a tıkla. Kod listede görünür.

---

## 3. Test (müşteri tarafı)

1. Ana siteyi aç: **http://127.0.0.1:8000**

2. **Fiyatlandırma** bölümüne in, **Tek Analiz** (veya başka bir plan) için **Satın Al** / **Başla** benzeri butona tıkla.  
   Ödeme özeti (checkout) sayfası açılır.

3. **İndirim kodu** kutusuna az önce oluşturduğun kodu yaz (örn. `indirim20` veya `INDIRIM20`).

4. **Uygula**’ya tıkla.  
   - Geçerli kod: “İndirim uygulandı.” yazar, toplam tutar indirimli fiyata düşer.  
   - Geçersiz kod: Kırmızı hata mesajı çıkar.

5. Ödemeyi gerçekten yapmak zorunda değilsin; sadece indirim satırının ve toplamın doğru güncellenmesi test için yeterli.

---

## Özet adresler

| Ne yapıyorsun?      | Adres |
|---------------------|--------|
| Admin giriş         | http://127.0.0.1:8000/admin veya http://127.0.0.1:8000/admin/login |
| İndirim kodları     | http://127.0.0.1:8000/admin/coupons |
| Yeni kod ekle       | http://127.0.0.1:8000/admin/coupons/new |
| Ana site (test)     | http://127.0.0.1:8000 → Fiyatlandırma → plan seç → indirim kodu dene |

Admin şifresi `.env` içindeki `ADMIN_SECRET` (örn. `ufK.1521`).
