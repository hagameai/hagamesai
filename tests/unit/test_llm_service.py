import pytest
from llm_service.service import LLMService


@pytest.fixture
def llm_service():
    """
    Fixture to create an instance of `LLMService` for testing.
    """
    return LLMService()


def test_service_initialization(llm_service):
    """
    Test that the LLMService initializes correctly.
    """
    assert llm_service is not None


def test_process_request_valid(llm_service):
    """
    Test processing a valid request.
    """
    request_data = {'input': 'Hello, AI!'}
    response = llm_service.process_request(request_data)
    assert response is not None
    assert 'output' in response
    assert response['output'] == 'Hello, AI! processed'  # Example expected behavior


def test_process_request_invalid(llm_service):
    """
    Test processing an invalid request.
    """
    request_data = {'wrong_key': 'Invalid data'}
    with pytest.raises(ValueError, match='Invalid request format'):
        llm_service.process_request(request_data)


def test_service_response_format(llm_service):
    """
    Test that the response format is correct.
    """
    request_data = {'input': 'Test response format.'}
    response = llm_service.process_request(request_data)
    assert isinstance(response, dict)
    assert 'output' in response
    assert isinstance(response['output'], str)