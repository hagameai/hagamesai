import pytest
from fastapi.testclient import TestClient
from api.auth import app

# Create a test client using the FastAPI app
client = TestClient(app)

@pytest.mark.parametrize(
    "username, password, expected_status",
    [
        ("testuser", "testpass", 200),  # Successful login
        ("wronguser", "testpass", 401),  # Wrong username
        ("testuser", "wrongpass", 401),  # Wrong password
    ],
)
def test_authentication(username, password, expected_status):
    "/auth/login" is the endpoint for user login
    response = client.post("/auth/login", json={
        "username": username,
        "password": password,
    })
    assert response.status_code == expected_status


def test_registration():
    # Test user registration with valid data
    response = client.post("/auth/register", json={
        "username": "newuser",
        "password": "newpass",
        "email": "newuser@example.com"
    })
    assert response.status_code == 201
    assert "token" in response.json()  # Ensure a token is returned

    # Test registration with existing username
    response = client.post("/auth/register", json={
        "username": "newuser",
        "password": "newpass",
        "email": "newuser@example.com"
    })
    assert response.status_code == 400  # Conflict
    assert "detail" in response.json()


# Add more tests as necessary for other authentication features
