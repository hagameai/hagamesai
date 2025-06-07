"""Adaptive Prediction Engine for HAGAME."""

from typing import Any, Dict, List, Optional
import logging
import numpy as np
from pydantic import BaseModel
from .base import AIComponent

logger = logging.getLogger(__name__)


class PredictionModel(BaseModel):
    """Model for prediction data."""
    game_id: str
    player_id: str
    prediction_type: str
    confidence: float
    predicted_values: Dict[str, Any]
    context: Dict[str, Any]


class AdaptivePredictionEngine(AIComponent):
    """Component for making adaptive predictions about game states and player behavior."""

    def __init__(self):
        self.models: Dict[str, Any] = {}  # Game-specific prediction models
        self.history: List[PredictionModel] = []
        self.learning_rate: float = 0.01

    async def initialize(self) -> None:
        """Initialize prediction models and parameters."""
        logger.info("Initializing Adaptive Prediction Engine")
        # Initialize base prediction models
        self.models = {
            "behavior": self._create_behavior_model(),
            "outcome": self._create_outcome_model(),
            "strategy": self._create_strategy_model()
        }

    def _create_behavior_model(self) -> Dict[str, Any]:
        """Create model for predicting player behavior."""
        return {
            "weights": np.random.randn(10),  # Initial random weights
            "bias": np.random.randn(),
            "features": ["action_history", "cognitive_state", "game_context"]
        }

    def _create_outcome_model(self) -> Dict[str, Any]:
        """Create model for predicting game outcomes."""
        return {
            "weights": np.random.randn(8),
            "bias": np.random.randn(),
            "features": ["game_state", "player_stats", "uncertainty"]
        }

    def _create_strategy_model(self) -> Dict[str, Any]:
        """Create model for predicting optimal strategies."""
        return {
            "weights": np.random.randn(12),
            "bias": np.random.randn(),
            "features": ["game_state", "player_profile", "historical_patterns"]
        }

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process current game state and make predictions."""
        try:
            game_id = input_data.get("game_id")
            player_id = input_data.get("player_id")
            game_state = input_data.get("game_state", {})
            cognitive_state = input_data.get("cognitive_state", {})
            uncertainty = input_data.get("uncertainty", {})

            # Make different types of predictions
            behavior_pred = self._predict_behavior(game_state, cognitive_state)
            outcome_pred = self._predict_outcome(game_state, uncertainty)
            strategy_pred = self._predict_strategy(game_state, cognitive_state)

            prediction = PredictionModel(
                game_id=game_id,
                player_id=player_id,
                prediction_type="composite",
                confidence=self._calculate_confidence(
                    behavior_pred, outcome_pred, strategy_pred),
                predicted_values={
                    "behavior": behavior_pred,
                    "outcome": outcome_pred,
                    "strategy": strategy_pred
                },
                context={
                    "game_state": game_state,
                    "cognitive_state": cognitive_state,
                    "uncertainty": uncertainty
                }
            )

            self.history.append(prediction)

            return prediction.dict()

        except Exception as e:
            logger.error(f"Error in prediction processing: {str(e)}")
            raise

    def _predict_behavior(self, game_state: Dict[str, Any], cognitive_state: Dict[str, Any]) -> Dict[str, Any]:
        """Predict player behavior based on game state and cognitive state."""
        features = self._extract_features(
            game_state, cognitive_state, self.models["behavior"]["features"])
        prediction = np.dot(
            features, self.models["behavior"]["weights"]) + self.models["behavior"]["bias"]
        return {
            "predicted_actions": self._normalize_prediction(prediction),
            "confidence": float(np.mean(np.abs(prediction)))
        }

    def _predict_outcome(self, game_state: Dict[str, Any], uncertainty: Dict[str, Any]) -> Dict[str, Any]:
        """Predict game outcome based on current state and uncertainty."""
        features = self._extract_features(
            game_state, uncertainty, self.models["outcome"]["features"])
        prediction = np.dot(
            features, self.models["outcome"]["weights"]) + self.models["outcome"]["bias"]
        return {
            "win_probability": float(self._sigmoid(prediction)),
            "confidence": float(self._calculate_outcome_confidence(prediction, uncertainty))
        }

    def _predict_strategy(self, game_state: Dict[str, Any], cognitive_state: Dict[str, Any]) -> Dict[str, Any]:
        """Predict optimal strategy based on game state and cognitive state."""
        features = self._extract_features(
            game_state, cognitive_state, self.models["strategy"]["features"])
        prediction = np.dot(
            features, self.models["strategy"]["weights"]) + self.models["strategy"]["bias"]
        return {
            "recommended_actions": self._strategy_to_actions(prediction),
            "confidence": float(self._calculate_strategy_confidence(prediction, cognitive_state))
        }

    def _extract_features(self, state: Dict[str, Any], context: Dict[str, Any], feature_list: List[str]) -> np.ndarray:
        """Extract relevant features from state and context."""
        features = []
        for feature in feature_list:
            value = state.get(feature, 0) or context.get(feature, 0)
            features.append(float(value) if isinstance(
                value, (int, float)) else 0.0)
        return np.array(features)

    def _normalize_prediction(self, prediction: np.ndarray) -> List[float]:
        """Normalize prediction values to probabilities."""
        exp_pred = np.exp(prediction - np.max(prediction))
        return (exp_pred / exp_pred.sum()).tolist()

    def _sigmoid(self, x: float) -> float:
        """Apply sigmoid function to scalar value."""
        return 1 / (1 + np.exp(-x))

    def _calculate_confidence(self, *predictions: Dict[str, Any]) -> float:
        """Calculate overall confidence based on individual predictions."""
        confidences = [p.get("confidence", 0.0) for p in predictions]
        return float(np.mean(confidences))

    def _calculate_outcome_confidence(self, prediction: float, uncertainty: Dict[str, Any]) -> float:
        """Calculate confidence in outcome prediction."""
        base_confidence = self._sigmoid(abs(prediction))
        uncertainty_factor = uncertainty.get("outcome_uncertainty", 0.5)
        return base_confidence * (1 - uncertainty_factor)

    def _calculate_strategy_confidence(self, prediction: float, cognitive_state: Dict[str, Any]) -> float:
        """Calculate confidence in strategy prediction."""
        base_confidence = self._sigmoid(abs(prediction))
        cognitive_factor = cognitive_state.get("certainty", 0.5)
        return base_confidence * cognitive_factor

    def _strategy_to_actions(self, prediction: float) -> List[Dict[str, Any]]:
        """Convert strategy prediction to concrete actions."""
        return [
            {
                "action_type": "move",
                "probability": self._sigmoid(prediction),
                "parameters": {"direction": "optimal"}
            },
            {
                "action_type": "attack",
                "probability": self._sigmoid(-prediction),
                "parameters": {"target": "nearest"}
            }
        ]

    async def update(self, feedback: Dict[str, Any]) -> None:
        """Update prediction models based on feedback."""
        try:
            actual_outcome = feedback.get("actual_outcome", {})
            predicted_outcome = feedback.get("predicted_outcome", {})

            # Calculate prediction error
            error = self._calculate_prediction_error(
                actual_outcome, predicted_outcome)

            # Update model weights
            self._update_weights(error, feedback)

            # Adjust learning rate based on error
            self._adjust_learning_rate(error)

            logger.info(f"Updated prediction models with error: {error}")

        except Exception as e:
            logger.error(f"Error updating prediction models: {str(e)}")
            raise

    def _calculate_prediction_error(self, actual: Dict[str, Any], predicted: Dict[str, Any]) -> float:
        """Calculate error between actual and predicted outcomes."""
        actual_value = actual.get("value", 0.0)
        predicted_value = predicted.get("value", 0.0)
        return float(abs(actual_value - predicted_value))

    def _update_weights(self, error: float, feedback: Dict[str, Any]) -> None:
        """Update model weights based on prediction error."""
        for model_name, model in self.models.items():
            features = self._extract_features(
                feedback.get("game_state", {}),
                feedback.get("context", {}),
                model["features"]
            )
            gradient = error * features
            model["weights"] -= self.learning_rate * gradient
            model["bias"] -= self.learning_rate * error

    def _adjust_learning_rate(self, error: float) -> None:
        """Adjust learning rate based on prediction error."""
        if error > 0.5:
            self.learning_rate *= 0.95  # Decrease learning rate if error is high
        else:
            self.learning_rate *= 1.05  # Increase learning rate if error is low
        # Keep learning rate in reasonable bounds
        self.learning_rate = max(0.001, min(0.1, self.learning_rate))
