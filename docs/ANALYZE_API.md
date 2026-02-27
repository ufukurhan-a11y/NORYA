# Analyze API — endpoint ve alan eşlemesi

422 hatasını önlemek için body/FormData alan isimleri backend ile birebir aynı olmalı.

---

## 1) POST /analyze (metin analizi)

**Beklenen:** `Content-Type: application/json`, JSON body.

| Alan           | Tip     | Zorunlu | Açıklama        |
|----------------|--------|---------|------------------|
| `text`         | string | Evet    | Tahlil metni     |
| `doctor_notes` | string | Hayır   | Doktor notu      |
| `lang`         | string | Hayır   | Rapor dili (tr, en, …) |

**Çalışan örnek (fetch):**
```javascript
fetch(API_BASE + '/analyze', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token },
  body: JSON.stringify({
    text: 'Hemoglobin: 14 g/dL, WBC: 7.2',
    doctor_notes: null,
    lang: 'tr'
  })
});
```

**Çalışan örnek (curl):**
```bash
curl -X POST http://127.0.0.1:8000/analyze \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT" \
  -d '{"text":"Hemoglobin: 14 g/dL","lang":"tr"}'
```

---

## 2) POST /analyze/upload (dosya — multipart)

**Beklenen:** `Content-Type: multipart/form-data` (header ekleme; tarayıcı boundary ekler).

| Alan   | Tip  | Zorunlu | Açıklama      |
|--------|------|---------|---------------|
| `file` | file | Evet    | PDF veya JPG/PNG |
| `lang` | string | Hayır | Rapor dili    |

**Çalışan örnek (fetch + FormData):**
```javascript
var formData = new FormData();
formData.append('file', file);   // File nesnesi
formData.append('lang', 'tr');
fetch(API_BASE + '/analyze/upload', {
  method: 'POST',
  headers: { 'Authorization': 'Bearer ' + token },
  body: formData
});
```

**Not:** `Content-Type` eklenmemeli; tarayıcı `multipart/form-data; boundary=...` atar.

---

## 3) POST /analyze/upload-json (dosya — base64)

**Beklenen:** `Content-Type: application/json`, JSON body.

| Alan          | Tip    | Zorunlu | Açıklama          |
|---------------|--------|---------|--------------------|
| `file_base64` | string | Evet    | Base64 kodlanmış dosya |
| `filename`    | string | Hayır   | Varsayılan: "upload" |
| `lang`        | string | Hayır   | Rapor dili        |

**Çalışan örnek (fetch):**
```javascript
var b64 = '...'; // base64 string (data URL'den virgül sonrası)
fetch(API_BASE + '/analyze/upload-json', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token },
  body: JSON.stringify({
    file_base64: b64,
    filename: 'tahlil.jpg',
    lang: 'tr'
  })
});
```

---

## Hata önleme

- **422 Unprocessable Content:** Bu dokümandaki alan isimleri ve Content-Type kullanılmalı; backend artık bu endpoint'lerde body'yi elle okuyor, 422 yerine **400** ve açıklayıcı mesaj döner.
- **400:** `detail` alanındaki mesajda eksik/yanlış alan yazacak (örn. "'text' alanı zorunludur").
- ValidationError detayı sunucu logunda: `Request validation error (422): path=... detail=[...]`
