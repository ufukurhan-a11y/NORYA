# Norya — Tek Analiz, Aylık ve Yıllık Paketler

Bu dokümanda üç paket tek sayfada özetleniyor: **Tek Analiz**, **Aylık Abonelik**, **Yıllık Abonelik**.

---

## Uygulamada nerede görünür?

| Nerede | URL / Erişim |
|--------|----------------|
| **Ödeme sayfası** (3 plan butonu + fiyat) | `/pay` veya `/pay?plan=single_13eur` / `monthly_50eur` / `yearly_99eur` |
| **Fiyatlandırma (SPA)** | `/pricing` veya `/#fiyatlandirma` / `/#pricing` |
| **Fiyat API (JSON)** | `GET /api/pricing` — ülkeye göre single, monthly, yearly fiyatları döner |

Tarayıcıda paketleri görmek için: **`http://127.0.0.1:8000/pay`** (veya canlı site adresiniz + `/pay`).

---

## Paket özeti (kod tanımları)

| Paket | Plan kodu | Ürün (product) | Fiyat (EUR) | PayTR amount (cent) |
|-------|-----------|-----------------|-------------|--------------------|
| **Tek Analiz** | `single_13eur` | `single` | 13 € | 1300 |
| **Aylık Abonelik** | `monthly_50eur` | `monthly` | 50 € | 5000 |
| **Yıllık Abonelik** | `yearly_99eur` | `yearly` | 99 € | 9900 |

- **Fiyatlar:** `app/main.py` → `EUR_BASE = {"single": 13, "monthly": 50, "yearly": 99}`
- **Plan kodları:** `app/main.py` → `PAYTR_PLAN_CODES` (single_13eur, monthly_50eur, yearly_99eur)

---

## Plan isimleri (çok dil)

- **TR:** Tek Analiz, Aylık Abonelik, Yıllık Abonelik  
- **EN:** Single Analysis, Monthly Subscription, Yearly Subscription  
- **DE/FR/IT/ES:** `app/pay_i18n.py` → `PAY_UI` içinde `plan_single`, `plan_monthly`, `plan_yearly`

---

## Paket faydaları (benefits)

- **Tek Analiz:** 1 analiz, Health Score, PDF, diyet/yaşam tarzı önerileri  
- **Aylık:** Ayda 5 analiz, karşılaştırma, PDF, öncelikli destek  
- **Yıllık:** Ayda 5 analiz (yıllık), tüm Pro özellikleri, 2 ay bedava, en avantajlı fiyat  

Tam liste: `app/pay_i18n.py` → `PLAN_BENEFITS` (`single`, `monthly`, `yearly`).

---

## QR doğrulama hangi paketlerde?

- **QR doğrulama (PDF’de QR + `/verify/...`):** **Tek Analiz**, **Aylık** ve **Yıllık** pakette. Müşteri PDF'deki QR ile raporun doğruluğunu ve orijinalliğini doğrulayabilir.  
- **Ücretsiz:** PDF’de QR yok. Ayrıntı: `docs/QR-DOGRULAMA.md`

Özet: **Tek analizi, aylık ve yıllık paketleri uygulamada `/pay` sayfasından, kodda ise `app/main.py` (EUR_BASE, PAYTR_PLAN_CODES) ve `app/pay_i18n.py` (PLAN_BENEFITS, plan isimleri) içinden takip edebilirsiniz.

---

## Sonuçları PDF olarak nereden görebilirim?

PDF raporlar **bu dokümanın içinde** açılmaz; aşağıdaki yerlerden **PDF dosyasını indirip** görüntüleyebilirsiniz.

| Nereden | Nasıl |
|--------|--------|
| **Uygulama (kullanıcı)** | Giriş yap → **Analiz geçmişi** → ilgili raporun yanında **Raporu İndir** / **PDF**. Tarayıcıda açılır veya indirilir. |
| **Örnek PDF (test)** | Proje kökünde: `python scripts/test_premium_pdf.py` çalıştırın → `test_premium_report.pdf` oluşur. QR’lı örnek için: `python scripts/test_premium_pdf.py --qr`. |
| **Admin paneli** | `/admin` → **Analizler** → listede her satırda **Norya raporu** linki → tıklayınca o analizin PDF’i açılır. |

**API ile PDF almak:**  
- `POST /analyze/history/{analysis_id}/pdf-token` ile 5 dakika geçerli token alınır (giriş gerekli).  
- `GET /analyze/history/{analysis_id}/pdf?access_token=...` veya `Authorization: Bearer ...` ile PDF indirilir.

**Kısa cevap:** Evet, sonuçları PDF olarak görebilirsiniz; dokümandan değil, **uygulamadaki “Raporu İndir”**, **admin panelindeki “Norya raporu”** veya **test scripti** (`scripts/test_premium_pdf.py`) ile.

---

## Raporu buradan (Cursor'dan) PDF olarak görmek

| Ne yapmak istiyorsunuz? | Nasıl? |
|-------------------------|--------|
| **Örnek raporu hemen açmak** | Sol dosya ağacında **`test_premium_report.pdf`** dosyasına tıklayın (proje kökünde). Cursor PDF'i önizler veya varsayılan uygulamada açar. |
| **PDF yoksa / yeniden oluşturmak** | Terminalde: `cd /Users/ufukurhan/norya` sonra `python3 scripts/test_premium_pdf.py` (veya `.venv/bin/python scripts/test_premium_pdf.py`). Oluşan dosya: `test_premium_report.pdf`. |
| **QR'lı örnek** | `python3 scripts/test_premium_pdf.py --qr` → yine `test_premium_report.pdf` güncellenir. **QR kodu raporda sadece bu komutla üretilen PDF’te görünür;** `--qr` olmadan çalıştırırsanız doğrulama kutusu yer almaz. |
| **Sistemde PDF'i açmak** | Terminalde: `open test_premium_report.pdf` (macOS) veya `xdg-open test_premium_report.pdf` (Linux). |

---

## Analiz et bölümüne gitmek — Raporu ekrandan buradan görmek

Raporu **Analiz et** adımından çalıştırıp ekranda görmek için uygulamayı açıp doğrudan analiz bölümüne gidebilirsiniz.

| Ne yapmak istiyorsunuz? | Nasıl? |
|-------------------------|--------|
| **Analiz et bölümüne doğrudan gitmek** | Uygulama çalışıyorken tarayıcıda açın: **[http://127.0.0.1:8000/#analyze-section](http://127.0.0.1:8000/#analyze-section)** (localhost). Veya ana sayfada **Analiz Yap** butonuna tıklayın; aynı bölüme gider. |
| **Raporu hangi dilde görmek** | Sayfada dil seçin (TR, EN, DE, FR, ES, IT vb.); analiz ve rapor seçtiğiniz dilde üretilir. PDF indirme de o dilde olur. |
| **Uygulama kapalıysa** | Terminalde: `cd /Users/ufukurhan/norya` sonra `uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000` (veya `.venv/bin/uvicorn app.main:app --reload --port 8000`). Ardından tarayıcıda **http://127.0.0.1:8000/#analyze-section** açın. |

**Kısa yol:** Buradan raporu görmek için tarayıcıda **http://127.0.0.1:8000/#analyze-section** adresini açın → tahlil metni yapıştırın veya PDF/görsel yükleyin → **Analiz Et** → Sonuç ekranında rapor (ve istersen **Raporu İndir** ile PDF) seçtiğiniz dilde görünür.

---

## Kartları da buradan görmek (fiyatlandırma, Elite, özellik kartları)

Ana sayfadaki ve ödeme sayfasındaki **kartları** (paket kartları, Elite hero kartı, özellik/güven kartları, QR tanıtımı) tarayıcıda açarak görebilirsiniz. Uygulama çalışıyorken aşağıdaki linkleri kullanın.

| Kartlar | Tarayıcıda açın |
|--------|------------------|
| **Fiyatlandırma kartları** (Tek Analiz, Aylık, Yıllık) | **http://127.0.0.1:8000/#fiyatlandirma** veya **http://127.0.0.1:8000/pay** |
| **Elite hero kartı** (Health Score, PDF, QR doğrulama vb.) | **http://127.0.0.1:8000/** → sayfada aşağı kaydırın, "ELITE HEALTH REPORT" kartı |
| **Özellik kartları** (6’lı grid: analiz, rapor, gizlilik vb.) | **http://127.0.0.1:8000/#ozellikler** |
| **Güven kartları** (SSL, KVKK, PayTR, **QR doğrulama**) | **http://127.0.0.1:8000/** → hero altı rozetler + "Güven ve tasarım" listesi + "Global standards" pill’leri |
| **Rapor PDF’indeki kartlar** (özet kartları, skor kartı, QR doğrulama kutusu) | Sol dosya ağacında **`test_premium_report.pdf`**’e tıklayın veya terminalde **`open test_premium_report.pdf`** (macOS). PDF’in ilk sayfasında: Genel Sağlık Skoru kartı, 4’lü özet kartları, **Rapor Doğrulama** (QR) kutusu. **QR’ı görmek için** PDF’i önce **`python3 scripts/test_premium_pdf.py --qr`** ile oluşturun. |

**Uygulama kapalıysa:** Önce `uv run uvicorn app.main:app --reload --port 8000` (veya `.venv/bin/uvicorn app.main:app --reload --port 8000`) çalıştırın, sonra yukarıdaki linkleri açın.

**Özet:** Evet, kartları da buradan görebilirsiniz; tarayıcıda **http://127.0.0.1:8000/** ve **http://127.0.0.1:8000/#fiyatlandirma** / **http://127.0.0.1:8000/pay** adreslerini açmanız yeterli.
