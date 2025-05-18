import pytest
from fastapi.testclient import TestClient
from api.auth import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def create_user(client):
    response = client.post('/auth/register', json={
        'username': 'test_user',
        'password': 'test_pass',
        'email': 'test_user@example.com'
    })
    return response.json()

@pytest.fixture
def login_user(client, create_user):
    response = client.post('/auth/login', json={
        'username': 'test_user',
        'password': 'test_pass'
    })
    return response.json()

def test_user_registration(client):
    response = client.post('/auth/register', json={
        'username': 'new_user',
        'password': 'new_pass',
        'email': 'new_user@example.com'
    })
    assert response.status_code == 201
    assert 'access_token' in response.json()


def test_user_login(client, create_user):
    response = client.post('/auth/login', json={
        'username': 'test_user',
        'password': 'test_pass'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json()


def test_login_with_invalid_credentials(client):
    response = client.post('/auth/login', json={
        'username': 'wrong_user',
        'password': 'wrong_pass'
    })
    assert response.status_code == 401
    assert 'detail' in response.json()


def test_login_without_password(client):
    response = client.post('/auth/login', json={
        'username': 'test_user'
    })
    assert response.status_code == 422
    assert 'detail' in response.json()


def test_registration_with_existing_username(client):
    client.post('/auth/register', json={
        'username': 'existing_user',
        'password': 'pass',
        'email': 'existing_user@example.com'
    })  # Register first time
    response = client.post('/auth/register', json={
        'username': 'existing_user',
        'password': 'pass',
        'email': 'existing_user2@example.com'
    })
    assert response.status_code == 400
    assert 'detail' in response.json()