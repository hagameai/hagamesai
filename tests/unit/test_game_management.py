import pytest
from fastapi.testclient import TestClient
from api.games import app

@pytest.fixture()
def client():
    return TestClient(app)

# Test case for creating a game definition
def test_create_game_definition(client):
    response = client.post("/games/", json={
        "name": "Test Game",
        "description": "A game for testing purposes."
    })
    assert response.status_code == 201
    assert response.json() == {
        "name": "Test Game",
        "description": "A game for testing purposes.",
        "id": 1
    }

# Test case for retrieving game definitions
def test_get_game_definitions(client):
    response = client.get("/games/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list

# Test case for updating a game definition
def test_update_game_definition(client):
    response = client.put("/games/1", json={
        "name": "Updated Test Game",
        "description": "An updated game for testing purposes."
    })
    assert response.status_code == 200
    assert response.json() == {
        "name": "Updated Test Game",
        "description": "An updated game for testing purposes.",
        "id": 1
    }

# Test case for deleting a game definition
def test_delete_game_definition(client):
    response = client.delete("/games/1")
    assert response.status_code == 204
    response = client.get("/games/1")
    assert response.status_code == 404  # Ensure the game no longer exists
