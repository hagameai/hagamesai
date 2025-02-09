import pytest
from fastapi.testclient import TestClient
from llm_service.service import app

# Test client for the FastAPI application
client = TestClient(app)

@pytest.mark.parametrize("input_data, expected_status", [
    ({"prompt": "What is AI?"}, 200),
    ({"prompt": ""}, 422),  # Invalid input case
])
def test_llm_service(input_data, expected_status):
    response = client.post("/llm/service", json=input_data)
    assert response.status_code == expected_status

# Add more tests to cover different scenarios

def test_llm_service_response_format():
    input_data = {"prompt": "Explain quantum computing."}
    response = client.post("/llm/service", json=input_data)
    assert response.status_code == 200
    assert "response" in response.json()  # Check if response key exists
    assert isinstance(response.json()["response"], str)  # Ensure the response is a string


def test_llm_service_invalid_method():
    response = client.get("/llm/service")  # Using GET instead of POST
    assert response.status_code == 405  # Method not allowed

# Further tests can be implemented to validate specific LLM outputs based on known inputs
