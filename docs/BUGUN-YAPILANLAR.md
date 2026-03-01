# Bugün Yapılanlar (1 Mart 2026)

Kısa özet: PDF indirme (özellikle canlıda), admin logları, deploy, Cloudflare ve dokümantasyon.

---

## 1. PDF indirme (local + canlı)

**Sorun:** Lokalda PDF açılıyordu, canlıda (noryaai.com) “Önce analiz yapın” veya tıklanınca hareket yoktu.

**Yapılanlar:**
- **Backend:** Analiz cevabında her zaman `analiz_id` dönüyor (test modunda da kayıt oluşturulup id dönüyor). PDF için tek kullanımlık token: `POST /analyze/history/{id}/pdf-token` → `access_token`; `GET .../pdf?access_token=...` ile PDF açılıyor (proxy Authorization keserse bile çalışır).
- **Frontend:** “Raporu İndir” önce token alıyor, sonra `?access_token=...` ile PDF URL’ini yeni sekmede açıyor. `rid` yoksa son analiz `/analyze/history?limit=1` ile alınıp URL `?rid=...` ile güncelleniyor. Hata mesajı: sadece gerçekten rid yoksa “Önce analiz yapın”; sunucu hatasında HTTP kodu ve gerçek mesaj gösteriliyor.
- **Console log:** `[PDF] Raporu İndir tıklandı, getReportId()= ...`, Token URL, Token response status — Network/Console’dan takip için.
- **CSP:** `script-src`’e cdnjs ve cloudflareinsights, `img-src`’e `blob:` eklendi. Kullanılmayan jsPDF/html2canvas script’leri kaldırıldı (PDF artık sunucuda).
- **PDF 500:** Backend’de PDF hatası olunca `log.exception` ile tam traceback yazılıyor. Prod’da WeasyPrint için `Dockerfile` (cairo/pango) ve RENDER-DEPLOY’da “PDF 500” bölümü eklendi.

**Dosyalar:** `app/main.py`, `app/core/security.py`, `static/index.html`, `app/services/report_pdf.py`, `Dockerfile`, `docs/RENDER-DEPLOY.md`

---

## 2. Admin: Upload ve Hata logları

- Sol menü: “Dosya Upload Logları”, “Hata Logları”; metin tek satırda düzgün görünsün diye `white-space: nowrap`, sidebar `w-60`.
- Backend’de hata mesajı kısaltması kaldırıldı (`uploads.py` ve `errors.py`’deki `[:100]` / `[:200]`).
- Şablonda hata sütunu: `truncate` kaldırıldı, `break-words`, `whitespace-pre-wrap`, `max-w-xl`, `title` (tooltip) eklendi.

**Dosyalar:** `app/templates/admin/base_admin.html`, `app/templates/admin/uploads_list.html`, `app/templates/admin/errors_list.html`, `app/admin/routers/uploads.py`, `app/admin/routers/errors.py`

---

## 3. PDF rapor içeriği (grafik, diyet, takviye)

- Bölüm başlığı tanıma genişletildi: “Diyet planı”, “Takviye”, “Kalp” vb. ayrı bölüm olarak `raw_sections`’a düşüyor.
- Biyobelirteç satırı için esnek regex (`BIOMARKER_LINE_RELAXED`) eklendi; tablo ve range bar grafiklerinin daha sık üretilmesi hedeflendi.

**Dosyalar:** `app/services/report_pdf.py`

---

## 4. Deploy ve sunucu

- **Deploy:** `deploy/deploy.sh` (commit + push; Render otomatik build), `deploy/README-DEPLOY.md`.
- **Sunucu yeniden başlatma:** `./portu-kapat-ve-baslat.sh` veya `./restart-server.sh`; kullanım notları verildi.

**Dosyalar:** `deploy/deploy.sh`, `deploy/README-DEPLOY.md`, `restart-server.sh`

---

## 5. Cloudflare

- **docs/CLOUDFLARE-VE-GOOGLE-ANALYTICS.md** güncellendi: PDF ve sitenin açılması için kısa liste:
  - SSL/TLS: Full (+ Always Use HTTPS).
  - Speed → Rocket Loader: Kapalı.
  - Security → Security Level: Medium veya Low.
  - Authorization / CSP header’ları değiştirilmesin.
  - Tarayıcıda noryaai.com için pop-up izni.

---

## 6. Dokümantasyon

- RENDER-DEPLOY: PDF 500 ve Docker/WeasyPrint bölümü.
- Cloudflare: sadece yapılacaklar listesi, gereksiz detay azaltıldı.

---

**Canlıda PDF’in düzelmesi için:** Bu değişikliklerin hepsi deploy edilmeli (`./deploy/deploy.sh`), Render build bitmeli, sayfa sert yenilenmeli (Cmd+Shift+R). Cloudflare’de Rocket Loader kapalı, Security Level makul olmalı.
