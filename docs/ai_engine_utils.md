# AI Engine Utility Functions Documentation

This document provides an overview of the utility functions used in the AI engine module of the hagamesai project. The utility functions are designed to facilitate various operations related to cognitive modeling and AI processing.

## Overview

The AI engine utility functions are responsible for supporting core functionalities such as data preprocessing, model evaluation, and cognitive processing. These functions are utilized across different components of the AI engine to ensure modularity and reusability.

## Utility Functions

### 1. Data Normalization

```python
def normalize_data(data: List[float]) -> List[float]:
    """
    Normalize the input data to a range between 0 and 1.

    Parameters:
    - data (List[float]): A list of float values to be normalized.

    Returns:
    - List[float]: A list of normalized float values.
    """
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]
```

### 2. Cognitive Load Calculation

```python
def calculate_cognitive_load(task_difficulty: float, user_expertise: float) -> float:
    """
    Calculate the cognitive load based on task difficulty and user expertise.

    Parameters:
    - task_difficulty (float): The difficulty level of the task.
    - user_expertise (float): The expertise level of the user.

    Returns:
    - float: The calculated cognitive load.
    """
    return task_difficulty / (user_expertise + 1e-5)  # Prevent division by zero
```

### 3. Performance Evaluation

```python
def evaluate_performance(predictions: List[float], actuals: List[float]) -> float:
    """
    Evaluate the performance of the AI model using Mean Squared Error (MSE).

    Parameters:
    - predictions (List[float]): The predictions made by the model.
    - actuals (List[float]): The actual values.

    Returns:
    - float: The calculated Mean Squared Error.
    """
    return sum((p - a) ** 2 for p, a in zip(predictions, actuals)) / len(actuals)
```

## Usage

These utility functions can be imported and utilized in various components of the AI engine. Ensure to handle exceptions and edge cases appropriately when using these functions in production.

## Conclusion

The utility functions outlined in this document play a vital role in the functionality of the AI engine. By maintaining a modular approach, we can enhance, test, and maintain these functions independently as the project evolves.

For further information, refer to the source code and related documentation.