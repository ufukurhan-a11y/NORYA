"""Starlette TemplateResponse(request, name, ctx) ile eski (name, ctx) çağrıları uyumluluk katmanı."""
import os

import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
os.environ.setdefault("SECRET_KEY", "test-secret-key")
os.environ.setdefault("OPENAI_API_KEY", "sk-test-dummy")
os.environ.setdefault("ENVIRONMENT", "development")

from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_seo_landing_template_renders_not_jinja_cache_error(client: TestClient):
    """Eski TemplateResponse(name, ctx) yanlış sırayla Starlette'e giderse Jinja2 TypeError üretirdi."""
    r = client.get("/tr/kan-tahlili-sonucu")
    assert r.status_code == 200
    assert len(r.text) > 200


def test_static_marketing_pages_render(client: TestClient):
    for path in ("/about", "/science", "/de/faq"):
        r = client.get(path)
        assert r.status_code == 200, path
        assert len(r.text) > 100
