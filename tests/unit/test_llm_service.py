import pytest
from llm_service.service import LLMService


@pytest.fixture
def llm_service():
    """Fixture to create an instance of LLMService for testing."""
    return LLMService()


def test_llm_service_initialization(llm_service):
    """Test that the LLMService initializes correctly."""
    assert llm_service is not None


def test_llm_service_request_handling(llm_service):
    """Test LLM service can handle a request."""
    request_data = {"input": "What is the capital of France?"}
    response = llm_service.handle_request(request_data)
    assert "output" in response
    assert response["output"] == "The capital of France is Paris."


def test_llm_service_error_handling(llm_service):
    """Test LLM service handles errors gracefully."""
    invalid_request_data = {"input": None}
    response = llm_service.handle_request(invalid_request_data)
    assert "error" in response
    assert response["error"] == "Invalid input"


@pytest.mark.parametrize("query, expected_output", [
    ("Who is the president of the USA?", "The president of the USA is Joe Biden."),
    ("What is the largest planet in our solar system?", "The largest planet in our solar system is Jupiter."),
])
def test_llm_service_varied_responses(llm_service, query, expected_output):
    """Test LLM service responds correctly to varied queries."""
    request_data = {"input": query}
    response = llm_service.handle_request(request_data)
    assert "output" in response
    assert response["output"] == expected_output
