import pytest
from fastapi.testclient import TestClient
from api.llm import app

# Create a test client using the FastAPI app
client = TestClient(app)

@pytest.fixture(scope="module")
def test_client():
    yield client

def test_llm_endpoint_valid_request(test_client):
    # Test a valid request to the LLM endpoint
    response = test_client.post("/llm", json={
        "prompt": "What is AI?",
        "max_tokens": 50
    })
    assert response.status_code == 200
    assert "choices" in response.json()


def test_llm_endpoint_invalid_request(test_client):
    # Test an invalid request to the LLM endpoint
    response = test_client.post("/llm", json={})
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()


def test_llm_endpoint_edge_case(test_client):
    # Test an edge case request to the LLM endpoint
    response = test_client.post("/llm", json={
        "prompt": ""
    })
    assert response.status_code == 400  # Bad Request
    assert "detail" in response.json()