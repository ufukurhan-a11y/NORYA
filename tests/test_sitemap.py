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
