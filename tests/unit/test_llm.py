import pytest
from fastapi.testclient import TestClient
from api.llm import app  # Import your FastAPI app here

# Initialize the test client
client = TestClient(app)


def test_llm_endpoint():
    """
    Test for the LLM endpoint to check if it returns a valid response.
    """
    response = client.post("/llm_endpoint", json={"input": "Test input"})
    assert response.status_code == 200
    assert "output" in response.json()


def test_llm_endpoint_invalid_input():
    """
    Test the LLM endpoint with invalid input to ensure it handles errors correctly.
    """
    response = client.post("/llm_endpoint", json={"input": ""})  # Sending empty input
    assert response.status_code == 400
    assert "detail" in response.json()
    assert response.json()["detail"] == "Input cannot be empty"


def test_llm_endpoint_with_edge_case():
    """
    Test the LLM endpoint with edge case inputs.
    """
    response = client.post("/llm_endpoint", json={"input": "Edge case test"})
    assert response.status_code == 200
    assert "output" in response.json()