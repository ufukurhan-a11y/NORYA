# Norya Ödeme Akışı (PayTR)

## Kart bilgilerini kim, nerede giriyor?

**Kart bilgilerini müşteri (ödeme yapan kişi) girer** — ve **sizin sitenizde değil**, PayTR’ın güvenli sayfasında (iframe içinde).

- **Sizin** kartınızı girmeniz gerekmez. Ödemeyi **almanız** PayTR hesabınıza bağlı: PayTR panelde tanımlı banka/ödeme hesabınıza para aktarılır.
- **Müşteri**, “Ödemeyi Başlat” / “Yıllık Planı Başlat” dedikten sonra açılan **PayTR iframe’inde** kendi kart numarası, son kullanma tarihi ve CVV’yi girer. Bu sayfa `paytr.com` alanında açılır; Norya bu bilgileri hiç görmez, PCI uyumluluğu PayTR tarafındadır.

Bu yüzden **kart bilgisi girişi için ayrı bir sayfa yazmıyorsunuz**. Mevcut ödeme sayfası + PayTR iframe’i bu işi yapıyor.

---

## İşlem adımları (sırayla)

1. **Müşteri** noryaai.com/payment (veya /pay) sayfasına gider, plan seçer (tek analiz / aylık / yıllık), e‑posta girer, “Ödemeyi Başlat”a tıklar.

2. **Tarayıcı** backend’e `POST /paytr/init` atar (plan_kodu, e‑posta, isim, kupon vb.).

3. **Backend (Norya)**  
   - Sipariş kaydı oluşturur (`PaymentOrder`, `merchant_oid`).  
   - PayTR’a “token al” isteği atar (`https://www.paytr.com/odeme/api/get-token`).  
   - PayTR’dan dönen **token**’ı tarayıcıya gönderir.

4. **Tarayıcı** bu token ile iframe’in adresini ayarlar:  
   `https://www.paytr.com/odeme/guvenli/{token}`  
   Sayfa içinde **PayTR’ın kendi formu** açılır; **müşteri kart bilgilerini burada girer**.

5. **PayTR** kartı işler, ödemeyi alır. Sonra iki şey yapar:  
   - **Tarayıcıyı yönlendirir:**  
     - Başarılı → `merchant_ok_url` (örn. `.../payment/success?merchant_oid=...`)  
     - Başarısız → `merchant_fail_url` (örn. `.../payment/failed?merchant_oid=...`)  
   - **Backend’e bildirim (callback) gönderir:**  
     `POST /payment/callback` (veya `/paytr/callback`) ile ödeme sonucunu iletir.

6. **Backend** callback’te imzayı doğrular, siparişi “completed” yapar, kullanıcıya premium/analiz hakkı tanır. Success sayfası da (gerekirse polling ile) sipariş durumunu gösterir.

---

## Sizin yapmanız gerekenler (ödeme almak için)

1. **PayTR’da tüccar hesabı** açıp, panelden **Bildirim URL**’ini şu şekilde ayarlayın:  
   `https://noryaai.com/payment/callback` (veya `https://noryaai.com/paytr/callback` — ikisi de aynı handler’a gider).

2. **.env** (veya canlı sunucu ortam değişkenleri) içinde PayTR bilgilerini doldurun:  
   - `PAYTR_MERCHANT_ID`  
   - `PAYTR_MERCHANT_KEY`  
   - `PAYTR_MERCHANT_SALT`  

3. **Para nereye yatacak?**  
   PayTR panelde tanımladığınız banka/ödeme hesabına. Norya’da “kendi kartımı gireceğim” diye bir sayfa yok; ödemeyi **alma** tamamen PayTR hesabınız üzerinden olur.

---

## Özet

| Soru | Cevap |
|------|--------|
| Kart bilgisi giriş sayfası yazacak mıyım? | Hayır. Kart bilgisi PayTR iframe’inde (paytr.com) girilir. |
| Müşteri kartını nerede girer? | “Ödemeyi Başlat” sonrası açılan iframe’de (PayTR güvenli ödeme sayfası). |
| Ben (satıcı) kendi kartımı nerede gireceğim? | Girmiyorsunuz; para PayTR hesabınıza tanımlı banka hesabına aktarılır. |
| Ödeme sayfası ne işe yarıyor? | Plan seçimi, fiyat, “Ödemeyi Başlat” butonu ve token alındıktan sonra PayTR iframe’ini göstermek. |

Mevcut `/payment` (ve `/pay`) sayfası bu akışı karşılıyor; ekstra bir “kart formu sayfası” gerekmez.
