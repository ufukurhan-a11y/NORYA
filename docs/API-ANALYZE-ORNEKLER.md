# /analyze Endpoint'leri – Beklenen Alanlar ve Çalışan Örnekler

## 1) POST /analyze (metin analizi)

**Content-Type:** `application/json`  
**Zorunlu alan:** `text` (string, boş olamaz)  
**İsteğe bağlı:** `doctor_notes` (string), `lang` (string: tr, en, de, …)

### Çalışan örnek (fetch)

```javascript
fetch('http://127.0.0.1:8000/analyze', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
  },
  body: JSON.stringify({
    text: 'Hemoglobin: 14 g/dL, WBC: 7.2, Glukoz: 95 mg/dL',
    doctor_notes: null,
    lang: 'tr'
  })
});
```

### Çalışan örnek (curl)

```bash
curl -X POST http://127.0.0.1:8000/analyze \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"text":"Hemoglobin: 14 g/dL","lang":"tr"}'
```

**Not:** JSON body Pydantic ile doğrulanır. Eksik/yanlış alan **422** döner; doğru format: `text` zorunlu string.

---

## 2) POST /analyze/upload (dosya – multipart)

**Content-Type:** `multipart/form-data`  
**Zorunlu alan:** `file` (dosya)  
**İsteğe bağlı:** `lang` (string)

### Çalışan örnek (FormData + fetch)

```javascript
var formData = new FormData();
formData.append('file', fileInput.files[0]);  // alan adı: "file"
formData.append('lang', 'tr');

fetch('http://127.0.0.1:8000/analyze/upload', {
  method: 'POST',
  headers: { 'Authorization': 'Bearer ' + token },
  body: formData
});
```

**Önemli:** `Content-Type` header'ı **göndermeyin**; tarayıcı otomatik `multipart/form-data; boundary=...` ekler.

### Çalışan örnek (curl)

```bash
curl -X POST http://127.0.0.1:8000/analyze/upload \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@tahlil.pdf" \
  -F "lang=tr"
```

---

## 3) POST /analyze/upload-json (dosya – base64 JSON)

**Content-Type:** `application/json`  
**Zorunlu alan:** `file_base64` (string, base64)  
**İsteğe bağlı:** `filename` (string, varsayılan "upload"), `lang` (string)

### Çalışan örnek (fetch)

```javascript
var b64 = '...'; // dosyadan base64 (FileReader.readAsDataURL sonrası virgülden sonrası)
fetch('http://127.0.0.1:8000/analyze/upload-json', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
  },
  body: JSON.stringify({
    file_base64: b64,
    filename: 'tahlil.jpg',
    lang: 'tr'
  })
});
```

**Not:** UI varsayılan olarak FormData (`/analyze/upload`) kullanır; upload-json yedek amaçlıdır.

---

## Kesin test (200 dönene kadar)

Sunucu çalışırken (`uvicorn app.main:app --reload --port 8000`) aşağıdaki curl'ler **giriş yapılmış token** ile **200** döner. Token yoksa 401 alırsınız; önce `/auth/login` ile token alın.

### 1) Metin testi

```bash
curl -i -X POST "http://127.0.0.1:8000/analyze" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"text":"LDL 115, HDL 52","lang":"tr"}'
```

Beklenen: `HTTP/1.1 200 OK` ve JSON içinde `sonuc`, `analiz_id`.

### 2) Dosya testi

```bash
curl -i -X POST "http://127.0.0.1:8000/analyze/upload" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@/Users/$USER/Downloads/test.pdf" \
  -F "lang=tr"
```

Beklenen: `HTTP/1.1 200 OK` ve JSON içinde `sonuc`, `analiz_id`. (`test.pdf` yoksa geçerli bir PDF/JPG yolu kullanın.)

---

## Alan isimleri özeti

| Endpoint              | Gönderi tipi   | Zorunlu alan(lar) | İsim uyumu (frontend)     |
|-----------------------|----------------|----------------------------------|---------------------------|
| POST /analyze         | JSON           | `text`                           | ✅ text, doctor_notes, lang |
| POST /analyze/upload  | FormData       | `file`                           | ✅ file, lang              |
| POST /analyze/upload-json | JSON       | `file_base64`                    | ✅ file_base64, filename, lang |

422 alırsan terminalde şu log çıkar: `Request validation error (422): path=... method=... detail=[...]` – `detail` içinde eksik/hatalı alan adı yazar.
