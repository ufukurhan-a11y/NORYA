# Norya 7/24 Açık Kalması (Yolculukta / Dışarıdayken)

Bilgisayarın kapalı veya uyku modunda olduğunda uygulama çalışmaz. **Sürekli açık** kalması için Norya’yı **bulutta** çalıştırman gerekir.

## Önerilen: Render’a deploy

Projede zaten hazır: **docs/RENDER-DEPLOY.md**

1. **render.com** → GitHub ile giriş → Repo: **NORYA**.
2. **Web Service** oluştur, env değişkenlerini ekle (OPENAI_API_KEY, SECRET_KEY, FRONTEND_URL, CORS_ORIGINS, vb.).
3. Deploy bittikten sonra **norya-xxxx.onrender.com** (veya kendi domain’in **noryaai.com**) 7/24 açık olur.
4. Bilgisayarını kapatıp yolculuğa çıksan bile site erişilebilir kalır.

**Not:** Render **Free** planda yaklaşık 15 dakika işlem yoksa uyur; ilk istekte uyanır (birkaç saniye gecikme). Kesintisiz 7/24 için **ücretli** plan (Starter vb.) kullan.

## Alternatifler

- **Railway.app** – Benzer şekilde GitHub repo bağlayıp deploy.
- **Fly.io** – `fly launch` ile deploy (Dockerfile var).
- **VPS** (DigitalOcean, Hetzner, vb.) – Sunucu kiralayıp `./start-background.sh` + systemd veya Docker ile sürekli çalıştırırsın.

## Özet

| Nerede çalışıyor? | 7/24 açık mı? |
|-------------------|----------------|
| Kendi bilgisayarında (start.sh) | Hayır – bilgisayar/sleep = kapanır |
| Kendi bilgisayarında (start-background.sh) | Hayır – bilgisayar kapanınca yine durur |
| **Render / Railway / VPS** | **Evet** – sunucu sürekli açık |

Yolculukta da açık kalsın istiyorsan: **Render’a deploy et** (detay: **docs/RENDER-DEPLOY.md**).
