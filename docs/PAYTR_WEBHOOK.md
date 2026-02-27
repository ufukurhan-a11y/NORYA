# PayTR Webhook / Callback

PayTR ödeme bildirimi (callback) endpoint'leri ve hash/imza doğrulaması.

## Endpoint'ler

| URL | Açıklama |
|-----|----------|
| `POST /payment/callback` | PayTR bildirim URL'i (panelde bu adresi tanımlayın) |
| `POST /api/paytr/webhook` | Alias; aynı işlem |

PayTR, ödeme sonucunu **form-urlencoded** POST ile bu adrese gönderir.

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
   - Yanıt: **400** + metin `PAYTR notification failed: bad hash`.
4. Hash **doğruysa** idempotent ödeme akışına geçilir (Sprint-1).

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
- Uygulama çalışıyor olmalı: `bash baslat.sh` (port 8000).

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

- Yanıt: **400** ve body: `PAYTR notification failed: bad hash`.
- `SecurityLog` tablosunda `event='paytr_invalid_hash'` kaydı oluşur (Admin → Güvenlik panelinden veya DB'den kontrol edebilirsin).

### 4. Eksik key/salt (400)

- Geçici olarak `.env`'de `PAYTR_MERCHANT_KEY` veya `PAYTR_MERCHANT_SALT`'ı boşaltıp uygulamayı yeniden başlat.
- Herhangi bir payload ile callback çağır.

Beklenen: **400** (`PAYTR notification failed: misconfiguration`) ve gerekirse `paytr_invalid_hash` / missing key-salt ile ilgili bir log kaydı.

---

## Özet

- Hash **doğrulanmadan** ödeme işlenmez.
- `merchant_key` ve `merchant_salt` **env'den** okunur.
- Hash **yanlışsa**: `SecurityLog` → `paytr_invalid_hash`, yanıt **400**.
- Hash **doğruysa**: Sprint-1 idempotent akışı (is_processed, processed_at, kullanıcı hakları) uygulanır.
