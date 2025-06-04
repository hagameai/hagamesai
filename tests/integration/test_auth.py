import pytest
from fastapi.testclient import TestClient
from api.auth import app

# Test client for the FastAPI app
client = TestClient(app)

@pytest.mark.parametrize("username, password, expected_status", [
    ("testuser", "testpass", 200),  # Successful login
    ("invaliduser", "testpass", 401),  # Invalid user
    ("testuser", "wrongpass", 401),  # Invalid password
])
def test_login(username, password, expected_status):
    response = client.post("/auth/login", json={
        "username": username,
        "password": password
    })
    assert response.status_code == expected_status


def test_register():
    response = client.post("/auth/register", json={
        "username": "newuser",
        "password": "newpass",
        "email": "newuser@example.com"
    })
    assert response.status_code == 201
    assert "access_token" in response.json()


def test_register_existing_user():
    response = client.post("/auth/register", json={
        "username": "testuser",
        "password": "testpass",
        "email": "testuser@example.com"
    })
    assert response.status_code == 400  # User already exists

