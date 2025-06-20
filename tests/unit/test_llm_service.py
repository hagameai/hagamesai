import pytest
from llm_service.service import LLMService


def test_llm_service_initialization():
    """
    Test initialization of the LLMService.
    """
    service = LLMService()
    assert service is not None,
           "LLMService should be initialized successfully"


def test_llm_service_predict():
    """
    Test the predict method of LLMService.
    """
    service = LLMService()
    input_data = "Sample input for prediction"
    result = service.predict(input_data)
    assert result is not None,
           "Predict should return a result"
    assert isinstance(result, dict),
           "Predict result should be a dictionary"


def test_llm_service_handle_invalid_input():
    """
    Test handling of invalid input in the predict method.
    """
    service = LLMService()
    with pytest.raises(ValueError):
        service.predict(None)


@pytest.mark.parametrize("input_data, expected_output",
                         [
                             ("input1", {"result": "output1"}),
                             ("input2", {"result": "output2"}),
                         ])
def test_llm_service_multiple_predictions(input_data, expected_output):
    """
    Test the predict method with multiple inputs to verify consistent output.
    """
    service = LLMService()
    result = service.predict(input_data)
    assert result == expected_output,
           f"Expected {expected_output} but got {result}"