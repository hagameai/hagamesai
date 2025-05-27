import pytest
from fastapi.testclient import TestClient
from core.ai_engine import app  # Assuming your FastAPI app is in core/ai_engine.py

@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


def test_ai_engine_integration(client):
    """Test integration of AI engine with valid input."""
    response = client.post("/api/llm/engine", json={
        "input_data": "Sample input for AI engine"
    })
    assert response.status_code == 200
    assert "output_data" in response.json()


def test_ai_engine_integration_invalid_data(client):
    """Test integration of AI engine with invalid input."""
    response = client.post("/api/llm/engine", json={
        "input_data": ""
    })
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()


def test_ai_engine_integration_error_handling(client):
    """Test AI engine's error handling with incorrect endpoint."""
    response = client.post("/api/llm/non_existing_endpoint", json={
        "input_data": "Sample input"
    })
    assert response.status_code == 404  # Not Found
    assert "detail" in response.json()