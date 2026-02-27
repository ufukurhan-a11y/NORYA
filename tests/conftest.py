"""Pytest fixtures: test client, test DB (in-memory SQLite)."""
import os
import pytest
from fastapi.testclient import TestClient

# Test ortamında in-memory SQLite (app import edilmeden önce set edilmeli)
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
os.environ.setdefault("SECRET_KEY", "test-secret-key")
os.environ.setdefault("OPENAI_API_KEY", "sk-test-dummy")
# Kayıt rate limit yüksek olsun ki tüm testler geçebilsin
os.environ.setdefault("RATE_LIMIT_REGISTER_PER_MINUTE", "100")

from app.main import app


@pytest.fixture(scope="function")
def client():
    """TestClient; lifespan ile in-memory DB ve tablolar hazır olur."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def _auth_token():
    """Tek sefer kayıt + giriş (rate limit 3/dk aşmamak için). Session boyunca aynı token."""
    with TestClient(app) as auth_client:
        auth_client.post(
            "/auth/register",
            data={
                "email": "test@example.com",
                "password": "test123456",
                "full_name": "Test User",
                "phone": "+905551234567",
                "country": "TR",
            },
        )
        r = auth_client.post(
            "/auth/login",
            data={"email": "test@example.com", "password": "test123456"},
        )
        assert r.status_code == 200, f"Login failed: {r.status_code} {r.text}"
        return r.json().get("access_token")


@pytest.fixture
def auth_headers(_auth_token):
    """Kayıtlı kullanıcı token'ı ile Authorization header döner."""
    return {"Authorization": f"Bearer {_auth_token}"}
