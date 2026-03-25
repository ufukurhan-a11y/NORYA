import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, select

from app.core.database import engine
from app.models.email_lead import EmailLead


def _lead_payload(email: str, consent_kvkk: bool = True, consent_gdpr: bool = True, **extra):
    payload = {
        "email": email,
        "name": "Test",
        "source": "blog",
        "locale": "tr",
        "consent_kvkk": consent_kvkk,
        "consent_gdpr": consent_gdpr,
        "utm_source": "utm_test",
    }
    payload.update(extra)
    return payload


def test_lead_subscribe_requires_consent(client: TestClient):
    r = client.post(
        "/api/lead/subscribe",
        json=_lead_payload("consent-required@example.com", consent_kvkk=False, consent_gdpr=True),
    )
    assert r.status_code == 400
    j = r.json()
    assert j.get("ok") is False
    assert j.get("error") == "consent_required"


def test_lead_subscribe_and_unsubscribe(client: TestClient):
    email = "lead-unsub@example.com"

    r = client.post("/api/lead/subscribe", json=_lead_payload(email))
    assert r.status_code == 200
    assert r.json().get("ok") is True
    assert r.json().get("already") is False

    with Session(engine) as db:
        lead = db.exec(select(EmailLead).where(EmailLead.email == email)).first()
        assert lead is not None
        assert lead.unsubscribed is False
        assert lead.consent_kvkk is True
        assert lead.consent_gdpr is True

    r2 = client.get("/api/lead/unsubscribe", params={"email": email})
    assert r2.status_code == 200
    assert "İptal" in r2.text or "cancel" in r2.text.lower()

    with Session(engine) as db:
        lead = db.exec(select(EmailLead).where(EmailLead.email == email)).first()
        assert lead is not None
        assert lead.unsubscribed is True

