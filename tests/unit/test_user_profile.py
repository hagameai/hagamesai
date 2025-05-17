import pytest
from fastapi.testclient import TestClient
from api.auth import app  # Adjust the import based on your project structure

# Create a test client using the FastAPI app
client = TestClient(app)

@pytest.fixture
def create_user():
    """Fixture to create a user for testing"""
    response = client.post("/auth/register", json={
        "username": "testuser",
        "password": "testpassword",
        "email": "testuser@example.com"
    })
    return response.json()


def test_user_profile_creation(create_user):
    """Test user profile creation"""
    response = client.post("/users/profile", json={
        "bio": "This is a test user profile."
    }, headers={
        "Authorization": f"Bearer {create_user['access_token']}"
    })
    assert response.status_code == 201
    assert "profile_id" in response.json()


def test_get_user_profile(create_user):
    """Test fetching user profile"""
    response = client.get("/users/profile", headers={
        "Authorization": f"Bearer {create_user['access_token']}"
    })
    assert response.status_code == 200
    assert "bio" in response.json()


def test_update_user_profile(create_user):
    """Test updating user profile"""
    response = client.put("/users/profile", json={
        "bio": "Updated test user profile."
    }, headers={
        "Authorization": f"Bearer {create_user['access_token']}"
    })
    assert response.status_code == 200
    assert response.json()["bio"] == "Updated test user profile."


def test_delete_user_profile(create_user):
    """Test deleting user profile"""
    response = client.delete("/users/profile", headers={
        "Authorization": f"Bearer {create_user['access_token']}"
    })
    assert response.status_code == 204

    # Verify profile is deleted
    response = client.get("/users/profile", headers={
        "Authorization": f"Bearer {create_user['access_token']}"
    })
    assert response.status_code == 404
