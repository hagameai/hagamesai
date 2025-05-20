import pytest
from llm_service.service import LLMService


@pytest.fixture
def llm_service():
    """Fixture for LLMService instance."""
    return LLMService()


def test_llm_service_initialization(llm_service):
    """Test the initialization of the LLMService."""
    assert llm_service is not None
    assert hasattr(llm_service, 'model')
    assert llm_service.model is not None


def test_llm_service_predict(llm_service):
    """Test the predict method of LLMService."""
    input_data = "What is the capital of France?"
    response = llm_service.predict(input_data)
    assert isinstance(response, str)
    assert len(response) > 0


def test_llm_service_handle_invalid_input(llm_service):
    """Test the predict method with invalid input."""
    input_data = None
    with pytest.raises(ValueError):
        llm_service.predict(input_data)