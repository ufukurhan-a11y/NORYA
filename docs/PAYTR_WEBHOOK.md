# PayTR Webhook / Callback

PayTR ödeme bildirimi (callback) endpoint'leri ve hash/imza doğrulaması.

## Endpoint'ler

| URL | Açıklama |
|-----|----------|
| `POST /paytr/callback` | PayTR bildirim URL'i (panelde **Bildirim URL** olarak `https://noryaai.com/paytr/callback` kullanılabilir). **Public, auth yok.** |
| `POST /payment/callback` | Alias; aynı işlem |
| `POST /api/payment/callback` | Alias; aynı işlem (örn. Render'da bu URL kullanılıyorsa) |
| `POST /api/paytr/webhook` | Alias; aynı işlem |
| `GET /paytr/callback` | Tarayıcıda açıldığında 404 vermemek için 200 + kısa metin döner; ödeme bildirimi **sadece POST** ile gelir. |

PayTR, ödeme sonucunu **form-urlencoded** POST ile bu adreslerden birine gönderir. Başarılı işlemde yanıt: **plain text `OK`** (200).

---

## Gerekli env değişkenleri

Callback'in çalışması ve **hash doğrulaması** için aşağıdakiler zorunludur:

| Değişken | Açıklama |
|----------|----------|
| `PAYTR_MERCHANT_ID` | PayTR Mağaza Panel → Entegrasyon Bilgileri |
| `PAYTR_MERCHANT_KEY` | PayTR Mağaza Panel → Entegrasyon Bilgileri |
| `PAYTR_MERCHANT_SALT` | PayTR Mağaza Panel → Entegrasyon Bilgileri |

- `merchant_key` ve `merchant_salt` **hash doğrulamasında** kullanılır.
- Eksik veya yanlış olursa ödeme **işlenmez**; hash yanlışsa `SecurityLog`'a `paytr_invalid_hash` yazılır ve **400** dönülür.

---

## Hash doğrulaması

1. PayTR, POST ile `merchant_oid`, `status`, `total_amount`, `hash` ve diğer alanları gönderir.
2. Sunucu aynı hash'i hesaplar:
   - Metin: `{merchant_oid}{PAYTR_MERCHANT_SALT}{status}{total_amount}`
   - HMAC-SHA256(metin, `PAYTR_MERCHANT_KEY`)
   - Sonuç Base64 encode edilir.
3. Gelen `hash` ile hesaplanan değer **eşleşmezse**:
   - `SecurityLog` tablosuna `event='paytr_invalid_hash'` yazılır (ip, endpoint, detail).
   - Yanıt: **200** + metin `OK` (PayTR tekrar denemesin diye her zaman OK dönülür).
4. Hash **doğruysa** idempotent ödeme akışına geçilir.

---

## Örnek payload (PayTR'den gelen)

PayTR dokümantasyonuna göre bildirimde örnek alanlar:

```
merchant_oid=norya_123_1730123456_abc1
status=success
total_amount=1300
hash=Base64(HMAC-SHA256(...))
payment_id=...          # varsa transaction_id olarak kullanılır
transaction_id=...      # alternatif
```

Yerel test için bu alanları kendin üretirsin; `hash`'i yukarıdaki formüle göre hesaplaman gerekir.

---

## Doğrulamayı nasıl test edersin?

### 1. Ortam

- `.env` içinde `PAYTR_MERCHANT_KEY` ve `PAYTR_MERCHANT_SALT` dolu olmalı.
- Uygulama çalışıyor olmalı: `./start.sh` veya `uvicorn app.main:app --reload` (port 8000).

### 2. Geçerli hash ile test (200 / işlem başarılı)

- DB'de mevcut bir siparişin `merchant_oid` değerini al (örn. admin panelinden veya SQLite ile).
- Aynı sipariş için `status` ve `total_amount` değerlerini belirle (örn. `success`, `1300`).
- Hash'i hesapla (Python):

```python
import base64, hmac, hashlib

merchant_oid = "norya_1_1730123456_abc1"  # gerçek merchant_oid
merchant_salt = "SALT_DEĞERİ"             # .env'deki PAYTR_MERCHANT_SALT
merchant_key = "KEY_DEĞERİ"               # .env'deki PAYTR_MERCHANT_KEY
status = "success"
total_amount = "1300"

hash_str = f"{merchant_oid}{merchant_salt}{status}{total_amount}"
h = base64.b64encode(hmac.new(merchant_key.encode(), hash_str.encode(), hashlib.sha256).digest()).decode()
print("hash:", h)
```

- Callback'i çağır:

```bash
curl -X POST http://127.0.0.1:8000/payment/callback \
  -d "merchant_oid=norya_1_1730123456_abc1" \
  -d "status=success" \
  -d "total_amount=1300" \
  -d "hash=HESAPLADIĞIN_HASH"
```

Beklenen: **200 OK**, sipariş `completed` ve `is_processed=True` olur (idempotent akış).

### 3. Yanlış hash ile test (400 + SecurityLog)

- Aynı `merchant_oid`, `status`, `total_amount` ile **yanlış** bir `hash` gönder (örn. `hash=wrong`).

```bash
curl -X POST http://127.0.0.1:8000/payment/callback \
  -d "merchant_oid=norya_1_1730123456_abc1" \
  -d "status=success" \
  -d "total_amount=1300" \
  -d "hash=wrong"
```

Beklenen:

- `SecurityLog` tablosunda `event='paytr_invalid_hash'` kaydı oluşur; yanıt her zaman **200 OK** (PayTR tekrar denemesin).

### 4. Eksik key/salt

- Geçici olarak `.env`'de `PAYTR_MERCHANT_KEY` veya `PAYTR_MERCHANT_SALT`'ı boşaltıp uygulamayı yeniden başlat.
- Herhangi bir payload ile callback çağır: yanıt **200 OK**, logda missing key/salt kaydı düşer.

---

## Deploy sonrası test (curl)

```bash
# Başarı sayfası
curl -i https://noryaai.com/payment/success

# Başarısız sayfa
curl -i https://noryaai.com/payment/failed

# Callback (hash yanlış olsa bile 200 OK dönmeli; fraud loglanır)
curl -i -X POST https://noryaai.com/paytr/callback -d "merchant_oid=test&status=success&total_amount=100&hash=x"
```

---

## Özet

- Callback **her zaman** `200` + body `OK` döner (PayTR tekrar denemesi önlenir).
- Hash **yanlışsa**: `SecurityLog` → `paytr_invalid_hash`, sipariş güncellenmez.
- Hash **doğruysa**: idempotent akış (is_processed, paid_at, kullanıcı hakları) uygulanır.
