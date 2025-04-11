import pytest
from llm_service.service import LLMService


@pytest.fixture
def llm_service():
    """Fixture for LLMService instance."""
    return LLMService()


def test_llm_service_integration(llm_service):
    """Test LLM service integration with valid input."""
    response = llm_service.process_request({
        'input_data': 'Test input for LLM',
        'parameters': {'max_tokens': 50}
    })
    assert response is not None, "Expected a response from LLM service"
    assert 'output_data' in response, "Response should contain 'output_data' key"


def test_llm_service_error_handling(llm_service):
    """Test LLM service integration with invalid input."""
    with pytest.raises(ValueError):
        llm_service.process_request({
            'input_data': '',  # Invalid input
            'parameters': {'max_tokens': 50}
        })


@pytest.mark.parametrize('input_data, expected_output', [
    ('Hello, world!', 'Expected output for Hello'),
    ('Goodbye!', 'Expected output for Goodbye')
])
def test_llm_service_multiple_cases(llm_service, input_data, expected_output):
    """Test LLM service with multiple input cases."""
    response = llm_service.process_request({
        'input_data': input_data,
        'parameters': {'max_tokens': 50}
    })
    assert response['output_data'] == expected_output,
    f"Expected {expected_output} but got {response['output_data']}"