import pytest
from llm_service.service import AIEngineService


@pytest.fixture
def ai_engine_service():
    # Setup AIEngineService instance for testing
    service = AIEngineService()
    return service


def test_ai_engine_service_prediction(ai_engine_service):
    # Test the prediction method with a sample input
    input_data = {'user_input': 'Tell me a joke'}
    expected_output = 'Why did the scarecrow win an award? Because he was outstanding in his field!'

    # Call the prediction method
    result = ai_engine_service.predict(input_data)

    # Assert the expected output
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


def test_ai_engine_service_error_handling(ai_engine_service):
    # Test error handling in the prediction method
    input_data = {'invalid_key': 'Some input'}

    # Call the prediction method and validate error handling
    with pytest.raises(ValueError):
        ai_engine_service.predict(input_data)
