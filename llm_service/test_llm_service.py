import unittest
from llm_service.service import LLMService

class TestLLMService(unittest.TestCase):
    """Unit tests for LLM service functionality."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.llm_service = LLMService()

    def test_generate_response(self):
        """Test the response generation from LLM service."""
        input_text = "What is the capital of France?"
        expected_output = "Paris"  # This should match the expected output based on the service logic
        response = self.llm_service.generate_response(input_text)
        self.assertEqual(response, expected_output,
                         f"Expected '{expected_output}' but got '{response}'")

    def test_invalid_input(self):
        """Test LLM service with invalid input."""
        input_text = ""
        with self.assertRaises(ValueError):
            self.llm_service.generate_response(input_text)

    def test_performance(self):
        """Test the performance of the LLM service."""
        import time
        input_text = "Tell me a joke"
        start_time = time.time()
        self.llm_service.generate_response(input_text)
        duration = time.time() - start_time
        self.assertLess(duration, 1,
                        "Response time should be less than 1 second")

if __name__ == '__main__':
    unittest.main()