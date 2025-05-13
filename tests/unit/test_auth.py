import pytest
from core.auth import authenticate_user, create_user, get_user_by_username
from fastapi import HTTPException

@pytest.fixture
def test_user():
    return {
        "username": "testuser",
        "password": "testpass",
        "email": "testuser@example.com"
    }

@pytest.fixture
def create_test_user(test_user):
    create_user(**test_user)
    yield test_user
    # Cleanup if needed (e.g., remove test user from DB)


def test_user_creation(create_test_user):
    user = get_user_by_username(create_test_user['username'])
    assert user is not None
    assert user['username'] == create_test_user['username']
    assert user['email'] == create_test_user['email']


def test_successful_authentication(create_test_user):
    user = authenticate_user(create_test_user['username'], create_test_user['password'])
    assert user is not None
    assert user['username'] == create_test_user['username']


def test_failed_authentication():
    with pytest.raises(HTTPException) as exc:
        authenticate_user("wronguser", "wrongpass")
    assert exc.value.status_code == 401
    assert "Invalid credentials" in str(exc.value.detail)