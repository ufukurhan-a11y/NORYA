# Bu Sistemde Ödemeler Nasıl İşliyor? (Otomatik mi?)

Özet: **Kullanıcı PayTR’de ödedikten sonra hak tanıma tamamen otomatik.** Elle onay yok; PayTR sunucunuza bildirim (callback) atar, sizin backend siparişi “tamamlandı” yapıp kullanıcıya analiz hakkı veya Pro plan tanır.

---

## 1. Kullanıcı tarafı (müşteri size ödeme yapar)

1. Kullanıcı **Ödeme** sayfasında plan seçer (tek analiz / aylık / yıllık).
2. **“Öde”** (veya “Güvenli ödemeye geç”) tıklar → backend `POST /paytr/init` ile PayTR’den **token** alır.
3. Kullanıcı **PayTR’nin sayfasına** gider (iframe veya yönlendirme): kart bilgilerini orada girer.
4. Ödeme **başarılı** veya **başarısız** olur.

Bu kısımda kullanıcı **sadece size** (Norya’ya) ödeme yapar; PayTR sizin sanal pos’unuzdur.

---

## 2. Otomatik kısım (callback — elle işlem yok)

- Ödeme sonucu belli olunca **PayTR**, sizin tanımladığınız **Bildirim URL**’e (örn. `https://noryaai.com/paytr/callback`) **POST** isteği gönderir.
- Sizin backend bu isteği alır:
  - **Hash doğrular** (PayTR’nin gönderdiği imza).
  - **Siparişi bulur** (`merchant_oid` ile).
  - **status == "success"** ise:
    - Siparişi `completed` yapar, `is_processed = True` işaretler.
    - **Tek analiz** ise: kullanıcıya `extra_credits + 1` ekler.
    - **Aylık/yıllık** ise: kullanıcının `plan = "pro"` yapar.
  - Hepsi **tek istekte, otomatik**; siz hiçbir şeye tıklamazsınız.

Yani: **Ödeme alındığı anda kullanıcıya hak tanıma otomatik.** Callback gelmezse (ağ hatası vb.) o sipariş “pending” kalır; o zaman admin panelinden veya PayTR panelinden kontrol edip gerekirse manuel müdahale edebilirsiniz.

---

## 3. Kullanıcı ödeme sonrası ne görür?

- PayTR, müşteriyi sizin **başarı** veya **hata** sayfanıza yönlendirir (`/payment/success` veya `/payment/failed`).
- Sayfa bazen **polling** ile sipariş durumunu kontrol eder (`GET /api/orders/status?merchant_oid=...`). Durum `paid` / `completed` olunca “Ödeme tamamlandı” mesajı veya analiz sayfasına yönlendirme gösterilir.

Yine tamamı **otomatik**; kullanıcı ekstra bir şey yapmaz.

---

## 4. “ChatGPT ödemeleri” / OpenAI tarafı

Sistemde **iki ayrı para akışı** var:

| Kim | Kime | Ne | Otomatik mi? |
|-----|------|-----|--------------|
| **Müşteri** | **Size (Norya)** | Tek analiz / Pro abonelik ücreti | Evet — PayTR ile ödeme, callback ile hak tanıma otomatik. |
| **Siz (Norya)** | **OpenAI** | Analiz başına API kullanım ücreti | Evet — sizin `OPENAI_API_KEY` ile her analizde API çağrısı yapılır; fatura OpenAI’a sizin hesabınıza kesilir. |

Yani:
- **Kullanıcıdan gelen ödemeler:** PayTR üzerinden size gelir; callback ile **otomatik** olarak sipariş tamamlanır ve kullanıcıya hak tanınır.
- **OpenAI (ChatGPT API) maliyeti:** Sizin işletme maliyetinizdir; kullanıcı doğrudan OpenAI’a ödeme yapmaz. Bu da zaten otomatik: her analiz isteğinde backend OpenAI API’yi çağırır, ücret sizin OpenAI hesabınızdan düşer.

---

## 5. Kısa özet

- **Kullanıcı ödemeleri:** PayTR ile alınıyor, **callback ile tamamen otomatik** işleniyor; kullanıcıya analiz hakkı / Pro plan otomatik tanınıyor.
- **OpenAI (ChatGPT) tarafı:** Sizin API anahtarınızla kullanılıyor; ödeme OpenAI’a sizden otomatik kesilir, kullanıcı bu kısımla doğrudan ilgili değil.

Elle yapmanız gereken tek şey: PayTR panelinde **Bildirim URL**’i doğru vermek ve canlıda **PAYTR_*** ortam değişkenlerini ayarlamak. Onlar tamam olduktan sonra ödeme ve hak tanıma akışı otomatik çalışır.
