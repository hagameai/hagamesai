import pytest
from fastapi.testclient import TestClient
from api.games import app

# Initialize the TestClient with the FastAPI app
client = TestClient(app)

# Test cases for game management
class TestGameManagement:
    @pytest.fixture
    def create_game(self):
        # Helper function to create a game
        response = client.post("/games/", json={
            "name": "Test Game",
            "description": "A game for testing purposes."
        })
        return response.json()

    def test_create_game(self, create_game):
        assert create_game['name'] == "Test Game"
        assert create_game['description'] == "A game for testing purposes."

    def test_get_game(self, create_game):
        game_id = create_game['id']
        response = client.get(f"/games/{game_id}")
        assert response.status_code == 200
        assert response.json()['name'] == "Test Game"

    def test_update_game(self, create_game):
        game_id = create_game['id']
        response = client.put(f"/games/{game_id}", json={
            "name": "Updated Game",
            "description": "An updated game for testing purposes."
        })
        assert response.status_code == 200
        assert response.json()['name'] == "Updated Game"

    def test_delete_game(self, create_game):
        game_id = create_game['id']
        response = client.delete(f"/games/{game_id}")
        assert response.status_code == 204
        # Ensure the game is deleted
        response = client.get(f"/games/{game_id}")
        assert response.status_code == 404
