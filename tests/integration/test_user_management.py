import pytest
from fastapi.testclient import TestClient
from api.auth import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_module():
    # Setup for the tests, if needed (e.g., create a test user)
    yield
    # Teardown if needed


def test_user_registration(setup_module):
    response = client.post("/api/auth/register", json={
        "username": "testuser",
        "password": "testpassword",
        "email": "testuser@example.com"
    })
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"


def test_user_login(setup_module):
    response = client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_user_profile_retrieval(setup_module):
    login_response = client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    access_token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    profile_response = client.get("/api/users/me", headers=headers)
    assert profile_response.status_code == 200
    assert profile_response.json()["username"] == "testuser"


def test_user_profile_update(setup_module):
    login_response = client.post("/api/auth/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    access_token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    update_response = client.put("/api/users/me", headers=headers, json={
        "email": "updateduser@example.com"
    })
    assert update_response.status_code == 200
    assert update_response.json()["email"] == "updateduser@example.com"