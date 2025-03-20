import unittest
from llm_service.service import LLMService

class TestLLMService(unittest.TestCase):
    def setUp(self):
        self.llm_service = LLMService()

    def test_service_initialization(self):
        # Test if LLMService initializes correctly
        self.assertIsNotNone(self.llm_service)

    def test_generate_response(self):
        # Test generating a response from the LLM
        prompt = "What is the capital of France?"
        response = self.llm_service.generate_response(prompt)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def test_handle_error(self):
        # Test error handling in response generation
        with self.assertRaises(ValueError):
            self.llm_service.generate_response('')  # Empty prompt should raise an error

if __name__ == '__main__':
    unittest.main()