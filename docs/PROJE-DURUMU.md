# Norya — Proje Durumu ve Eksiklik Kontrolü

Son kontrol tarihi: proje baştan aşağı taranmıştır.

---

## Tamamlanan / Hazır Olanlar

| Alan | Durum |
|------|--------|
| **Auth** | Kayıt, giriş, JWT, e-posta doğrulama, şifre sıfırlama, misafir girişi |
| **Analiz** | Metin, PDF, görsel yükleme; OpenAI rapor; diyet planı, takviye, kalp sağlığı bölümleri |
| **Rapor** | Özet, değerler, risk, öneriler, PDF indir, paylaş, doktora götür, EMR/EHR notu |
| **Ödeme** | PayTR entegrasyonu, tek/aylık/yıllık plan, indirim kodu, misafir ödeme |
| **Admin** | Giriş (cookie), dashboard, kullanıcılar, analizler, ödemeler, kuponlar, loglar |
| **Frontend** | Tek sayfa (SPA), çok dil (TR/EN/IT/ES/FR/DE/HE/AR/HI/EL/CS/SR), PWA, responsive |
| **Yasal / UX** | Kullanım koşulları, gizlilik politikası, ödeme ve iade, iletişim (e-posta) bölümleri |
| **Güvenlik** | Rate limit, production’da SECRET_KEY/OPENAI kontrolü, HSTS/CSP, 500’de stack trace dönmüyor |
| **Config** | .env.example, DEPLOY.md, Cloudflare + GA4 rehberi, ENVIRONMENT notu |
| **Test** | test_health, test_auth, test_rate_limit |

---

## İsteğe Bağlı / “Olursa İyi Olur” Eksikler

| Eksik | Açıklama | Öncelik |
|-------|----------|---------|
| **Fatura / makbuz** | Sipariş sonrası indirilebilir fatura/makbuz modülü (ADMIN.md’de “henüz yok” deniyor) | Düşük |
| **Çerez bildirimi** | Sitede “KVKK uyumlu” geçiyor; ayrı bir çerez onay bandı (cookie banner) yok | Düşük (yasal gereklilik olarak eklenebilir) |
| **404 sayfası** | Bilinmeyen API path’lerde JSON 404 dönüyor; tarayıcıda yanlış URL’de SPA hash kullanılıyorsa sorun olmaz | Çok düşük |
| **README baslat.sh** | Düzeltildi → `start.sh` kullanılacak şekilde güncellendi | — |

---

## Yayına Almadan Yapılacaklar (Kod Dışı)

- Domain + hosting + SSL
- .env: `ENVIRONMENT=production`, `SECRET_KEY`, `FRONTEND_URL`, `CORS_ORIGINS`, PayTR URL’leri, SMTP
- İsteğe bağlı: `GA_MEASUREMENT_ID`, Cloudflare DNS

Detay: **DEPLOY.md**

---

## Sonuç

**Proje yayına alınabilir durumda.** Kritik eksik yok. Fatura/makbuz ve çerez bildirimi isteğe bağlı iyileştirme; canlıya geçtikten sonra eklenebilir.
