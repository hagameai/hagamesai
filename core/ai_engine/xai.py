"""Explainable AI (XAI) component for HAGAME."""

from typing import Any, Dict, List, Optional
import logging
import numpy as np
from pydantic import BaseModel
from .base import AIComponent

logger = logging.getLogger(__name__)


class Explanation(BaseModel):
    """Model for AI explanation data."""
    game_id: str
    timestamp: float
    decision_explanations: Dict[str, str]
    feature_importance: Dict[str, float]
    counterfactuals: List[Dict[str, Any]]
    confidence_levels: Dict[str, float]


class ExplainableAI(AIComponent):
    """Component for generating explanations of AI decisions."""

    def __init__(self):
        self.explanation_history: List[Explanation] = []
        self.feature_weights: Dict[str, np.ndarray] = {
            "decision": np.random.randn(5),
            "outcome": np.random.randn(4),
            "strategy": np.random.randn(6)
        }
        self.explanation_templates: Dict[str,
                                         str] = self._initialize_templates()

    def _initialize_templates(self) -> Dict[str, str]:
        """Initialize explanation templates."""
        return {
            "decision": (
                "The AI made this decision because {main_factor}, "
                "considering {secondary_factor}. "
                "This was influenced by {context_factor}."
            ),
            "outcome": (
                "The predicted outcome is based on {main_factor}, "
                "with {secondary_factor} playing a significant role. "
                "Historical data suggests {historical_factor}."
            ),
            "strategy": (
                "The recommended strategy focuses on {main_factor}, "
                "while accounting for {secondary_factor}. "
                "This approach was chosen because {reasoning_factor}."
            ),
            "counterfactual": (
                "If {changed_factor} had been {alternative_value}, "
                "the outcome would likely have been {alternative_outcome}."
            )
        }

    async def initialize(self) -> None:
        """Initialize XAI system."""
        logger.info("Initializing Explainable AI component")
        self._initialize_feature_analyzers()

    def _initialize_feature_analyzers(self) -> None:
        """Initialize feature analysis components."""
        self.analyzers = {
            "decision": self._create_decision_analyzer(),
            "outcome": self._create_outcome_analyzer(),
            "strategy": self._create_strategy_analyzer()
        }

    def _create_decision_analyzer(self) -> Dict[str, Any]:
        """Create decision analysis component."""
        return {
            "features": [
                "player_state",
                "game_context",
                "historical_actions",
                "predicted_outcomes",
                "uncertainty_factors"
            ],
            "weights": self.feature_weights["decision"]
        }

    def _create_outcome_analyzer(self) -> Dict[str, Any]:
        """Create outcome analysis component."""
        return {
            "features": [
                "current_state",
                "player_performance",
                "game_dynamics",
                "external_factors"
            ],
            "weights": self.feature_weights["outcome"]
        }

    def _create_strategy_analyzer(self) -> Dict[str, Any]:
        """Create strategy analysis component."""
        return {
            "features": [
                "player_profile",
                "game_objectives",
                "resource_state",
                "opponent_analysis",
                "risk_factors",
                "temporal_context"
            ],
            "weights": self.feature_weights["strategy"]
        }

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate explanations for AI decisions and predictions."""
        try:
            game_id = input_data.get("game_id")
            game_state = input_data.get("game_state", {})
            predictions = input_data.get("predictions", {})
            cognitive_state = input_data.get("cognitive_state", {})

            # Generate decision explanations
            decision_explanations = self._explain_decisions(
                game_state,
                predictions,
                cognitive_state
            )

            # Calculate feature importance
            feature_importance = self._calculate_feature_importance(
                game_state,
                predictions
            )

            # Generate counterfactuals
            counterfactuals = self._generate_counterfactuals(
                game_state,
                predictions
            )

            # Calculate confidence levels
            confidence_levels = self._calculate_confidence_levels(
                game_state,
                predictions,
                feature_importance
            )

            # Create explanation model
            import time
            explanation = Explanation(
                game_id=game_id,
                timestamp=time.time(),
                decision_explanations=decision_explanations,
                feature_importance=feature_importance,
                counterfactuals=counterfactuals,
                confidence_levels=confidence_levels
            )

            self.explanation_history.append(explanation)

            return explanation.dict()

        except Exception as e:
            logger.error(f"Error generating explanations: {str(e)}")
            raise

    def _explain_decisions(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any],
        cognitive_state: Dict[str, Any]
    ) -> Dict[str, str]:
        """Generate natural language explanations for decisions."""
        explanations = {}

        # Explain decision making
        decision_factors = self._analyze_decision_factors(
            game_state, predictions)
        explanations["decision"] = self._format_decision_explanation(
            decision_factors)

        # Explain outcome predictions
        outcome_factors = self._analyze_outcome_factors(
            game_state, predictions)
        explanations["outcome"] = self._format_outcome_explanation(
            outcome_factors)

        # Explain strategy recommendations
        strategy_factors = self._analyze_strategy_factors(
            game_state, cognitive_state)
        explanations["strategy"] = self._format_strategy_explanation(
            strategy_factors)

        return explanations

    def _analyze_decision_factors(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Analyze factors influencing decisions."""
        analyzer = self.analyzers["decision"]
        features = self._extract_decision_features(game_state, predictions)
        importance = features * analyzer["weights"]

        return {
            "main_factor": self._get_most_important_factor(
                importance,
                analyzer["features"]
            ),
            "secondary_factor": self._get_secondary_factor(
                importance,
                analyzer["features"]
            ),
            "context_factor": self._get_context_factor(game_state)
        }

    def _analyze_outcome_factors(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Analyze factors influencing outcome predictions."""
        analyzer = self.analyzers["outcome"]
        features = self._extract_outcome_features(game_state, predictions)
        importance = features * analyzer["weights"]

        return {
            "main_factor": self._get_most_important_factor(
                importance,
                analyzer["features"]
            ),
            "secondary_factor": self._get_secondary_factor(
                importance,
                analyzer["features"]
            ),
            "historical_factor": self._get_historical_factor(game_state)
        }

    def _analyze_strategy_factors(
        self,
        game_state: Dict[str, Any],
        cognitive_state: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Analyze factors influencing strategy recommendations."""
        analyzer = self.analyzers["strategy"]
        features = self._extract_strategy_features(game_state, cognitive_state)
        importance = features * analyzer["weights"]

        return {
            "main_factor": self._get_most_important_factor(
                importance,
                analyzer["features"]
            ),
            "secondary_factor": self._get_secondary_factor(
                importance,
                analyzer["features"]
            ),
            "reasoning_factor": self._get_reasoning_factor(cognitive_state)
        }

    def _calculate_feature_importance(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> Dict[str, float]:
        """Calculate importance scores for different features."""
        importance_scores = {}

        # Calculate decision feature importance
        decision_features = self._extract_decision_features(
            game_state, predictions)
        importance_scores.update(self._calculate_feature_scores(
            decision_features,
            self.analyzers["decision"]["features"],
            self.feature_weights["decision"]
        ))

        # Calculate outcome feature importance
        outcome_features = self._extract_outcome_features(
            game_state, predictions)
        importance_scores.update(self._calculate_feature_scores(
            outcome_features,
            self.analyzers["outcome"]["features"],
            self.feature_weights["outcome"]
        ))

        # Calculate strategy feature importance
        strategy_features = self._extract_strategy_features(game_state, {})
        importance_scores.update(self._calculate_feature_scores(
            strategy_features,
            self.analyzers["strategy"]["features"],
            self.feature_weights["strategy"]
        ))

        return importance_scores

    def _generate_counterfactuals(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate counterfactual explanations."""
        counterfactuals = []

        # Generate decision counterfactuals
        decision_cf = self._generate_decision_counterfactuals(
            game_state, predictions)
        counterfactuals.extend(decision_cf)

        # Generate outcome counterfactuals
        outcome_cf = self._generate_outcome_counterfactuals(
            game_state, predictions)
        counterfactuals.extend(outcome_cf)

        # Generate strategy counterfactuals
        strategy_cf = self._generate_strategy_counterfactuals(
            game_state, predictions)
        counterfactuals.extend(strategy_cf)

        return counterfactuals

    def _calculate_confidence_levels(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any],
        feature_importance: Dict[str, float]
    ) -> Dict[str, float]:
        """Calculate confidence levels for explanations."""
        confidence_levels = {}

        # Calculate decision explanation confidence
        confidence_levels["decision_confidence"] = self._calculate_decision_confidence(
            game_state,
            predictions,
            feature_importance
        )

        # Calculate outcome explanation confidence
        confidence_levels["outcome_confidence"] = self._calculate_outcome_confidence(
            game_state,
            predictions,
            feature_importance
        )

        # Calculate strategy explanation confidence
        confidence_levels["strategy_confidence"] = self._calculate_strategy_confidence(
            game_state,
            predictions,
            feature_importance
        )

        # Calculate overall explanation confidence
        confidence_levels["overall_confidence"] = np.mean(
            list(confidence_levels.values()))

        return confidence_levels

    def _extract_decision_features(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> np.ndarray:
        """Extract features for decision explanation."""
        return np.array([
            float(game_state.get("player_state_value", 0.0)),
            float(game_state.get("game_context_value", 0.0)),
            float(game_state.get("historical_actions_value", 0.0)),
            float(predictions.get("predicted_outcome_value", 0.0)),
            float(predictions.get("uncertainty_value", 0.0))
        ])

    def _extract_outcome_features(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> np.ndarray:
        """Extract features for outcome explanation."""
        return np.array([
            float(game_state.get("current_state_value", 0.0)),
            float(game_state.get("player_performance_value", 0.0)),
            float(game_state.get("game_dynamics_value", 0.0)),
            float(game_state.get("external_factors_value", 0.0))
        ])

    def _extract_strategy_features(
        self,
        game_state: Dict[str, Any],
        cognitive_state: Dict[str, Any]
    ) -> np.ndarray:
        """Extract features for strategy explanation."""
        return np.array([
            float(game_state.get("player_profile_value", 0.0)),
            float(game_state.get("game_objectives_value", 0.0)),
            float(game_state.get("resource_state_value", 0.0)),
            float(game_state.get("opponent_analysis_value", 0.0)),
            float(game_state.get("risk_factors_value", 0.0)),
            float(game_state.get("temporal_context_value", 0.0))
        ])

    async def update(self, feedback: Dict[str, Any]) -> None:
        """Update XAI model based on feedback."""
        try:
            # Update feature weights
            self._update_feature_weights(feedback)

            # Update explanation templates if provided
            self._update_templates(feedback)

            # Re-initialize analyzers with updated weights
            self._initialize_feature_analyzers()

            logger.info("Updated XAI model")

        except Exception as e:
            logger.error(f"Error updating XAI model: {str(e)}")
            raise

    def _update_feature_weights(self, feedback: Dict[str, Any]) -> None:
        """Update feature weights based on feedback."""
        learning_rate = 0.01

        for feature_type, weights in self.feature_weights.items():
            if f"{feature_type}_accuracy" in feedback:
                accuracy = feedback[f"{feature_type}_accuracy"]
                gradient = np.array(feedback.get(
                    f"{feature_type}_gradient", [0] * len(weights)))
                self.feature_weights[feature_type] += learning_rate * \
                    accuracy * gradient

    def _update_templates(self, feedback: Dict[str, Any]) -> None:
        """Update explanation templates based on feedback."""
        if "template_updates" in feedback:
            updates = feedback["template_updates"]
            for template_type, new_template in updates.items():
                if template_type in self.explanation_templates:
                    self.explanation_templates[template_type] = new_template
