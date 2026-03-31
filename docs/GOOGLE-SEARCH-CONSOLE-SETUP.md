# Google Search Console Setup & Sitemap Submit

**Tarih**: 31 Mart 2026  
**Hedef**: SEO optimizasyonlarını Google'a bildirmek

---

## 🎯 Adım Adım Kurulum

### 1️⃣ Google Search Console'a Giriş Yap

🔗 **URL**: https://search.google.com/search-console

**Gerekenler**:
- Google hesabı (tercihen iş hesabı)
- Domain sahipliği (noryaai.com)

---

### 2️⃣ Property Ekleyin

#### Seçenek A: Domain Property (ÖNERİLEN)
Kapsam: Tüm alt domainler (www., blog., api., vb.)

1. **"Add Property"** tıklayın
2. **Domain** seçin
3. Domain girin: `noryaai.com`
4. **Continue** tıklayın
5. **DNS Verification** seçin
6. DNS sağlayıcınıza gidin (GoDaddy, Namecheap, Cloudflare, vb.)
7. TXT kaydı ekleyin:
   ```
   Host: @
   Value: google-site-verification=XXXXXXXXXXXXXXXXXXXX
   TTL: 3600 (1 saat)
   ```
8. **Verify** tıklayın (propagation 5-10 dakika sürebilir)

#### Seçenek B: URL Prefix Property
Kapsam: Sadece belirtilen URL

1. **"Add Property"** tıklayın
2. **URL Prefix** seçin
3. URL girin: `https://noryaai.com`
4. **Continue** tıklayın

**Doğrulama Yöntemleri** (birini seçin):

##### A. HTML Dosyası Yükleme
1. **HTML file** indirin
2. Dosyayı server'a yükleyin: `/static/googleXXXXXXXXXXXX.html`
3. **Verify** tıklayın

##### B. DNS Kaydı
1. **Domain name provider** seçin
2. TXT kaydını DNS'e ekleyin
3. **Verify** tıklayın

##### C. Google Analytics
1. **Google Analytics** seçin
2. GA4 property seçin
3. **Verify** tıklayın

##### D. Google Tag Manager
1. **Google Tag Manager** seçin
2. Container seçin
3. **Verify** tıklayın

---

### 3️⃣ Sitemap Submit Edin

#### Adımlar:

1. **Sol Menü** → **Sitemaps** tıklayın
2. **"Add a new sitemap"** butonuna tıklayın
3. **Sitemap URL** alanına: `sitemap.xml` yazın
4. **"Submit"** butonuna tıklayın

![Sitemap Submit Örneği](https://support.google.com/webmasters/static/images/search-console.png)

#### Beklenen Sonuç:

```
✅ Status: Success
📊 Discovered: 500+ URLs
📅 Last read: Just now
```

---

### 4️⃣ Sitemap URL'leri

**Ana Sitemap**: 
```
https://noryaai.com/sitemap.xml
```

**İçerik**:
- ✅ Ana sayfa ve dil bazlı landing'ler (TR, EN, DE, ES, FR, IT, HE, HI, AR)
- ✅ Kurumsal sayfalar (hastaneler, klinikler, laboratuvarlar)
- ✅ Blog index sayfaları (9 dil)
- ✅ Tüm blog yazıları
- ✅ SEO landing pages
- ✅ Yasal sayfalar
- ✅ Araçlar ve hesaplamalar

**Toplam URL**: ~500+ sayfa

---

### 5️⃣ IndexNow (Bing/Yandex için)

**Otomatik index için**:

1. **Admin panel** → **SEO** → **IndexNow**
2. **"Submit URLs"** tıklayın
3. Yeni içerikler otomatik bildirilir

**IndexNow Key**: `/app/main.py` içinde tanımlı
```python
_INDEXNOW_KEY = settings.indexnow_key.strip()
```

**Key Dosyası**: 
```
https://noryaai.com/{key}.txt
```

---

## 🔍 Doğrulama Checklist

### ✅ Search Console Kurulumu
- [ ] Google hesabı ile giriş yapıldı
- [ ] Domain property eklendi
- [ ] DNS verification tamamlandı
- [ ] Property verified durumu: ✅

### ✅ Sitemap Submit
- [ ] Sitemap URL: `sitemap.xml` submit edildi
- [ ] Status: **Success**
- [ ] URLs discovered: **500+**
- [ ] Errors: **0**

### ✅ URL Inspection
- [ ] Ana sayfa test edildi: `https://noryaai.com`
- [ ] Enterprise sayfası test: `https://noryaai.com/hastaneler-icin?lang=tr`
- [ ] Blog index test: `https://noryaai.com/en/blog`
- [ ] Hreflang tags görünüyor: ✅
- [ ] Canonical tags görünüyor: ✅

---

## 📊 Takip Edilecek Metrikler

### İlk 7 Gün
- **Indexed pages**: Kaç sayfa indekslenmiş
- **Crawl errors**: 404, 500 hataları
- **Sitemap errors**: Parse hataları

### İlk 30 Gün
- **Impressions**: Kaç kez gösterildi
- **Clicks**: Kaç kez tıklandı
- **CTR**: Tıklama oranı
- **Average position**: Ortalama sıralama

### İlk 90 Gün
- **Top queries**: En çok trafik getiren kelimeler
- **Top pages**: En çok trafik alan sayfalar
- **Countries**: Hangi ülkelerden trafik
- **Devices**: Mobile vs Desktop

---

## 🚨 Sık Karşılaşılan Hatalar

### ❌ Sitemap Parse Error
**Sebep**: Geçersiz XML formatı  
**Çözüm**: `sitemap.xml` URL'ini browser'da test edin

### ❌ URLs Not Indexed
**Sebep**: noindex tag, robots.txt engeli  
**Çözüm**: URL Inspection ile kontrol edin

### ❌ Hreflang Errors
**Sebep**: Yanlış dil kodu, eksik x-default  
**Çözüm**: Hreflang tags doğrulayın

### ❌ Canonical Error
**Sebep**: Self-referential canonical yok  
**Çözüm**: Her sayfada canonical tag ekleyin

---

## 🔧 Faydalı Araçlar

### Google Araçları
- **URL Inspection Tool**: https://search.google.com/search-console/inspection
- **Rich Results Test**: https://search.google.com/test/rich-results
- **Mobile-Friendly Test**: https://search.google.com/test/mobile-friendly

### Third-Party Araçlar
- **Sitemap Validator**: https://www.xml-sitemaps.com/validate-sitemap
- **Hreflang Checker**: https://www.sistrix.com/hreflang-validator/
- **Schema Validator**: https://validator.schema.org/

---

## 📈 Sonraki Adımlar

### Hafta 1
1. ✅ Sitemap submit
2. ✅ URL Inspection testleri
3. ✅ Crawl errors kontrol
4. ✅ Mobile usability check

### Hafta 2
1. 📊 Performance report inceleme
2. 🔍 Top queries analizi
3. 🌍 Countries report
4. 📱 Mobile vs Desktop analizi

### Hafta 3-4
1. 📝 Yeni içerik planı (top queries bazlı)
2. 🔗 Internal linking optimizasyonu
3. 🎯 Keyword optimization
4. 📊 A/B test planı

---

## 📞 Destek & Kaynaklar

### Resmi Dokümantasyon
- **Search Console Help**: https://support.google.com/webmasters
- **SEO Starter Guide**: https://developers.google.com/search/docs/beginner/seo-starter-guide
- **Sitemaps**: https://developers.google.com/search/docs/crawling-indexing/sitemaps

### NoryaAI İletişim
- **Teknik**: support@noryaai.com
- **SEO**: info@noryaai.com

---

## 🎯 Başarı Kriterleri

### 1. Ay
- ✅ Tüm sayfalar indekslenmiş
- ✅ 0 crawl error
- ✅ Sitemap success status

### 3. Ay
- 📈 50%+ organik trafik artışı
- 📈 İlk 10'da 20+ keyword
- 📈 3%+ CTR

### 6. Ay
- 🎯 5+ ülkede ilk sayfa
- 🎯 150%+ organik trafik
- 🎯 100+ demo request

---

**Son Güncelleme**: 31 Mart 2026  
**Versiyon**: 1.0  
**Sonraki Gözden Geçirme**: 30 Nisan 2026
