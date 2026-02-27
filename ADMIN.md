# Norya Admin Paneline Giriş

Admin panelinde kullanıcılar, loglar, ödemeler ve istatistikler (şu an sitede kaç kişi, ülke, telefon vb.) görüntülenir.

---

## 1. Admin şifresini ayarlayın

Proje kökündeki `.env` dosyasında `ADMIN_SECRET` değerini tanımlayın. Bu değer sadece sizin bildiğiniz güçlü bir parola olmalı.

```env
ADMIN_SECRET=buraya-guclu-bir-sifre-yazin
```

Örnek üretmek için: `openssl rand -hex 24`

---

## 2. Siteyi çalıştırın

Terminalde:

```bash
cd /Users/ufukurhan/norya
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Yerelde: tarayıcıda **http://127.0.0.1:8000** açılır.
- Başka bir port kullanıyorsanız (örn. 5000) adres **http://127.0.0.1:5000** olur.

---

## 3. Admin paneline girin

1. Tarayıcıda **ana site adresini** açın (örn. **http://127.0.0.1:8000**).
2. Adres çubuğuna **`/admin`** ekleyin:
   - **http://127.0.0.1:8000/admin**
3. Açılan sayfada “Admin şifresini girin (ADMIN_SECRET)” kutusuna `.env` dosyasına yazdığınız **ADMIN_SECRET** değerini yapıştırın.
4. **Giriş** butonuna tıklayın.

Giriş başarılıysa istatistikler, kullanıcılar, loglar ve ödemeler tabloları görünür.

---

## Özet (hızlı erişim)

| Adım | Ne yapılır |
|------|-------------|
| 1 | `.env` içine `ADMIN_SECRET=...` yazın |
| 2 | `uvicorn app.main:app --reload --port 8000` ile siteyi başlatın |
| 3 | Tarayıcıda **http://127.0.0.1:8000/admin** açın |
| 4 | ADMIN_SECRET değerini girip **Giriş** deyin |

---

## Canlı (production) sunucuda

Site canlı domain’de çalışıyorsa (örn. `https://norya.com`):

- Admin paneli adresi: **https://norya.com/admin**
- Aynı şekilde ADMIN_SECRET’ı girin; `.env` dosyası sunucuda da aynı değişkenle ayarlanmış olmalı.

---

## Panelde neler var?

- **Şu an sitede:** Son 2 dakikada heartbeat atan giriş yapmış kullanıcı sayısı.
- **Toplam kullanıcı / analiz / ödeme:** Özet sayılar.
- **Kullanıcılar:** E-posta, ad, **telefon**, **ülke**, plan, ek hak, kayıt tarihi.
- **Loglar:** Olay türü, kullanıcı, IP, **ülke**, tarih.
- **Ödemeler:** Siparişler ve durumları.
- **Son analizler:** Son 50 analiz kaydı (kaynak, giriş/sonuç önizleme).
- **Sistem durumu:** Health linki ve OpenAI tanımlı mı bilgisi.

---

## Fatura (makbuz) ve logo

- **Fatura/makbuz** modülü henüz yok. Eklenirse aynı **Norya logosu** (turuncu kare + N.) ve **#e07a5f** marka rengi kullanılacak; rapor ve admin ile tutarlı olur.
- İsterseniz ileride: ödeme tamamlandığında PDF makbuz indirme veya e-posta ile fatura/makbuz gönderme eklenebilir.

---

## İleride eklenebilecek özellikler

| Özellik | Açıklama |
|--------|----------|
| **Fatura / makbuz PDF** | Ödeme sonrası indirilebilir veya e-posta ile gönderilen makbuz (aynı logo). |
| **E-posta bildirimleri** | Kayıt onayı, ödeme onayı, analiz hazır (opsiyonel). |
| **Admin: manuel hak** | Zaten var: `POST /payment/grant` ile kullanıcıya analiz hakkı tanıma. |
| **Admin: ödeme export** | Ödemeleri CSV/Excel olarak dışa aktarma. |
| **Kullanıcı paneli** | Profil, geçmiş ödemeler, abonelik durumu tek sayfada. |
| **E-posta şablonları** | Logo’lu HTML e-posta (davet, şifre sıfırlama, makbuz). |
