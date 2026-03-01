# Norya — Deploy Nasıl Yapılır?

## Render kullanıyorsanız (noryaai.com)

Deploy = GitHub’a push. Render repo’ya bağlıysa otomatik build alır ve canlıyı günceller.

### Tek komut (önerilen)

```bash
cd /Users/ufukurhan/norya
chmod +x deploy/deploy.sh
./deploy/deploy.sh
```

- Değişiklik varsa: commit + push yapar (mesajı sorar veya “Deploy: tarih” kullanır).
- Değişiklik yoksa: sadece push yapıp yapmayacağını sorar.

İstersen commit mesajını komutla da verebilirsin:

```bash
./deploy/deploy.sh "PDF canlıda token ile açılıyor"
```

### Elle deploy

```bash
cd /Users/ufukurhan/norya
git add -A
git status
git commit -m "Deploy: PDF canlıda düzeltmesi"
git push origin main
```

Push sonrası **Render Dashboard** → **norya** servisi → **Logs**’tan build’i izleyebilirsin. Bittiğinde canlı site güncel olur.

---

## VPS kullanıyorsanız (kendi sunucunuz)

Sunucuda proje dizininde:

```bash
cd /var/www/norya   # veya projenin olduğu dizin
git pull origin main
sudo systemctl restart norya   # veya ./restart-server.sh
```

Lokalde sunucuya bağlanıp çekmek için (SSH ile):

```bash
ssh kullanici@sunucu-ip "cd /var/www/norya && git pull origin main && sudo systemctl restart norya"
```
