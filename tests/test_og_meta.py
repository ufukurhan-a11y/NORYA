"""OG / Twitter paylaşım görselleri: doğru yol ve boyut meta'ları."""
from fastapi.testclient import TestClient


def test_og_default_uses_images_path_and_dimensions(client: TestClient):
    """Dosya yalnızca static/images/og-default.png altında; eski /static/og-default.png kırık."""
    for path in ("/about", "/science", "/security", "/technology", "/how-it-works", "/pricing"):
        r = client.get(path)
        assert r.status_code == 200, path
        assert "/static/images/og-default.png" in r.text, path
        assert "/static/og-default.png" not in r.text, path
        assert "og:image:width" in r.text
        assert "1376" in r.text
        assert "768" in r.text


def test_seo_landing_og_consistent(client: TestClient):
    r = client.get("/tr/kan-tahlili-sonucu")
    assert r.status_code == 200
    assert "/static/images/og-default.png" in r.text
    assert "/static/og-default.png" not in r.text
    assert "og:image:width" in r.text


def test_unit_converter_has_social_meta(client: TestClient):
    r = client.get("/en/tools/unit-converter")
    assert r.status_code == 200
    assert "/static/images/og-default.png" in r.text
    assert "twitter:image" in r.text
    assert "og:image:width" in r.text
