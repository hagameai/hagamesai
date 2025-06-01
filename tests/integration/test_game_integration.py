import pytest
from fastapi.testclient import TestClient
from main import app

# Create a test client using the FastAPI app
client = TestClient(app)


@pytest.fixture
def create_game():
    # Sample payload for creating a game
    payload = {
        "name": "Test Game",
        "description": "A game for testing purposes",
        "rules": "Test rules for the game."
    }
    response = client.post("/games/", json=payload)
    assert response.status_code == 201
    return response.json()


def test_create_game(create_game):
    game = create_game
    assert "id" in game
    assert game["name"] == "Test Game"
    assert game["description"] == "A game for testing purposes"


def test_get_game(create_game):
    game_id = create_game["id"]
    response = client.get(f"/games/{game_id}")
    assert response.status_code == 200
    game = response.json()
    assert game["id"] == game_id
    assert game["name"] == "Test Game"


def test_update_game(create_game):
    game_id = create_game["id"]
    update_payload = {
        "name": "Updated Game",
        "description": "An updated description for the game."
    }
    response = client.put(f"/games/{game_id}", json=update_payload)
    assert response.status_code == 200
    updated_game = response.json()
    assert updated_game["name"] == "Updated Game"


def test_delete_game(create_game):
    game_id = create_game["id"]
    response = client.delete(f"/games/{game_id}")
    assert response.status_code == 204
    # Ensure the game was deleted
    response = client.get(f"/games/{game_id}")
    assert response.status_code == 404
