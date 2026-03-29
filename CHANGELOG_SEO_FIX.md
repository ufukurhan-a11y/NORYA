# SEO Fix: Google Search Console "401 Unauthorized" Indexleme Sorunu Çözümü

**Tarih:** 2026-03-30  
**İlgili Issue:** Google Search Console'da `/analyze/export` için "401 Unauthorized nedeniyle engellendi" hatası

## Sorun

Google bot, authentication gerektiren private endpoint'lere (`/analyze/export`, `/payment/success`, vb.) erişmeye çalışıyor ve 401 Unauthorized hatası alıyordu. Bu durum Search Console'da indexleme sorunu olarak raporlanıyordu.

## Kök Neden

1. `/analyze/export` endpoint'i zaten `robots.txt` içinde `Disallow` edilmişti
2. Ancak HTML yanıt veren bazı sayfalar (`/payment/success`, `/payment/failed`) için `noindex` meta tag ve header eksikti
3. Sitemap generation'da private URL'leri filtrelemek için merkezi bir helper yoktu
4. Canonical/hreflang üretiminde private URL'lerin sızma riski vardı

## Yapılan Değişiklikler

### 1. Yeni Helper Fonksiyon: `is_public_indexable_url()`

**Dosya:** `app/main.py`

Tüm URL'lerin public indexable olup olmadığını kontrol eden merkezi helper:

```python
def is_public_indexable_url(path: str) -> bool:
    """
    SEO: URL'in sitemap'te ve canonical/hreflang'de yer alıp almaması gerektiğini belirler.
    
    Returns:
        True: URL sitemap'e eklenebilir, canonical/hreflang'de kullanılabilir
        False: URL private, sitemap'e eklenmemeli, noindex gerekebilir
    """
```

**Filtreleme Kuralları:**
- **Private Prefix'ler:** `/admin`, `/login`, `/analyze`, `/enterprise`, `/pay`, `/payment`, `/verify`, `/api`, `/v1`, `/report`, `/chat`
- **Private Exact Paths:** `/payment/success`, `/payment/failed`
- **Private Contains:** `/history/`, `/export`, `/usage`, `/share/`, `/pdf`, `/callback`, `/webhook`, `/grant`, `/token`, `/init`, `/subscribe`, `/unsubscribe`

### 2. Robots.txt Güncellemesi

**Dosya:** `app/main.py` (`robots_txt` route)

Daha kapsamlı `Disallow` kuralları:

```
Disallow: /admin/
Disallow: /analyze/
Disallow: /payment/
Disallow: /verify/
Disallow: /api/
Disallow: /v1/
Disallow: /report
```

### 3. Sitemap.xml Filtreleme

**Dosya:** `app/main.py` (`sitemap_xml` route)

Sitemap generation'da her URL eklenmeden önce `is_public_indexable_url()` ile kontrol ediliyor:

```python
def add(loc: str, ...):
    path = loc.replace(base_url, "") or "/"
    if not is_public_indexable_url(path):
        return  # Private URL'leri sitemap'e ekleme
    # ... URL ekle
```

### 4. Noindex Headers ve Meta Tags

#### `/payment/success`
**Dosya:** `app/main.py`

- HTML head'e `<meta name="robots" content="noindex,nofollow" />` eklendi
- Response header'e `X-Robots-Tag: noindex, nofollow` eklendi

#### `/payment/failed`
**Dosya:** `app/main.py`

- HTML head'e `<meta name="robots" content="noindex,nofollow" />` eklendi
- Response header'e `X-Robots-Tag: noindex, nofollow` eklendi

#### `/analyze/export`
**Dosya:** `app/main.py`

- Response header'e `X-Robots-Tag: noindex, nofollow` eklendi

#### `/analyze/usage` ve `/analyze/history`
**Dosya:** `app/main.py`

- Response header'e `X-Robots-Tag: noindex, nofollow` eklendi

### 5. Test Güncellemeleri

**Dosya:** `tests/test_sitemap.py`

Yeni testler eklendi:

```python
def test_robots_txt_disallows_private_routes(client: TestClient):
    """robots.txt içinde private route'lar Disallow edilmeli."""

def test_sitemap_xml_does_not_contain_private_routes(client: TestClient):
    """sitemap.xml içinde private route'lar olmamalı."""

def test_payment_success_has_noindex_header(client: TestClient):
    """/payment/success noindex içermeli."""

def test_payment_failed_has_noindex_header(client: TestClient):
    """/payment/failed noindex içermeli."""
```

## Sitemap Dışı Bırakılan Route'lar

### Authentication Required
- `/analyze/*` (tüm analiz sayfaları)
  - `/analyze/export`
  - `/analyze/history`
  - `/analyze/usage`
  - `/analyze/history/{id}`
- `/report`

### Payment Pages
- `/payment/success`
- `/payment/failed`
- `/payment/callback`
- `/pay`

### Verification
- `/verify/{report_id}`

### Admin & API
- `/admin/*`
- `/api/*`
- `/v1/*`

### Enterprise
- `/enterprise/*`

## Neden `/analyze/export` 401 Veriyordu?

`/analyze/export` endpoint'i kullanıcı authentication'ı gerektiriyor:

```python
@app.get("/analyze/export")
def analyze_export(
    user: User = Depends(get_current_user),  # <-- Auth required
    db: Session = Depends(get_db),
):
```

Google bot bu sayfaya eriştiğinde:
1. Cookie veya token yok
2. `get_current_user` dependency 401 Unauthorized döndürüyor
3. Search Console "401UnauthorizedError" olarak raporluyor

## Neden Artık Index Sorunu Üretmeyecek?

1. **robots.txt Disallow:** `/analyze/` path'i artık tamamen disallow
2. **Sitemap'te Yok:** `is_public_indexable_url()` helper'ı sitemap'e eklenmeyi engelliyor
3. **X-Robots-Tag Header:** Endpoint `noindex, nofollow` header döndürüyor
4. **No Canonical/Hreflang:** Private URL'ler canonical veya hreflang etiketlerinde referans verilmiyor

## Etkilenmeyen Özellikler

✅ **Report Export:** Kullanıcılar hala `/analyze/export` endpoint'ini kullanabilir (JSON download)  
✅ **Payment Flow:** `/payment/success` polling ve conversion tracking çalışmaya devam ediyor  
✅ **PDF Generation:** `/analyze/history/{id}/pdf` endpoint'leri çalışıyor  
✅ **Guest Payments:** Misafir ödeme akışı bozulmadı  

## Deployment Checklist

- [ ] `app/main.py` deploy edildi
- [ ] `tests/test_sitemap.py` deploy edildi
- [ ] Production'da `/sitemap.xml` kontrol edildi (private URL yok)
- [ ] Production'da `/robots.txt` kontrol edildi (Disallow kuralları var)
- [ ] `/payment/success` sayfası noindex tag içeriyor
- [ ] Google Search Console'da 401 hatası bir sonraki crawl'de kaybolmalı

## Sonraki Adımlar

1. **Google Search Console:** Bir sonraki crawl sonrası "401 Unauthorized" hatalarının azaldığını gözlemle
2. **Removal Tool:** Eğer `/analyze/export` hala index'te görünüyorsa, GSC Removal Tool ile kaldırma isteği gönder
3. **Monitoring:** Haftalık SEO kontrolünde sitemap ve robots.txt'yi doğrula

## İlgili Dosyalar

- `app/main.py` (ana değişiklikler)
- `tests/test_sitemap.py` (yeni testler)
- `static/robots.txt` (referans, main.py içinde render ediliyor)
