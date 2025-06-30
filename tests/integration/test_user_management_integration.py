import pytest
from fastapi.testclient import TestClient
from api.auth import app
from crud.user import UserCRUD

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    return client

@pytest.fixture(scope="module")
def setup_user():
    # Create a test user
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "securepassword"
    }
    user = UserCRUD.create_user(user_data)
    yield user  # This is where the tests will run
    # Teardown logic goes here if needed
    UserCRUD.delete_user(user.id)


def test_user_registration(test_client):
    response = test_client.post("/auth/register", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 201
    assert "access_token" in response.json()


def test_user_login(test_client, setup_user):
    response = test_client.post("/auth/login", json={
        "username": setup_user.username,
        "password": "securepassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_user_profile_retrieval(test_client, setup_user):
    # Simulate login to get access token
    login_response = test_client.post("/auth/login", json={
        "username": setup_user.username,
        "password": "securepassword"
    })
    access_token = login_response.json()["access_token"]
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = test_client.get(f"/users/{setup_user.id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == setup_user.username


def test_user_profile_update(test_client, setup_user):
    login_response = test_client.post("/auth/login", json={
        "username": setup_user.username,
        "password": "securepassword"
    })
    access_token = login_response.json()["access_token"]
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    updated_data = {
        "username": "updateduser",
        "email": "updated@example.com"
    }
    response = test_client.put(f"/users/{setup_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"
