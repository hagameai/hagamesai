# Utility functions for AI engine processing

from typing import Any, Dict, List, Optional
import json


def load_json(file_path: str) -> Dict[str, Any]:
    """
    Load a JSON file and return its content as a dictionary.
    
    :param file_path: Path to the JSON file.
    :return: Dictionary containing the JSON data.
    :raises FileNotFoundError: If the file does not exist.
    :raises json.JSONDecodeError: If the file cannot be decoded.
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def save_json(data: Dict[str, Any], file_path: str) -> None:
    """
    Save a dictionary as a JSON file.
    
    :param data: Dictionary to save.
    :param file_path: Destination path for the JSON file.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def extract_keys(data: List[Dict[str, Any]], keys: List[str]) -> List[Dict[str, Any]]:
    """
    Extract specific keys from a list of dictionaries.
    
    :param data: List of dictionaries to extract keys from.
    :param keys: List of keys to extract.
    :return: List of dictionaries containing only the specified keys.
    """
    return [{k: d[k] for k in keys if k in d} for d in data]


def validate_input(data: Any, expected_type: type) -> bool:
    """
    Validate if the input data is of the expected type.
    
    :param data: The data to validate.
    :param expected_type: The expected type of the data.
    :return: True if data is of expected type, False otherwise.
    """
    return isinstance(data, expected_type)
