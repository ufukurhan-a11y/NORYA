# Canlıda (noryaai.com) Değişiklikler Görünmüyorsa

Push yaptıktan sonra canlı sitede güncellemeler görünmüyorsa aşağıdakileri sırayla kontrol edin.

## 1. Render deploy tamamlandı mı?

- **https://dashboard.render.com** → **norya** servisini açın.
- **Events** veya **Logs** sekmesinde son deploy’a bakın:
  - **Building** / **Deploying** ise bitmesini bekleyin (birkaç dakika).
  - **Failed** ise log’a tıklayıp hata mesajını okuyun; düzeltip tekrar push veya **Manual Deploy** yapın.
  - **Live** (yeşil) ise deploy tamamlanmış demektir; sorun büyük ihtimalle cache (aşağıdaki adımlar).

## 2. Render build cache

Bazen eski katman kullanılır, yeni kod image’a girmeyebilir.

- Render’da servis sayfasında **Manual Deploy** → **Clear build cache & deploy** seçin.
- Build’in bitmesini bekleyin.

## 3. Cloudflare cache

noryaai.com Cloudflare arkasındaysa HTML uzun süre cache’lenebilir.

- **https://dash.cloudflare.com** → **noryaai.com** → **Caching** → **Configuration**.
- **Purge Everything** ile tüm cache’i temizleyin (veya **Custom Purge** ile sadece `https://noryaai.com` ve `https://noryaai.com/` ekleyin).
- Birkaç dakika sonra siteyi tekrar açıp deneyin.

## 4. Tarayıcı cache

- **Sert yenileme:** Windows’ta `Ctrl+Shift+R`, Mac’te `Cmd+Shift+R`.
- Veya **Gizli/Incognito** pencerede https://noryaai.com açın.

## 5. Doğrulama

Yeni içerik yüklendiğinde aşağıdakiler görünür:

- Ana sayfada en altta **İletişim ve Şirket Bilgileri** bölümü (NoryaAI, Ufuk Urhan, +90 507 170 35 64, support@ / info@, adres).
- **https://noryaai.com/legal/iletisim** sayfasında Yetkili Kişi, Ticari Ünvan, Vergi Bilgileri vb. tüm başlıklar dolu.

---

**Özet:** Önce Render’da deploy’un **Live** olduğundan emin olun; sonra Cloudflare **Purge** ve tarayıcıda **sert yenileme** yapın.
