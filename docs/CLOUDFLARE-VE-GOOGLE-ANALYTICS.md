# Cloudflare ve Google Analytics — Norya

## Cloudflare: Farkı ne, ne işe yarar?

**Cloudflare** birkaç farklı ürün sunar; karışan kısım da bu.

| Ürün | Ne işe yarar? | Norya için gerekli mi? |
|------|----------------|-------------------------|
| **Cloudflare DNS** | Domain’in isim sunucusu (NS). Alan adını norya.com’a yönlendirir; A/CNAME kayıtlarını burada yönetirsin. | Evet — domain aldıktan sonra DNS için kullanılabilir. |
| **Cloudflare Proxy (CDN)** | Trafik Cloudflare üzerinden geçer: DDoS koruma, önbellek, SSL. “Turuncu bulut” = proxy açık. | İsteğe bağlı — hem hız hem koruma sağlar. |
| **Cloudflare Registrar** | Sadece **domain satın alma** ( .com vb.). Fiyat maliyet fiyatına yakın; DNS sonradan Cloudflare’e taşınabilir. | İsteğe bağlı — domain’i başka yerden de alabilirsin. |

**Kısa cevap:** “Cloudflare” deyince çoğu zaman **DNS + proxy (CDN)** birlikte kullanılır: Domain’i Cloudflare’e bağlarsın, siten hem hızlanır hem korunur. Registrar ise sadece domain alma yeri; Norya’nın çalışması için şart değil.

---

## Cloudflare kurulum (DNS + proxy, domain hazırken)

1. **cloudflare.com** → Hesap aç / giriş yap.
2. **Add site** → Alan adını yaz (örn. norya.com) → Plan seç (ücretsiz yeterli).
3. Cloudflare, mevcut DNS kayıtlarını tarar; onayla.
4. **Nameservers**: Cloudflare iki NS adresi verir (örn. `ada.ns.cloudflare.com`, `bob.ns.cloudflare.com`). Bu adresleri **domain’i aldığın yerde** (Turhost, Namecheap vb.) “Nameserver” olarak kaydet. Böylece domain’in DNS’i Cloudflare’e taşınmış olur.
5. Cloudflare **DNS** sekmesinde:
   - **A** kaydı: `@` → sunucu IP’n.
   - **A** veya **CNAME**: `www` → sunucu IP’n veya `@`.
6. **SSL/TLS**: “Full” veya “Full (strict)” seç (sunucuda HTTPS açıksa “Full (strict)”).
7. **Proxy** (turuncu bulut): Açık bırakırsan trafik Cloudflare’den geçer (önbellek + koruma). İstemezsen “DNS only” (gri bulut) yaparsın.

Bu adımlardan sonra norya.com, sunucuna Cloudflare üzerinden gider; Norya uygulamasında ekstra kod gerekmez.

---

## Google Analytics 4 (GA4)

Norya’da GA4, **.env** üzerinden açılıyor; kod tarafı hazır.

### 1. GA4 ölçüm kimliği al

1. **analytics.google.com** → Hesap / Mülk oluştur.
2. **Veri akışı** → Web → Site URL’ini yaz (örn. https://norya.com).
3. **Ölçüm kimliği** (Measurement ID) kopyala: `G-XXXXXXXXXX` formatında.

### 2. Norya’da ayarla

Sunucudaki **.env** dosyasına ekle:

```env
GA_MEASUREMENT_ID=G-XXXXXXXXXX
```

Uygulamayı yeniden başlat. Ana sayfa (/) sunulurken bu ID enjekte edilir; diğer sayfalar SPA olduğu için aynı sayfa içinde gezinmeler de GA’da toplanır (sayfa yenilenmeden yapılan tıklamalar için GA4’ün otomatik topladığı etkileşimler kullanılır).

### 3. Kontrol

Tarayıcıda siteyi aç → Geliştirici araçları (F12) → Network → “gtag” veya “google-analytics” filtrele; istekler gidiyorsa GA çalışıyordur. Birkaç dakika sonra Analytics panelinde “Gerçek zamanlı” bölümünde ziyaret görünebilir.

---

## Özet

- **Cloudflare:** DNS + isteğe bağlı proxy (CDN). Domain’i Cloudflare’e bağlayıp A/CNAME ve SSL ayarlarını yap; Norya’da ekstra bir şey yapma.
- **Google Analytics:** .env’e `GA_MEASUREMENT_ID=G-XXXXXXXXXX` yaz; ana sayfa otomatik GA4 yükler.

Bu dosya projede kalacak; domain ve GA kimliğini aldığında yukarıdaki adımlarla tamamlarsın.
