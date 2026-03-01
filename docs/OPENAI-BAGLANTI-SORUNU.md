# OpenAI Bağlantı Hatası Çözümü

Admin panelinde **"AI servisine bağlanılamadı"** veya **Connection error** görüyorsanız aşağıdaki adımları uygulayın.

## 1. Bağlantıyı test edin

Proje kökünde:

```bash
.venv/bin/python scripts/test_openai_connection.py
```

Script şunları kontrol eder:
- `.env` içinde `OPENAI_API_KEY` var mı (sk- ile başlamalı)
- `api.openai.com:443` erişilebiliyor mu
- Gerçek bir API isteği başarılı mı

## 2. .env kontrolü

- `OPENAI_API_KEY=sk-...` satırı **başında/sonunda boşluk** olmamalı.
- Birden fazla anahtar: `OPENAI_API_KEYS=sk-1,sk-2` (virgülle ayrılmış).

## 3. Ağ / firewall

- Sunucu veya bilgisayarınız **api.openai.com** adresine çıkış yapabiliyor olmalı.
- Kurumsal ağdaysanız proxy gerekebilir:
  ```bash
  export HTTPS_PROXY=http://proxy.sirket.com:8080
  ```
- VPN veya farklı bir ağdan (örn. mobil hotspot) deneyin.

## 4. OpenAI hesabı

- [platform.openai.com](https://platform.openai.com) → API keys: Anahtar **silinmemiş** olmalı.
- Billing: Kredi eklenmiş veya kullanım limiti aşılmamış olmalı.

## 5. Admin’de “Yenile” ve önbellek

Dashboard’daki **AI Durumu** kutusu sonucu **60 saniye** önbelleklenir. Geçici ağ dalgalanmasında hata görebilirsiniz; **Yenile** butonuna basın veya 1 dakika bekleyip sayfayı yenileyin.

## 6. Admin raporları

**Raporlar** sayfası (tarih aralığı, CSV indir) OpenAI’e bağlı **değildir**. Bağlantı hatası sadece **AI Durumu** kutusunu ve **kan tahlili analizi** özelliğini etkiler. Rapor almak için Admin → Raporlar’ı kullanmaya devam edebilirsiniz.
