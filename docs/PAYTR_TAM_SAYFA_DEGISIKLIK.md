# PayTR: iFrame Kaldırıldı, Tam Sayfa Yönlendirme

## Özet

- **Önce:** "Ödemeyi Başlat" tıklanınca sayfada gömülü iframe ile PayTR ödeme ekranı açılıyordu.
- **Sonra:** Aynı sekmede tam sayfa olarak PayTR güvenli ödeme sayfasına yönlendirme (`window.location.href`).

## Değişen Dosyalar

| Dosya | Değişiklik |
|-------|------------|
| `app/main.py` | `_paytr_canonical_base()` eklendi; PayTR success/fail URL'leri ve ödeme sayfası base_url tek canonical domain (noryaai.com / www uyumlu). Production'da `test_mode` zorunlu "0". iframe_v2 parametresi kaldırıldı. Init yanıtına `redirect_url` eklendi. Success/failed sayfaları canonical base kullanıyor. |
| `app/templates/payment_page.html` | iframe ile ilgili HTML (iframe-section, iframe-wrapper, paytr-iframe) kaldırıldı. İlgili CSS (iframe-section, iframe-wrapper, iframe-skeleton, paytr-iframe) ve medya sorguları kaldırıldı. JS: iframe referansları ve clearIframe kaldırıldı; başarılı init sonrası `window.location.href = redirect_url` ile tam sayfa yönlendirme. |

## Canonical domain

- Tüm PayTR callback ve yönlendirme URL'leri tek domain üzerinden: `FRONTEND_URL` veya istek host'u kullanılır; `www.noryaai.com` → `https://noryaai.com` normalize edilir.
- **PayTR panel:** Bildirim URL tek domain ile uyumlu olmalı, örn. `https://noryaai.com/paytr/callback`.

## Canlı / test modu

- `ENVIRONMENT=production` ise PayTR get-token isteğinde `test_mode` her zaman **0** gönderilir (canlıda test modu kullanılmaz).
- Aksi durumda `PAYTR_TEST_MODE` env değişkeni kullanılır.

## Hata mesajları

- Init hatası (4xx/5xx): Sunucudan dönen `detail` kullanıcıya kırmızı kutu içinde gösterilir; PayTR `reason` metni mesaja eklenir.
- Zaman aşımı (25 sn): "Bağlantı zaman aşımına uğradı. Lütfen tekrar deneyin veya destek@noryaai.com ile iletişime geçin."
- Console (F12): Hata yanıtı loglanır.

## Production kontrol listesi

- [ ] `FRONTEND_URL=https://noryaai.com` (veya canonical domain) ayarlı
- [ ] `ENVIRONMENT=production` (test_mode otomatik 0)
- [ ] PayTR panel: Bildirim URL = `https://noryaai.com/paytr/callback` (veya canonical domain)
- [ ] PayTR panel: Mağaza canlı modda, entegrasyon bilgileri doğru
