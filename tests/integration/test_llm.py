import pytest
from fastapi.testclient import TestClient
from api.llm import app

@pytest.fixture(scope="module")
def test_client():
    """Fixture to create a test client for the FastAPI app."""
    client = TestClient(app)
    return client


def test_llm_endpoint(client):
    """Test the LLM service API endpoint."""
    response = client.post("/llm/endpoint", json={
        "input": "Test input data"
    })
    assert response.status_code == 200,
    assert "output" in response.json(),
    assert response.json()["output"] == "Expected output"  # Replace with expected output


def test_llm_invalid_input(client):
    """Test LLM service API with invalid input."""
    response = client.post("/llm/endpoint", json={
        "input": 12345  # Invalid input type
    })
    assert response.status_code == 422,
    assert "detail" in response.json(),
    assert response.json()["detail"] == "Input validation error"  # Replace with actual error message
