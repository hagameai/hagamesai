import pytest
from schemas.llm_response import LLMResponse


def test_llm_response_initialization():
    """
    Test the initialization of LLMResponse schema.
    """
    response_data = {
        'id': '123',
        'status': 'success',
        'data': {'message': 'Hello, world!'}
    }
    llm_response = LLMResponse(**response_data)
    assert llm_response.id == '123'
    assert llm_response.status == 'success'
    assert llm_response.data['message'] == 'Hello, world!'


def test_llm_response_invalid_data():
    """
    Test LLMResponse initialization with invalid data.
    """
    with pytest.raises(ValueError):
        LLMResponse(id='123', status='success', data='Invalid data')


def test_llm_response_missing_fields():
    """
    Test LLMResponse initialization with missing required fields.
    """
    with pytest.raises(TypeError):
        LLMResponse(status='success')


def test_llm_response_empty_data():
    """
    Test LLMResponse with empty data field.
    """
    response_data = {
        'id': '124',
        'status': 'success',
        'data': {}
    }
    llm_response = LLMResponse(**response_data)
    assert llm_response.data == {}


if __name__ == '__main__':
    pytest.main()