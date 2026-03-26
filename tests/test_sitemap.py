"""Sitemap ve robots.txt doğrulama: blog index + tüm blog URL'leri, Sitemap satırı."""
import re
from fastapi.testclient import TestClient


def test_robots_txt_contains_sitemap_url(client: TestClient):
    """robots.txt içinde Sitemap: https://noryaai.com/sitemap.xml satırı olmalı."""
    r = client.get("/robots.txt")
    assert r.status_code == 200
    text = r.text
    assert "Sitemap:" in text
    assert "https://noryaai.com/sitemap.xml" in text


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
