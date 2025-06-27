import pytest
from fastapi.testclient import TestClient
from api.llm import app

# Create a test client using the FastAPI app
client = TestClient(app)


# Test cases for LLM API endpoints
class TestLLMAPI:

    def test_llm_endpoint(self):
        # Test the LLM API endpoint with a sample request payload
        payload = {
            "input_text": "Hello, AI!",
            "model": "gpt-3.5-turbo"
        }
        response = client.post("/llm/generate", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "output_text" in data
        assert isinstance(data["output_text"], str)

    def test_llm_endpoint_invalid_model(self):
        # Test the LLM API endpoint with an invalid model
        payload = {
            "input_text": "Hello, AI!",
            "model": "invalid-model"
        }
        response = client.post("/llm/generate", json=payload)
        assert response.status_code == 400
        assert "error" in response.json()

    def test_llm_endpoint_missing_fields(self):
        # Test the LLM API endpoint with missing fields
        payload = {"input_text": "Hello, AI!"}
        response = client.post("/llm/generate", json=payload)
        assert response.status_code == 422
        assert "detail" in response.json()

    def test_llm_endpoint_empty_input(self):
        # Test the LLM API endpoint with empty input text
        payload = {
            "input_text": "",
            "model": "gpt-3.5-turbo"
        }
        response = client.post("/llm/generate", json=payload)
        assert response.status_code == 400
        assert "error" in response.json()