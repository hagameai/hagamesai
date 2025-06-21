import pytest
from fastapi.testclient import TestClient
from api.llm_service import app

@pytest.fixture(scope="module")
def test_client():
    """Fixture to create a test client for the FastAPI app."""  
    client = TestClient(app)
    yield client


def test_llm_endpoint_response(test_client):
    """Test the LLM service endpoint response."""
    response = test_client.post('/llm-endpoint', json={"input": "test input"})
    assert response.status_code == 200
    assert "output" in response.json()


def test_llm_endpoint_invalid_input(test_client):
    """Test the LLM service endpoint with invalid input."""
    response = test_client.post('/llm-endpoint', json={"input": ""})
    assert response.status_code == 422
    assert "detail" in response.json()


def test_llm_endpoint_performance(test_client):
    """Test the performance of the LLM service endpoint."""
    import time
    start_time = time.time()
    response = test_client.post('/llm-endpoint', json={"input": "performance test input"})
    duration = time.time() - start_time
    assert response.status_code == 200
    assert duration < 1.0  # endpoint should respond in under 1 second


if __name__ == '__main__':
    pytest.main()