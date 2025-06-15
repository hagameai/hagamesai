import pytest
from fastapi.testclient import TestClient
from llm_service.service import app

# Create a TestClient for the FastAPI app
client = TestClient(app)

@pytest.mark.parametrize("input_data, expected_response_code", [
    ("{\"prompt\": \"Hello, AI!\"}", 200),
    ("{\"prompt\": \"What is the capital of France?\"}", 200),
    ("{\"prompt\": \"Tell me a joke.\"}", 200),
    ("{\"prompt\": \"\"}", 400)  # Testing with empty prompt
])
def test_llm_response(input_data, expected_response_code):
    response = client.post("/llm/respond", json=input_data)
    assert response.status_code == expected_response_code

# Additional tests for LLM service integration

def test_llm_service_integration():
    # Test a valid request
    response = client.post("/llm/respond", json={"prompt": "What is AI?"})
    assert response.status_code == 200
    assert "response" in response.json()

    # Test invalid request
    response = client.post("/llm/respond", json={})  # No prompt
    assert response.status_code == 400
    assert response.json() == {"detail": "Prompt is required."}

    # Test LLM service with unexpected input
    response = client.post("/llm/respond", json={"prompt": 12345})
    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()