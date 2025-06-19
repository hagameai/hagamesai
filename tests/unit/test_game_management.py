import pytest
from fastapi.testclient import TestClient
from api.games import app
from crud.game_definition import GameDefinitionCRUD

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def setup_game_definition():
    # Sample game definition to be used in tests
    game_definition = {
        "name": "Sample Game",
        "description": "A sample game for testing.",
        "rules": "Sample rules"
    }
    # Assuming there is a method to create a game definition in the CRUD
    GameDefinitionCRUD.create(game_definition)
    yield game_definition  # Yield the created game definition for tests
    # Cleanup can be performed here if needed


def test_create_game(test_client, setup_game_definition):
    response = test_client.post("/games/", json=setup_game_definition)
    assert response.status_code == 201
    assert response.json()["name"] == setup_game_definition["name"]


def test_get_games(test_client):
    response = test_client.get("/games/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure it returns a list


def test_update_game(test_client, setup_game_definition):
    updated_game = {"name": "Updated Game", "description": "Updated description", "rules": "Updated rules"}
    response = test_client.put(f"/games/{setup_game_definition['id']}/", json=updated_game)
    assert response.status_code == 200
    assert response.json()["name"] == updated_game["name"]


def test_delete_game(test_client, setup_game_definition):
    response = test_client.delete(f"/games/{setup_game_definition['id']}/")
    assert response.status_code == 204  # No content response for successful deletion

    # Verify that the game no longer exists
    response = test_client.get(f"/games/{setup_game_definition['id']}/")
    assert response.status_code == 404  # Should return 404 Not Found after deletion