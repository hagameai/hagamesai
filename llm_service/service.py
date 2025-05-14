import requests
import logging

class LLMService:
    """
    A service class to handle integration with the LLM (Large Language Model) API.
    """
    def __init__(self, api_key: str, api_url: str):
        """
        Initialize the LLM service with API key and URL.
        """
        self.api_key = api_key
        self.api_url = api_url
        self.logger = logging.getLogger(__name__)

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the LLM based on the provided prompt.
        :param prompt: The input prompt for the LLM.
        :return: The generated response from the LLM.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'prompt': prompt,
            'max_tokens': 150
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            response_data = response.json()
            return response_data.get('choices')[0].get('text').strip()
        except requests.exceptions.HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'An error occurred: {err}')
        return ""  # Return empty string in case of error

# Example usage:
# llm_service = LLMService(api_key='your_api_key', api_url='https://api.llmprovider.com/v1/generate')
# response = llm_service.generate_response('What is the capital of France?')
# print(response)