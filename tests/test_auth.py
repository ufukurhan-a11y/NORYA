"""Auth: register, login, validation."""
import pytest
from fastapi.testclient import TestClient


def test_register_success(client: TestClient):
    r = client.post(
        "/auth/register",
        data={
            "email": "new@example.com",
            "password": "secure123",
            "full_name": "New User",
            "phone": "+905559999999",
            "country": "TR",
        },
    )
    assert r.status_code == 200
    j = r.json()
    assert j.get("email") == "new@example.com"
    assert j.get("full_name") == "New User"


def test_register_validation(client: TestClient):
    r = client.post(
        "/auth/register",
        data={
            "email": "bad",
            "password": "123",
            "full_name": "",
            "phone": "1",
            "country": "X",
        },
    )
    assert r.status_code == 422


def test_login_success(client: TestClient):
    client.post(
        "/auth/register",
        data={
            "email": "login@example.com",
            "password": "pass123456",
            "full_name": "Login User",
            "phone": "+905551111111",
            "country": "TR",
        },
    )
    r = client.post(
        "/auth/login",
        data={"email": "login@example.com", "password": "pass123456"},
    )
    assert r.status_code == 200
    assert "access_token" in r.json()


def test_login_wrong_password(client: TestClient):
    client.post(
        "/auth/register",
        data={
            "email": "wrong@example.com",
            "password": "right123",
            "full_name": "Wrong User",
            "phone": "+905552222222",
            "country": "TR",
        },
    )
    r = client.post(
        "/auth/login",
        data={"email": "wrong@example.com", "password": "wrongpass"},
    )
    assert r.status_code == 401


def test_me_requires_auth(client: TestClient):
    r = client.get("/auth/me")
    assert r.status_code == 401


def test_me_with_token(client: TestClient, auth_headers: dict):
    r = client.get("/auth/me", headers=auth_headers)
    assert r.status_code == 200
    assert r.json().get("email") == "test@example.com"
