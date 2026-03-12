# Yarın Yapılacak: CSP / Conversion (Cloudflare)

**Tarih:** 12 Mart 2026  
**Durum:** Ödemeler çalışıyor. Tag Assistant bazen script-src-elem / connect-src CSP hataları gösteriyor. Sunucu doğru CSP gönderiyor (curl ile doğrulandı); sorun büyük ihtimalle cache veya Cloudflare’da ekstra CSP.

---

## 1. Cloudflare

- **Page Rule ekle:**  
  URL: `*noryaai.com/payment/success*`  
  Ayar: **Cache Level → Bypass**  
  (Bu sayfa hiç cache’lenmesin.)

- **Transform Rules / Response Headers kontrol:**  
  **Content-Security-Policy** ekleyen veya değiştiren kural var mı bak.  
  Varsa **sil** veya bu kuralın **`/payment/success` için çalışmasın**.

- **Purge:** Caching → Purge Everything (veya en azından bu URL).

---

## 2. Doğrulama

1. **Gizli pencere** aç.
2. Sadece şu adresi aç: `https://noryaai.com/payment/success?merchant_oid=test123&lang=tr`
3. **F12** → **Network** → sayfayı **sert yenile** (Ctrl+Shift+R).
4. En üstteki **document** isteğine tıkla → **Headers** → **Response Headers**:
   - **X-Norya-CSP: payment-success** var mı?
   - **Content-Security-Policy** içinde **script-src-elem** ve **googleads.g.doubleclick.net** geçiyor mu?
   - **Content-Security-Policy** 2 kez geçiyorsa → Cloudflare ekstra CSP ekliyor.
5. **Tag Assistant** bu sekmede açıp CSP hatalarının gidip gitmediğine bak.

---

## Not

- Ödeme alımı bu konudan etkilenmiyor; sorun sadece reklam dönüşüm ölçümü / optimizasyon için önemli.
- Kod tarafı hazır: `app/main.py` içinde `_CSP_PAYMENT_SUCCESS` ve `/payment/success` için gevşek CSP uygulanıyor.
