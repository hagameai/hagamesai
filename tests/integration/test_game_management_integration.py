import pytest
from fastapi.testclient import TestClient
from main import app

# Initialize the test client
client = TestClient(app)

@pytest.fixture
def game_data():
    return {
        "name": "Test Game",
        "description": "A game for testing purposes",
        "rules": "Test rules for the game",
        "max_players": 4
    }

def test_create_game(game_data):
    response = client.post("/games/", json=game_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == game_data["name"]
    assert "id" in data


def test_get_game(game_data):
    # First, create a game to retrieve
    create_response = client.post("/games/", json=game_data)
    game_id = create_response.json()["id"]

    # Now retrieve the created game
    response = client.get(f"/games/{game_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == game_id
    assert data["name"] == game_data["name"]


def test_update_game(game_data):
    # First, create a game to update
    create_response = client.post("/games/", json=game_data)
    game_id = create_response.json()["id"]
    updated_data = {"name": "Updated Game", "description": "Updated description"}

    # Now update the created game
    response = client.put(f"/games/{game_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_data["name"]


def test_delete_game(game_data):
    # First, create a game to delete
    create_response = client.post("/games/", json=game_data)
    game_id = create_response.json()["id"]

    # Now delete the created game
    response = client.delete(f"/games/{game_id}")
    assert response.status_code == 204

    # Ensure the game no longer exists
    response = client.get(f"/games/{game_id}")
    assert response.status_code == 404
