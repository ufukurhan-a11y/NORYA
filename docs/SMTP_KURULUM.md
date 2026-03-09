# SMTP Nasıl Açılır? (E-posta gönderimi)

Norya’da **üyelik doğrulama** ve **şifre sıfırlama** mailleri SMTP ile gider. SMTP’yi açmak için proje kökündeki **`.env`** dosyasına aşağıdaki değişkenleri eklemeniz yeterli.

---

## 1. Hangi değişkenler gerekli?

| Değişken | Zorunlu | Açıklama |
|----------|---------|----------|
| `SMTP_HOST` | Evet | SMTP sunucu adresi (örn. `smtp.gmail.com`) |
| `SMTP_USER` | Evet | Giriş kullanıcı adı (genelde e-posta) |
| `SMTP_PASSWORD` | Evet | Şifre veya uygulama şifresi |
| `SMTP_PORT` | Hayır | Varsayılan: `587` (TLS) |
| `SMTP_FROM` | Hayır | Gönderen adres (varsayılan: `noreply@norya.com`) |
| `SMTP_FROM_NAME` | Hayır | Gönderen adı (varsayılan: `Norya`) |
| `SMTP_USE_TLS` | Hayır | `1` = TLS kullan (varsayılan), `0` = kullanma |
| `FRONTEND_URL` | Önerilir | E-postadaki linklerin açılacağı site (örn. `https://noryaai.com`) |

**SMTP açık sayılması için:** `SMTP_HOST`, `SMTP_USER` ve `SMTP_PASSWORD` dolu olmalı. Uygulama başlarken logda “SMTP yapılandırıldı” veya “SMTP yapılandırılmadı” mesajını görebilirsiniz.

---

## 2. Mevcut mail hesabınız: support@noryaai.com

support@noryaai.com hesabınızı SMTP için kullanabilirsiniz. Önce bu hesabın **hangi sağlayıcıda** olduğunu bilmeniz gerekir (Google Workspace, Microsoft 365, hosting e-posta vb.).

### support@noryaai.com hangi sağlayıcıda?

- **Google Workspace (Gmail for work)** ise → Aşağıdaki “Gmail ile SMTP” bölümünü uygulayın; `SMTP_USER` ve `SMTP_FROM` olarak `support@noryaai.com` yazın. **Önemli:** Normal hesap şifresi yerine Google’da “Uygulama şifresi” oluşturup onu `SMTP_PASSWORD` olarak kullanın.
- **Hosting / cPanel / Plesk** (domain’i aldığınız yerde açılan e-posta) ise → Genelde sunucu `mail.noryaai.com` veya `smtp.noryaai.com`, port `587`. Hosting panelinde “E-posta hesapları” veya “SMTP ayarları”ndan bakın; kullanıcı adı tam e-posta (`support@noryaai.com`), şifre hesap şifreniz.
- **Microsoft 365 / Outlook** ise → SMTP sunucusu genelde `smtp.office365.com`, port `587`, kullanıcı `support@noryaai.com`, şifre hesap şifreniz (veya uygulama şifresi).

**.env örneği (support@noryaai.com ile):**

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=support@noryaai.com
SMTP_PASSWORD=your-app-password-or-account-password
SMTP_FROM=support@noryaai.com
SMTP_FROM_NAME=Norya
SMTP_USE_TLS=1
FRONTEND_URL=https://noryaai.com
```

- `SMTP_HOST` ve `SMTP_PORT` değerlerini sağlayıcınıza göre değiştirin (Google için `smtp.gmail.com` / 587, Office365 için `smtp.office365.com` / 587, hosting için `mail.noryaai.com` veya panelde yazan adres).
- Gönderen adresin **support@noryaai.com** olması için `SMTP_FROM=support@noryaai.com` kullanın; böylece doğrulama ve şifre sıfırlama mailleri bu adresten gider.

---

## 3. Gmail / Google Workspace (support@noryaai.com)

support@noryaai.com Gmail veya Google Workspace’te ise:

1. **support@noryaai.com** ile Google Hesabına giriş yapın.
2. **2 Adımlı Doğrulama** açık olmalı. Açık değilse: https://myaccount.google.com/security
3. **Uygulama şifresi** oluşturun: https://myaccount.google.com/apppasswords  
   - “Uygulama seç” → **Diğer (özel ad)** → “Norya” yazın → **Oluştur**.  
   - Çıkan **16 karakterlik şifreyi** kopyalayın (aradaki boşlukları silerek tek parça yazın).
4. Proje kökündeki **`.env`** dosyasına ekleyin:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=support@noryaai.com
SMTP_PASSWORD=abcdefghijklmnop
SMTP_FROM=support@noryaai.com
SMTP_FROM_NAME=Norya
SMTP_USE_TLS=1
FRONTEND_URL=https://noryaai.com
```

- `SMTP_PASSWORD`: Az önce oluşturduğunuz **uygulama şifresi** (normal Gmail şifrenizi yazmayın).  
- Uygulama şifresi tek sefer gösterilir; kaydedin. Unutursanız yeni bir tane oluşturup `.env`’i güncelleyin.

---

## 4. SendGrid ile SMTP

1. https://sendgrid.com üzerinden hesap açın.
2. **Settings → Sender Authentication** ile tek gönderici (Single Sender) veya domain doğrulaması yapın.
3. **Settings → API Keys** → Create API Key → “Restricted” veya “Full” → bir isim verin; **API Key** oluşturulunca kopyalayın (bir daha gösterilmez).
4. SendGrid SMTP bilgileri:  
   - Sunucu: `smtp.sendgrid.net`  
   - Port: `587`  
   - Kullanıcı: `apikey` (kelimenin kendisi)  
   - Şifre: az önce kopyaladığınız API Key  

`.env` örneği:

```env
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
SMTP_PASSWORD=SG.xxxxxxxxxxxxxxxxxxxxxxxx
SMTP_FROM=donotreply@yourdomain.com
SMTP_FROM_NAME=Norya
SMTP_USE_TLS=1
FRONTEND_URL=https://noryaai.com
```

`SMTP_FROM` adresinin doğruladığınız domain’e ait olması gerekir.

---

## 5. Resend ile SMTP

1. https://resend.com hesap açın.
2. **Domains** kısmında gönderim yapacağınız domain’i ekleyip DNS kayıtlarını tamamlayın.
3. **API Keys** → Create API Key → oluşan anahtarı kopyalayın.
4. Resend SMTP:  
   - Sunucu: `smtp.resend.com`  
   - Port: `465` veya `587`  
   - Kullanıcı: `resend`  
   - Şifre: API Key  

`.env` örneği:

```env
SMTP_HOST=smtp.resend.com
SMTP_PORT=587
SMTP_USER=resend
SMTP_PASSWORD=re_xxxxxxxxxxxxxxxx
SMTP_FROM=onboarding@yourdomain.com
SMTP_FROM_NAME=Norya
SMTP_USE_TLS=1
FRONTEND_URL=https://noryaai.com
```

---

## 6. Başka bir SMTP sunucusu

Kendi sunucunuz veya farklı bir sağlayıcı (Yandex, Outlook, hosting SMTP vb.) kullanıyorsanız:

- `SMTP_HOST`: sunucu adresi  
- `SMTP_PORT`: genelde `587` (TLS) veya `465` (SSL)  
- `SMTP_USER` / `SMTP_PASSWORD`: sunucunun verdiği kullanıcı ve şifre  
- TLS kullanıyorsanız `SMTP_USE_TLS=1`

Örnek:

```env
SMTP_HOST=mail.yourdomain.com
SMTP_PORT=587
SMTP_USER=noreply@yourdomain.com
SMTP_PASSWORD=your-password
SMTP_FROM=noreply@yourdomain.com
SMTP_FROM_NAME=Norya
SMTP_USE_TLS=1
FRONTEND_URL=https://noryaai.com
```

---

## 7. Kontrol

1. `.env` dosyasını kaydedin.
2. Uygulamayı yeniden başlatın: `uvicorn app.main:app --reload` (veya canlı sunucudaki başlatma komutu).
3. Logda şuna benzer bir satır görmelisiniz:  
   `E-posta (şifre sıfırlama): SMTP yapılandırıldı, gerçek mail gönderilecek.`
4. Test için: Sitede “Şifremi unuttum” ile e-posta adresinizi yazıp gönderin; gelen kutusunu (ve spam’i) kontrol edin.

---

## Özet

- SMTP’yi **açmak** = `.env` içinde `SMTP_HOST`, `SMTP_USER`, `SMTP_PASSWORD` doldurmak.
- Gmail için **uygulama şifresi**, SendGrid/Resend için **API Key** kullanın.
- Canlı sitede `FRONTEND_URL` mutlaka `https://noryaai.com` (veya kendi domain’iniz) olmalı; yoksa e-postadaki linkler yanlış sayfaya gider.

Bu ayarlarla hem üyelik doğrulama hem şifre sıfırlama mailleri gider.
