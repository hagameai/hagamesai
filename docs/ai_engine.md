# docs/ai_engine.md
# AI Engine Module Documentation

## Overview
The AI Engine module provides functionality for managing AI models, including:
- Model creation and configuration
- Adaptive predictions based on cognitive profiles
- Explainable AI (XAI) features using SHAP values
- Model metadata management

## Components

### AIModel
The core model class that represents an AI model in the system.

#### Fields:
- `id`: Unique identifier
- `name`: Model name
- `description`: Optional model description
- `config`: JSON configuration for model parameters
- `metadata`: Optional JSON metadata
- `file_path`: Path to the saved model file
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### API Endpoints

#### Create Model
```http
POST /ai_models/
```
Creates a new AI model with the specified configuration.

#### Get Model
```http
GET /ai_models/{model_id}
```
Retrieves model details by ID.

#### Update Model
```http
PUT /ai_models/{model_id}
```
Updates model configuration and metadata.

#### Predict
```http
POST /ai_models/{model_id}/predict
```
Generates predictions using the model, with optional cognitive profile adaptation.

#### Explain
```http
POST /ai_models/{model_id}/explain
```
Provides model explanations using SHAP values.

## Usage Examples

### Creating a New Model
```python
model_data = {
    "name": "sentiment_classifier",
    "description": "Sentiment analysis model",
    "config": {
        "model_type": "transformer",
        "parameters": {
            "max_length": 512
        }
    }
}
response = client.post("/ai_models/", json=model_data)
```

### Making Predictions
```python
input_data = {
    "text": "This is a sample input"
}
response = client.post("/ai_models/1/predict", json=input_data)
```

### Getting Model Explanations
```python
response = client.post("/ai_models/1/explain", json=input_data)
```

## Dependencies
- SHAP: For model explanations
- joblib: For model serialization
- numpy: For numerical computations

## Testing
Run tests using pytest:
```bash
pytest tests/test_ai_engine/
```