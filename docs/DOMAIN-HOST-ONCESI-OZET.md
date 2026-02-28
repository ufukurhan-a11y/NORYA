# Domain ve Host Almadan Önce / Sonra — Özet

## Ana sayfa (static/index.html)

### Şu an hazır olanlar
- Tek sayfa uygulama: hero, nasıl çalışır, fiyatlandırma, SSS, iletişim
- Çoklu dil (TR, EN, DE, AR, HE, HI, IT, ES, FR, EL, CS, SR)
- Giriş / kayıt / şifre sıfırlama modalleri
- Tahlil yükleme (metin, PDF, görsel) ve rapor
- PayTR ile tek analiz / aylık / yıllık ödeme (test modu destekli)
- PWA: manifest, tema rengi, ikon
- Dark/Light tema
- Dil menüsü ve nav menü düzgün açılıyor (overflow düzeltildi)

### Domain almadan yapılabilecek iyileştirmeler
| Ne | Açıklama |
|----|----------|
| **SEO meta** | `<meta name="description" content="...">`, `og:title`, `og:description`, `og:image` eklenebilir; domain sonrası canonical URL güncellenir. |
| **İkon çeşitliliği** | manifest’te sadece SVG var; PNG ikonlar (192x192, 512x512) eklenebilir (PWA tam uyum). |
| **Hata / boş durumlar** | Ağ hatası, “sonuç bulunamadı” gibi mesajlar metinlerle netleştirilebilir. |
| **Erişilebilirlik** | Form alanlarına `aria-label`, hata mesajlarına `aria-live` eklenebilir. |

---

## Admin paneli (/admin)

### Şu an hazır olanlar
- Cookie ile giriş (ADMIN_SECRET); production’da Secure cookie
- Dashboard, kullanıcılar, analizler, raporlar, kuyruk, kuponlar, ödemeler, hatalar, yüklemeler, güvenlik
- Analiz listesinde: sonuç önizleme, Norya raporu PDF, müşteri belgesi (orijinal PDF/görsel) linkleri
- PDF ve orijinal belge endpoint’leri hem X-Admin-Secret hem cookie ile çalışıyor
- Giriş kilidi: 5 başarısız denemede 15 dk lockout

### Domain almadan yapılabilecek iyileştirmeler
| Ne | Açıklama |
|----|----------|
| **Dashboard özeti** | İsteğe bağlı: son 24 saat analiz sayısı, son ödemeler özeti (zaten veri var, sadece görsel özet). |
| **Dışa aktarma** | Analiz listesini CSV/Excel ile dışa aktarma butonu. |
| **Arama / filtre** | Bazı sayfalarda gelişmiş filtre (tarih aralığı zaten analizlerde var). |

---

## Backend / Konfigürasyon

### Domain ve host almadan yapılması gerekenler (kritik değil, ama iyi olur)
| Ne | Nerede | Açıklama |
|----|--------|----------|
| **SECRET_KEY** | .env | Production’da mutlaka güçlü rastgele key (`openssl rand -hex 32`). |
| **ADMIN_SECRET** | .env | Admin paneli ve destek için şifre; production’da mutlaka set edilmeli. |
| **OPENAI_API_KEY** | .env | Analiz için zaten zorunlu. |
| **SMTP** | .env | Şifre sıfırlama / e-posta doğrulama için; yoksa link oluşur ama mail gitmez. |
| **PayTR test** | .env | PAYTR_* doldurulup PAYTR_TEST_MODE=1 ile test ödemesi yapılabilir. |

### Domain/host aldıktan sonra yapılacaklar (kısa liste)
| Ne | Açıklama |
|----|----------|
| **CORS_ORIGINS** | .env’de `https://alandiniz.com,https://www.alandiniz.com` yapın. |
| **FRONTEND_URL** | .env’de `https://alandiniz.com` (e-postadaki linkler için). |
| **PayTR canlı** | PAYTR_NOTIFICATION_URL, PAYTR_OK_URL, PAYTR_FAIL_URL’i domain’e göre güncelleyin; PAYTR_TEST_MODE=0. |
| **environment** | .env’de `ENVIRONMENT=production` (admin cookie Secure, debug kapalı). |
| **Veritabanı** | Production’da PostgreSQL önerilir; DATABASE_URL=postgresql://... |
| **SSL** | Nginx + Certbot veya host’un SSL’i; HTTPS zorunlu. |
| **Yedekleme** | DB ve `data/uploads` düzenli yedeklenmeli. |

---

## Özet tablo

| Alan | Domain öncesi yapılabilir | Domain sonrası zorunlu |
|------|---------------------------|-------------------------|
| **Ana sayfa** | SEO meta, PWA ikonlar, erişilebilirlik | Canonical URL (meta’da domain) |
| **Admin** | Dashboard özeti, dışa aktarma (opsiyonel) | Aynı; sadece HTTPS üzerinden erişim |
| **Config** | SECRET_KEY, ADMIN_SECRET, SMTP, PayTR test | CORS_ORIGINS, FRONTEND_URL, PayTR canlı URL’leri, ENVIRONMENT=production |
| **Host** | — | SSL, PostgreSQL (önerilen), yedekleme |

Domain ve host almadan uygulama tam işlevsel; asıl fark canlıda **CORS**, **FRONTEND_URL**, **PayTR URL’leri** ve **ENVIRONMENT=production** ile **SSL** ayarlarının yapılması.
