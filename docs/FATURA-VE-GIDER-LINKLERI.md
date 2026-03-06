# Fatura ve Gider Linkleri — Tek Sayfadan Erişim

Tüm abonelik/fatura sayfalarına buradan tek tek tıklayarak ulaşabilirsiniz. Faturaları aylık indirip **tek bir klasöre** (örn. `Faturalar/2025-03`) koyarak muhasebeciye verebilirsiniz.

---

## Hızlı linkler (tek tıkla fatura / ödeme geçmişi)

| Servis | Fatura / Ödeme geçmişi sayfası | Not |
|--------|--------------------------------|-----|
| **PayTR** | [Üye İşyeri Paneli → İşlemler / Raporlar](https://www.paytr.com) | Giriş: Mağaza No + şifre. Tahsilat raporu, işlem listesi. |
| **Render** | [Dashboard → Billing](https://dashboard.render.com/billing) | Fatura indir: Billing → Invoices / Usage. |
| **Cursor** | [Cursor Settings → Subscription / Billing](https://cursor.com/settings) veya e-posta ile gelen faturalar | Abonelik ve fatura bilgisi. |
| **ChatGPT / OpenAI** | [Usage → Billing](https://platform.openai.com/account/billing) | API kullanımı, kredi, faturalar. |
| **Cloudflare** | [Billing & Usage](https://dash.cloudflare.com/?to=/:account/billing) | Faturalar, kullanım özeti. |
| **Google (Analytics & Ads)** | [Google Ads Billing](https://ads.google.com/aw/billing) | Ads kullanım varsa fatura. Analytics ücretsiz. |
| **GİB e-Arşiv** | [E-Arşiv Portal](https://earsivportal.efatura.gov.tr) | E-arşiv fatura girişi, döküm. |
| **Domain (alan adı)** | Alan adınızı aldığınız yer (Cloudflare, Namecheap, GoDaddy vb.) | Yıllık yenileme faturası. |
| **E-posta (SMTP)** | Kullandığınız servis (SendGrid, Resend, Mailgun, Gmail vb.) | Şifre sıfırlama mailleri için. |

---

## Başka neler olabilir?

Aklınıza gelirse ekleyebileceğiniz yaygın servisler: GitHub (Copilot/Team), Sentry, Vercel/Netlify, 1Password/LastPass, Notion/Slack, Figma, banka (PayTR tahsilat hesabı / kredi kartı).

---

## Aylık toplama listesi (muhasebeciye vermek için)

Her ay bu listeyi takip edip faturaları tek klasöre indirin:

```
[ ] PayTR       — Panelden işlem/rapor export
[ ] Render      — Billing → Invoices → PDF indir
[ ] Cursor      — E-posta faturası veya Settings
[ ] OpenAI      — Billing → Invoices / Usage → PDF
[ ] Cloudflare  — Billing → Invoices → İndir
[ ] Google Ads  — Fatura varsa indir
[ ] GİB e-Arşiv — Gerekirse rapor
[ ] Domain      — Alan adı yenileme (yıllık)
[ ] E-posta     — SMTP servisi (SendGrid, Resend vb.)
```

**Klasör örneği:** `Faturalar/2025-03` içine `PayTR-Mart2025.pdf`, `Render-Mart2025.pdf` vb. koyun; zipleyip veya klasörü muhasebeciye gönderin.

---

## Doğrudan URL’ler (kopyala-yapıştır)

- **PayTR:** https://www.paytr.com  
- **Render Billing:** https://dashboard.render.com/billing  
- **Cursor:** https://cursor.com/settings (veya e-posta faturaları)  
- **OpenAI Billing:** https://platform.openai.com/account/billing  
- **Cloudflare Billing:** https://dash.cloudflare.com/?to=/:account/billing  
- **Google Ads Billing:** https://ads.google.com/aw/billing  
- **GİB e-Arşiv:** https://earsivportal.efatura.gov.tr  

---

## Tek panelde hepsini gösteren uygulama var mı?

**Hayır.** PayTR, Render, Cursor, OpenAI ve Cloudflare’ın faturalarını **tek bir resmi dashboard’da** toplayan ortak bir servis yok. Her biri kendi sitesinde fatura sunar.

**Pratik çözüm:**  
Bu sayfayı (veya bu sayfadaki linkleri) “tek adres” olarak kullanın; her ay buradan sırayla her servise girip fatura indirin ve hepsini **tek bir klasörde** toplayın. İsterseniz klasörü `Faturalar/Ay-Yil` şeklinde açıp muhasebeciye tek zip/klasör olarak verebilirsiniz.
