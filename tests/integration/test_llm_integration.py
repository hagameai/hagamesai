import pytest
from fastapi.testclient import TestClient
from api.llm import app

# Initialize the test client for the FastAPI app
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_module():
    # Code to run before tests in this module (e.g., setup database)
    yield  # This will run after tests in this module
    # Code to run after tests in this module (e.g., teardown database)


def test_llm_integration_setup(setup_module):
    """Test the LLM API setup and basic connectivity"""
    response = client.get("/llm/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_llm_integration_prediction(setup_module):
    """Test LLM prediction endpoint"""
    payload = {"input_text": "What is AI?"}
    response = client.post("/llm/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()


def test_llm_integration_error_handling(setup_module):
    """Test LLM prediction endpoint with invalid input"""
    payload = {"input_text": ""}
    response = client.post("/llm/predict", json=payload)
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()  # Validate error response


def test_llm_integration_performance(setup_module):
    """Test LLM prediction performance"""
    import time
    payload = {"input_text": "Explain quantum computing."}
    start_time = time.time()
    response = client.post("/llm/predict", json=payload)
    end_time = time.time()
    assert response.status_code == 200
    assert (end_time - start_time) < 2  # Ensure response time is under 2 seconds
