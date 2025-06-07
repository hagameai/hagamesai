import pytest
from fastapi.testclient import TestClient
from llm_service.service import app

# Initialize TestClient with the FastAPI app
client = TestClient(app)

@pytest.mark.parametrize(
    "input_data, expected_status_code",
    [
        ("{\"input\": \"Hello, AI!\"}", 200),  # Valid input
        ("{\"input\": \"\"}", 400)  # Invalid input (empty)
    ]
)
def test_llm_service_integration(input_data, expected_status_code):
    response = client.post("/llm/predict", json=input_data)
    assert response.status_code == expected_status_code

# Additional test cases can be added here to cover more scenarios

# Test for unexpected behavior


def test_llm_service_integration_unexpected():
    response = client.post("/llm/predict", json={})  # Sending empty JSON
    assert response.status_code == 422  # Unprocessable Entity
