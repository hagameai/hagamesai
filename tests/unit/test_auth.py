import pytest
from fastapi.testclient import TestClient
from api.auth import app

@pytest.fixture()
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


def test_user_registration(client):
    """Test user registration endpoint."""
    response = client.post("/auth/register", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 201
    assert response.json() == {"msg": "User created successfully"}


def test_user_login(client):
    """Test user login endpoint."""
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()


def test_invalid_login(client):
    """Test login with invalid credentials."""
    response = client.post("/auth/login", json={
        "username": "wronguser",
        "password": "wrongpass"
    })
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}