"""Sitemap ve robots.txt doğrulama: blog index + tüm blog URL'leri, Sitemap satırı."""
import re
from fastapi.testclient import TestClient


def test_is_public_indexable_url_helper():
    """is_public_indexable_url helper'ı private URL'leri doğru şekilde filtrelemeli."""
    from app.main import is_public_indexable_url
    
    # Public URL'ler True dönmeli
    public_urls = [
        "/",
        "/en",
        "/de",
        "/tr",
        "/pricing",
        "/how-it-works",
        "/about",
        "/contact",
        "/for-doctors",
        "/for-clinics",
        "/for-hospitals",
        "/en/blog",
        "/en/blog/sample-post",
        "/tr/kan-tahlili-sonucu",
        "/en/blood-test-results",
        "/legal/gizlilik",
        "/legal/kvkk",
        "/science",
        "/trust",
        "/methodology",
        "/medical-review",
        "/transparency",
        "/technology",
        "/security",
        "/enterprise-security",
        "/clinical-demo",
    ]
    for url in public_urls:
        assert is_public_indexable_url(url) is True, f"'{url}' public indexable olmalı"
    
    # Private URL'ler False dönmeli
    private_urls = [
        "/admin",
        "/admin/",
        "/admin/dashboard",
        "/login",
        "/login/",
        "/private",
        "/search",
        "/analyze",
        "/analyze/",
        "/analyze/export",
        "/analyze/history",
        "/analyze/history/123",
        "/analyze/usage",
        "/enterprise",
        "/enterprise/",
        "/pay",
        "/payment",
        "/payment/",
        "/payment/success",
        "/payment/failed",
        "/payment/callback",
        "/verify",
        "/verify/",
        "/verify/abc123",
        "/api",
        "/api/",
        "/api/v1/analyze",
        "/v1",
        "/v1/",
        "/report",
        "/chat",
        "/chat/",
        "/history/123",
        "/export",
        "/usage",
        "/share/abc123",
        "/pdf",
        "/pdf/download",
        "/callback",
        "/webhook",
        "/grant",
        "/token",
        "/init",
        "/subscribe",
        "/unsubscribe",
    ]
    for url in private_urls:
        assert is_public_indexable_url(url) is False, f"'{url}' private olmalı ve sitemap'te yer almamalı"


def test_robots_txt_contains_sitemap_url(client: TestClient):
    """robots.txt içinde Sitemap: https://noryaai.com/sitemap.xml satırı olmalı."""
    r = client.get("/robots.txt")
    assert r.status_code == 200
    text = r.text
    assert "Sitemap:" in text
    assert "https://noryaai.com/sitemap.xml" in text


def test_robots_txt_disallows_private_routes(client: TestClient):
    """robots.txt içinde private route'lar Disallow edilmeli."""
    r = client.get("/robots.txt")
    assert r.status_code == 200
    text = r.text
    # Private route'lar disallow edilmeli
    assert "Disallow: /admin/" in text
    assert "Disallow: /analyze/" in text
    assert "Disallow: /payment/" in text
    assert "Disallow: /verify/" in text
    assert "Disallow: /api/" in text
    assert "Disallow: /v1/" in text


def test_sitemap_xml_does_not_contain_private_routes(client: TestClient):
    """sitemap.xml içinde private route'lar (/analyze/export, /payment/success, vb.) olmamalı."""
    r = client.get("/sitemap.xml")
    assert r.status_code == 200
    body = r.text
    
    # Private URL'ler sitemap'te olmamalı
    private_paths = [
        "/analyze/export",
        "/analyze/history",
        "/analyze/usage",
        "/payment/success",
        "/payment/failed",
        "/verify/",
        "/admin",
        "/api/",
    ]
    for path in private_paths:
        assert path not in body, f"sitemap.xml içinde private route '{path}' bulunmamalı"


def test_payment_success_has_noindex_header(client: TestClient):
    """/payment/success sayfası noindex, nofollow header ve meta tag içermeli."""
    r = client.get("/payment/success")
    assert r.status_code == 200
    # X-Robots-Tag header kontrolü
    assert "noindex" in r.headers.get("X-Robots-Tag", "").lower() or "noindex" in r.text.lower()
    # Meta tag kontrolü
    assert '<meta name="robots" content="noindex,nofollow"' in r.text or "noindex" in r.text


def test_payment_failed_has_noindex_header(client: TestClient):
    """/payment/failed sayfası noindex, nofollow header ve meta tag içermeli."""
    r = client.get("/payment/failed")
    assert r.status_code == 200
    # X-Robots-Tag header kontrolü
    assert "noindex" in r.headers.get("X-Robots-Tag", "").lower() or "noindex" in r.text.lower()
    # Meta tag kontrolü
    assert '<meta name="robots" content="noindex,nofollow"' in r.text or "noindex" in r.text


def test_sitemap_xml_contains_blog_index_pages(client: TestClient):
    """sitemap.xml içinde /en/blog, /de/blog, /it/blog, /fr/blog index URL'leri olmalı."""
    r = client.get("/sitemap.xml")
    assert r.status_code == 200
    assert "application/xml" in r.headers.get("content-type", "")
    body = r.text
    for lang in ("en", "de", "it", "fr"):
        # <loc>.../en/blog</loc> veya .../en/blog şeklinde geçmeli
        assert f"/{lang}/blog</loc>" in body or f"/{lang}/blog\n" in body or f"/{lang}/blog\"" in body, (
            f"sitemap.xml içinde /{lang}/blog bulunamadı"
        )


def test_sitemap_xml_contains_blog_post_urls(client: TestClient):
    """sitemap.xml içinde en az bir blog post URL'i (/{lang}/blog/{slug}) olmalı."""
    r = client.get("/sitemap.xml")
    assert r.status_code == 200
    body = r.text
    # /xx/blog/slug-formatı (lang 2 harf, slug içinde tire olabilir)
    pattern = re.compile(r"<loc>[^<]+/([a-z]{2})/blog/([^<]+)</loc>")
    matches = pattern.findall(body)
    assert len(matches) >= 1, "sitemap.xml içinde hiç blog post URL'i yok; tüm dillerdeki postlar eklenmeli"


def test_sitemap_blog_urls_only_premium_locales(client: TestClient):
    """Blog canlıda yalnızca BLOG_LANGS_PREMIUM; el/cs/sr vb. sitemap'te olmamalı (404 önlenir)."""
    r = client.get("/sitemap.xml")
    assert r.status_code == 200
    body = r.text
    bad = re.findall(r"<loc>[^<]+/(el|cs|sr)/blog/", body)
    assert not bad, f"sitemap.xml premium olmayan blog locale içeriyor: {bad}"


def test_sitemap_xml_lastmod_from_updated_at(client: TestClient):
    """sitemap.xml'deki blog post URL'lerinde lastmod alanı olmalı (updatedAt kaynaklı)."""
    r = client.get("/sitemap.xml")
    assert r.status_code == 200
    body = r.text
    # Her <url> içinde lastmod olmalı
    url_blocks = re.findall(r"<url>(.*?)</url>", body, re.DOTALL)
    for block in url_blocks:
        if "/blog/" in block and "<loc>" in block:
            assert "<lastmod>" in block and "</lastmod>" in block, (
                "Blog post URL'inde lastmod (updatedAt) eksik: " + block[:200]
            )


def test_how_it_works_returns_200(client: TestClient):
    """How it works sayfası 404 vermemeli; Google Ads site bağlantısı için 200 dönmeli."""
    r = client.get("/how-it-works")
    assert r.status_code == 200, f"/how-it-works returned {r.status_code}"


def test_how_it_works_lang_de_returns_200_and_german_content(client: TestClient):
    """https://noryaai.com/how-it-works?lang=de hedef URL'i 200 dönmeli ve Almanca içerik göstermeli."""
    r = client.get("/how-it-works?lang=de")
    assert r.status_code == 200, f"/how-it-works?lang=de returned {r.status_code}"
    text = r.text
    assert "So funktioniert" in text or "Analyse starten" in text or "Preise ansehen" in text, (
        "Almanca metin bulunamadı; sayfa dil parametresine göre içerik değişmeli"
    )


def test_how_it_works_lang_ar_returns_200_and_arabic_content(client: TestClient):
    r = client.get("/how-it-works?lang=ar")
    assert r.status_code == 200
    text = r.text
    assert "كيف يعمل" in text and 'dir="rtl"' in text
    assert 'hreflang="ar"' in text and "how-it-works?lang=he" in text


def test_sitemap_xml_contains_how_it_works(client: TestClient):
    """sitemap.xml içinde /how-it-works URL'i olmalı."""
    r = client.get("/sitemap.xml")
    assert r.status_code == 200
    assert "/how-it-works</loc>" in r.text or "/how-it-works\n" in r.text, (
        "sitemap.xml içinde /how-it-works bulunamadı"
    )


def test_sitemap_xml_contains_clinician_landings(client: TestClient):
    """sitemap.xml içinde hekim/kurum landing URL'leri olmalı."""
    r = client.get("/sitemap.xml")
    assert r.status_code == 200
    body = r.text
    for path in ("/for-doctors", "/for-clinics", "/for-hospitals"):
        assert path in body, f"sitemap.xml içinde {path} bulunamadı"


def test_clinician_landing_pages_return_200(client: TestClient):
    """Klinik hedef sayfaları 404 vermemeli."""
    for path in ("/for-doctors", "/for-clinics", "/for-hospitals"):
        r = client.get(path)
        assert r.status_code == 200, f"{path} returned {r.status_code}"


SEO_LANDING_PATHS = [
    "/tr/kan-tahlili-sonucu",
    "/tr/kan-degerleri-anlama",
    "/tr/hemogram-sonucu",
    "/de/blutwerte-verstehen",
    "/de/laborwerte-verstehen",
    "/en/blood-test-results",
    "/en/understand-lab-results",
]


def test_seo_landing_pages_return_200(client: TestClient):
    """SEO landing sayfaları 404 vermemeli; hepsi 200 dönmeli."""
    for path in SEO_LANDING_PATHS:
        r = client.get(path)
        assert r.status_code == 200, f"{path} returned {r.status_code}"


def test_sitemap_xml_contains_seo_landing_urls(client: TestClient):
    """sitemap.xml içinde tüm SEO landing URL'leri olmalı."""
    r = client.get("/sitemap.xml")
    assert r.status_code == 200
    body = r.text
    for path in SEO_LANDING_PATHS:
        # <loc>http://.../tr/kan-tahlili-sonucu</loc>
        assert path in body, f"sitemap.xml içinde {path} bulunamadı"


def test_analyze_export_has_noindex_header(client: TestClient, auth_headers: dict):
    """/analyze/export endpoint'i X-Robots-Tag: noindex, nofollow header'ı dönmeli."""
    # Authenticated istek ile test et (çünkü auth gerektiriyor)
    r = client.get("/analyze/export", headers=auth_headers)
    assert r.status_code == 200
    # X-Robots-Tag header kontrolü
    assert "noindex" in r.headers.get("X-Robots-Tag", "").lower(), (
        f"/analyze/export X-Robots-Tag: noindex, nofollow header'ı dönmeli; mevcut: {r.headers.get('X-Robots-Tag')}"
    )
    assert "nofollow" in r.headers.get("X-Robots-Tag", "").lower(), (
        f"/analyze/export X-Robots-Tag: noindex, nofollow header'ı dönmeli; mevcut: {r.headers.get('X-Robots-Tag')}"
    )


def test_analyze_history_endpoints_have_noindex(client: TestClient, auth_headers: dict):
    """/analyze/history endpoint'leri X-Robots-Tag: noindex, nofollow header'ı dönmeli."""
    # GET /analyze/history
    r = client.get("/analyze/history", headers=auth_headers)
    assert r.status_code == 200
    assert "noindex" in r.headers.get("X-Robots-Tag", "").lower()
    
    # GET /analyze/usage
    r = client.get("/analyze/usage", headers=auth_headers)
    assert r.status_code == 200
    assert "noindex" in r.headers.get("X-Robots-Tag", "").lower()
