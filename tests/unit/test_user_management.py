import pytest
from fastapi.testclient import TestClient
from api.auth import app
from crud.user import UserCRUD

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "password": "testpassword",
        "email": "testuser@example.com"
    }

@pytest.fixture
def create_user(client, user_data):
    response = client.post('/auth/register', json=user_data)
    return response

def test_user_registration(client, user_data):
    response = client.post('/auth/register', json=user_data)
    assert response.status_code == 201
    assert "access_token" in response.json()
    assert response.json()["user"]['username'] == user_data['username']

def test_user_login(client, create_user, user_data):
    response = client.post('/auth/login', json={
        "username": user_data['username'],
        "password": user_data['password']
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_user_login_with_incorrect_password(client, create_user, user_data):
    response = client.post('/auth/login', json={
        "username": user_data['username'],
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert "detail" in response.json()
    assert response.json()["detail"] == "Incorrect username or password"

def test_user_profile(client, create_user):
    response = client.get('/auth/profile')
    assert response.status_code == 200
    assert "username" in response.json()
