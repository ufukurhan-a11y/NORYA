"""Health and API check endpoints."""
from fastapi.testclient import TestClient


def test_health_returns_ok(client: TestClient):
    r = client.get("/health")
    assert r.status_code == 200
    j = r.json()
    assert j.get("status") == "ok"
    assert "openai_configured" in j
    assert "database" in j
    assert j.get("database") in ("ok", "error")


def test_api_check(client: TestClient):
    r = client.get("/api-check")
    assert r.status_code == 200
    j = r.json()
    assert "openai_ayarli" in j
