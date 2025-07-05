import unittest
from core.llm_processing import process_llm_request

class TestLLMProcessing(unittest.TestCase):
    def test_process_llm_request_valid_input(self):
        # Test with valid input
        input_data = {'prompt': 'Hello, AI!', 'max_tokens': 50}
        expected_output = {'response': 'AI response here...'}  # Update with expected response
        result = process_llm_request(input_data)
        self.assertEqual(result, expected_output)

    def test_process_llm_request_empty_prompt(self):
        # Test with empty prompt
        input_data = {'prompt': '', 'max_tokens': 50}
        with self.assertRaises(ValueError):
            process_llm_request(input_data)

    def test_process_llm_request_invalid_max_tokens(self):
        # Test with invalid max_tokens
        input_data = {'prompt': 'Hello, AI!', 'max_tokens': -1}
        with self.assertRaises(ValueError):
            process_llm_request(input_data)

    def test_process_llm_request_missing_keys(self):
        # Test with missing keys
        input_data = {'prompt': 'Hello, AI!'}  # Missing max_tokens
        with self.assertRaises(KeyError):
            process_llm_request(input_data)

if __name__ == '__main__':
    unittest.main()