import logging
from typing import Any, Dict, List, Union

# Configure logging for this module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def calculate_similarity(vector_a: List[float], vector_b: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    if not vector_a or not vector_b:
        logger.error("Input vectors must not be empty.")
        return 0.0
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude_a = sum(a ** 2 for a in vector_a) ** 0.5
    magnitude_b = sum(b ** 2 for b in vector_b) ** 0.5
    if magnitude_a == 0 or magnitude_b == 0:
        logger.error("One of the vectors has zero magnitude.")
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)


def preprocess_input(data: Union[str, List[str]]) -> List[str]:
    """Preprocess input data for AI model consumption."""
    if isinstance(data, str):
        return [data.strip().lower()]  # Convert single string to list
    if isinstance(data, list):
        return [item.strip().lower() for item in data if isinstance(item, str)]
    logger.error("Invalid input type. Expected str or List[str].")
    return []


def extract_features(data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract relevant features from input data."""
    features = {
        'length': len(data.get('text', '')),  # Example feature
        'has_numeric': any(char.isdigit() for char in data.get('text', '')),
    }
    logger.info(f"Extracted features: {features}")
    return features
