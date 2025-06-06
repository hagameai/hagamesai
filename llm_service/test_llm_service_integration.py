import pytest
from fastapi.testclient import TestClient
from llm_service.service import app

@pytest.fixture(scope="module")
def test_client():
    """Fixture to create a test client for the FastAPI app."""
    client = TestClient(app)
    yield client


def test_llm_service_integration(test_client):
    """Integration tests for LLM service with external APIs."""
    # Example test case for LLM service
    response = test_client.post("/llm_service/endpoint", json={
        "input_data": "Test input"
    })
    assert response.status_code == 200
    assert "output_data" in response.json()
    assert response.json()["output_data"] == "Expected output" # Replace with actual expected output

    # Additional tests can be added here to cover more scenarios

    
def test_llm_service_error_handling(test_client):
    """Test error handling in LLM service."""
    response = test_client.post("/llm_service/endpoint", json={
        "input_data": "Invalid data"
    })
    assert response.status_code == 400
    assert "error" in response.json() # Ensure response has error key
