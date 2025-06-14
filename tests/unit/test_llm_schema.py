import pytest
from pydantic import ValidationError
from schemas.llm_request import LLMRequestSchema
from schemas.llm_response import LLMResponseSchema


def test_llm_request_schema_valid():
    # Test valid LLM request schema
    valid_data = {
        'prompt': 'What is the capital of France?',
        'max_tokens': 50,
        'temperature': 0.7,
    }
    schema = LLMRequestSchema(**valid_data)
    assert schema.prompt == valid_data['prompt']
    assert schema.max_tokens == valid_data['max_tokens']
    assert schema.temperature == valid_data['temperature']


def test_llm_request_schema_invalid():
    # Test invalid LLM request schema
    invalid_data = {
        'prompt': 12345,  # Invalid type for prompt
        'max_tokens': -10,  # Invalid value for max_tokens
        'temperature': 2.0,  # Invalid value for temperature
    }
    with pytest.raises(ValidationError):
        LLMRequestSchema(**invalid_data)


def test_llm_response_schema_valid():
    # Test valid LLM response schema
    valid_response_data = {
        'id': 'response_123',
        'choices': [{'text': 'Paris', 'index': 0}]
    }
    schema = LLMResponseSchema(**valid_response_data)
    assert schema.id == valid_response_data['id']
    assert len(schema.choices) == len(valid_response_data['choices'])


def test_llm_response_schema_invalid():
    # Test invalid LLM response schema
    invalid_response_data = {
        'id': 'response_123',
        'choices': [{'text': 12345}]  # Invalid type for text
    }
    with pytest.raises(ValidationError):
        LLMResponseSchema(**invalid_response_data)