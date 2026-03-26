# Google Search Console — haftalık kontrol listesi (NoryaAI)

Bu checklist, **her hafta aynı gün** ~20–30 dakikada tekrarlanacak şekilde tasarlandı. Amaç: index sorunlarını erken görmek, **yüksek gösterim + düşük CTR** fırsatlarını yakalamak, manuel işlem / uyarıları takip etmek.

## Ön koşullar

- [ ] Property doğrulandı (`https://noryaai.com` veya kullandığın canonical domain).
- [ ] `https://noryaai.com/sitemap.xml` **Sitemaps** altında gönderildi ve “Success” durumunda.
- [ ] Gerekirse hem **domain property** hem **URL prefix** ile aynı siteyi izle (tercihen domain).

## 1) Performans (Search results) — ~10 dk

| Adım | Ne bak |
| --- | --- |
| 1.1 | Son **3 ay** (veya 16 ay) görünürlük: toplam tıklama, gösterim, ort. CTR, ort. pozisyon. |
| 1.2 | **Sayfalar** sekmesi: gösterimde ilk 20 URL’yi aç; CTR %1’in altında kalanları işaretle. |
| 1.3 | **Sorgular** sekmesi: aynı döneme göre marka dışı sorgulara bak; hangi URL eşleşiyor not al. |
| 1.4 | Dil/ülke: filtrede **ülke** veya **arama görünümü** ile “anlamlı fark” var mı kontrol et. |

**Çıktı (her hafta 3 satır yeter):**

- URL veya sorgu → “CTR düşük, title/meta denemesi adayı”.
- URL → “pozisyon iyi, snippet güçlendir” veya “içerik güncellemesi”.

Bu çıktıyı `docs/30-GUNLUK-HIZLANDIRMA-PLANI.md` ile hizala: deploy sonrası 2–4 hafta bekle, sonra snippet’i tek değişkenle test et.

## 2) Dizin oluşturma (Indexing) — ~5 dk

- [ ] **Pages** → “Why pages aren’t indexed” özeti: yeni artış var mı?
- [ ] **Sitemaps** → “Discovered URLs” / hata sayısı.
- [ ] Örnek: `Excluded by ‘noindex’` veya `Crawled – currently not indexed` ani yükseldiyse ilgili şablon / header kontrolü (staging karışması, yanlış canonical vb.).

## 3) Deneyim (Experience) — ~3 dk

- [ ] **Core Web Vitals** (veya Page Experience): mobilde “Poor” URL sayısı artışı.
- [ ] Sorun varsa: hangi template / hangi büyük asset (görsel, script) — ticket notu.

## 4) Güvenlik ve manuel işlemler — ~2 dk

- [ ] **Security issues**: boş olmalı.
- [ ] **Manual actions**: boş olmalı.

## 5) Haftalık “tek aksiyon” kuralı

Her turda **en fazla 3 URL** için title veya meta açıklamasını değiştir; aynı hafta aynı URL’de ikinci büyük içerik revizyonu yapma (ölçümü kirletmemek için). Değişiklikleri repoda `seo_landing_i18n.py` / ilgili i18n dosyalarında tut; tarih + notu istersen bu dosyanın altına ekleyebilirsin.

### Son meta denemeleri (örnek — deploy tarihine göre güncelle)

Aynı CTR mantığı **9 dil** için uygulandı: EN + TR/DE (kanon slug’lar) + ES/FR/IT/HE/HI/AR (`blood-test-results`, `understand-lab-results`, `ai-blood-test-analyzer`).

| URL / eşdeğer | Not |
| --- | --- |
| `/en/blood-test-results` (ve `/es/…`, `/fr/…`, …) | “Explained” + PDF/foto yükleme vurgusu |
| `/tr/kan-tahlili-sonucu`, `/de/blutwerte-verstehen` | EN ile paralel niyet |
| `/tr/kan-degerleri-anlama`, `/de/laborwerte-verstehen` | “Nasıl okunur / Lesen” niyeti |
| `/en/understand-lab-results` (ve diğer diller) | Aralıklar + özet niyeti |
| `…/ai-blood-test-analyzer` (tüm diller) | PDF/foto + gerçek rapor / eğitim uyarısı |

---

**Özet cümle:** Bir haftada çok şey yapma; GSC’de **okuma + 3 snippet adayı** ile ritim kur. Büyüme takılıyorsa ikinci kanal `docs/OUTREACH-3-HAZIR-EMAIL.md`.
