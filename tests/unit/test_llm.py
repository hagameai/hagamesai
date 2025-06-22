import pytest
from fastapi.testclient import TestClient
from api.llm import app  # Import the FastAPI app


@pytest.fixture(scope="module")
def client():
    """Fixture for the FastAPI test client."""
    with TestClient(app) as c:
        yield c


def test_llm_endpoint():
    """Test the LLM endpoint for successful response."""
    response = client().post("/llm/endpoint", json={"input": "test input"})
    assert response.status_code == 200
    assert "output" in response.json()


def test_llm_endpoint_invalid_data():
    """Test the LLM endpoint with invalid data."""
    response = client().post("/llm/endpoint", json={"invalid_key": "test"})
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()


def test_llm_endpoint_error_handling():
    """Test the LLM endpoint for error handling."""
    response = client().post("/llm/endpoint", json={"input": None})
    assert response.status_code == 400  # Bad Request
    assert "error" in response.json()