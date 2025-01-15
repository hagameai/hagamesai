import pytest
from fastapi.testclient import TestClient
from api.games import app

# Initialize the test client
client = TestClient(app)

@pytest.mark.parametrize("game_data", [
    {"name": "Chess", "description": "A classic strategy game."},
    {"name": "Checkers", "description": "A classic board game for two players."},
])
def test_create_game(game_data):
    response = client.post("/games/", json=game_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == game_data["name"]


def test_get_all_games():
    response = client.get("/games/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_game_by_id():
    game_id = 1  # assuming a game with ID 1 exists
    response = client.get(f"/games/{game_id}")
    assert response.status_code == 200
    assert "name" in response.json()


def test_update_game():
    game_id = 1  # assuming a game with ID 1 exists
    updated_data = {"name": "Updated Chess", "description": "An updated description for the chess game."}
    response = client.put(f"/games/{game_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == updated_data["name"]


def test_delete_game():
    game_id = 1  # assuming a game with ID 1 exists
    response = client.delete(f"/games/{game_id}")
    assert response.status_code == 204
    # Check if game is deleted
    response = client.get(f"/games/{game_id}")
    assert response.status_code == 404
