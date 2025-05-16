import pytest
from fastapi.testclient import TestClient
from llm_service.service import app  # Import your FastAPI app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_llm_request(client):
    """
    Test LLM request endpoint.
    """
    response = client.post("/api/llm/request", json={
        "input": "Test input"
    })
    assert response.status_code == 200
    assert "output" in response.json()


def test_llm_response(client):
    """
    Test LLM response validation.
    """
    response = client.post("/api/llm/request", json={
        "input": "Test input"
    })
    llm_output = response.json()["output"]
    assert isinstance(llm_output, str)
    assert len(llm_output) > 0


def test_invalid_llm_request(client):
    """
    Test LLM request with invalid input.
    """
    response = client.post("/api/llm/request", json={})  # No input
    assert response.status_code == 422  # Unprocessable Entity


def test_llm_edge_case(client):
    """
    Test LLM request with edge case input.
    """
    response = client.post("/api/llm/request", json={
        "input": ""
    })  # Empty input
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()

