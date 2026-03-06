# Render'da PayTR Ortam Değişkenleri

Canlıda "Ödeme şu an aktif değil" hatasını kaldırmak için Render Dashboard'da bu değişkenleri ekleyin.

## Adımlar

1. https://dashboard.render.com → **norya** servisini açın.
2. Sol menüden **Environment** (Ortam Değişkenleri) sayfasına girin.
3. **Add Environment Variable** ile aşağıdaki satırları **tek tek** ekleyin (Key ve Value'yu kopyalayın).

## Eklenecek değişkenler

| Key | Value | Açıklama |
|-----|--------|----------|
| `PAYTR_MERCHANT_ID` | `677898` | PayTR Mağaza No |
| `PAYTR_MERCHANT_KEY` | *(PayTR panelden Mağaza Parola)* | Gizli tutun |
| `PAYTR_MERCHANT_SALT` | *(PayTR panelden Mağaza Gizli Anahtar)* | Gizli tutun |
| `PAYTR_TEST_MODE` | `1` | Test için 1, canlı ödeme için 0 |
| `PAYTR_EUR_TO_TRY_RATE` | `35` | TL tahsilat için (1 EUR = 35 TL). EUR hesaba geçince `0` yapın |

**Not:** `PAYTR_MERCHANT_KEY` ve `PAYTR_MERCHANT_SALT` değerlerini PayTR Üye İşyeri Paneli → Entegrasyon Bilgileri sayfasından alın. Yerel .env dosyanızda aynı değerler varsa oradan da kopyalayabilirsiniz.

4. Kaydettikten sonra Render servisi otomatik yeniden başlar. Birkaç dakika sonra https://noryaai.com üzerinde ödeme açık olacaktır.

## "Geçersiz istek veya mağaza aktif değil" hatası

Bu mesaj **PayTR API**'sinden döner. Genelde şu nedenlerle olur:

- **Mağaza henüz aktif değil:** PayTR Üye İşyeri Panelinde mağazanızın aktif ve ödeme almaya açık olduğundan emin olun.
- **Yanlış entegrasyon bilgileri:** `PAYTR_MERCHANT_ID`, `PAYTR_MERCHANT_KEY`, `PAYTR_MERCHANT_SALT` değerlerini PayTR → Entegrasyon Bilgileri sayfasından tekrar kopyalayın (başında/sonunda boşluk olmamalı).
- **Test / canlı uyumsuzluğu:** Test ortamı için panelde test modunun açık olması ve `PAYTR_TEST_MODE=1` kullanmanız gerekir. Canlı için `PAYTR_TEST_MODE=0` ve panelde canlı ödemeye izin verilmiş olmalı.
