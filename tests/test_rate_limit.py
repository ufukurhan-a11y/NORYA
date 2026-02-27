"""Rate limit: /debug/rate-test 5/minute returns 429 after 5 requests."""
from fastapi.testclient import TestClient


def test_debug_rate_test_200_then_429(client: TestClient):
    for i in range(5):
        r = client.get("/debug/rate-test")
        assert r.status_code == 200, f"Request {i+1} should be 200"
        assert r.json() == {"ok": True}
    r = client.get("/debug/rate-test")
    assert r.status_code == 429
    j = r.json()
    assert j.get("error") == "Too many requests"
    assert "detail" in j
