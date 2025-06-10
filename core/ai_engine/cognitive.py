"""Cognitive Model Builder for HAGAME."""

from typing import Any, Dict, List, Optional
import logging
import numpy as np
from pydantic import BaseModel
from .base import AIComponent

logger = logging.getLogger(__name__)


class CognitiveProfile(BaseModel):
    """Model for cognitive profile data."""
    player_id: str
    learning_style: str
    decision_making: Dict[str, float]
    attention_patterns: Dict[str, float]
    skill_levels: Dict[str, float]
    adaptability: float
    last_updated: float


class CognitiveModelBuilder(AIComponent):
    """Component for building and updating cognitive models of players."""

    def __init__(self):
        self.profiles: Dict[str, CognitiveProfile] = {}
        self.feature_weights: Dict[str, np.ndarray] = {
            "learning": np.random.randn(5),
            "decision": np.random.randn(4),
            "attention": np.random.randn(3),
            "skill": np.random.randn(6)
        }

    async def initialize(self) -> None:
        """Initialize cognitive modeling system."""
        logger.info("Initializing Cognitive Model Builder")
        # Initialize base cognitive modeling parameters
        self._initialize_feature_extractors()

    def _initialize_feature_extractors(self) -> None:
        """Initialize feature extraction components."""
        self.extractors = {
            "learning": self._create_learning_extractor(),
            "decision": self._create_decision_extractor(),
            "attention": self._create_attention_extractor(),
            "skill": self._create_skill_extractor()
        }

    def _create_learning_extractor(self) -> Dict[str, Any]:
        """Create extractor for learning style features."""
        return {
            "features": [
                "improvement_rate",
                "error_correction",
                "pattern_recognition",
                "knowledge_retention",
                "adaptation_speed"
            ],
            "weights": self.feature_weights["learning"]
        }

    def _create_decision_extractor(self) -> Dict[str, Any]:
        """Create extractor for decision-making features."""
        return {
            "features": [
                "reaction_time",
                "risk_taking",
                "strategic_depth",
                "tactical_awareness"
            ],
            "weights": self.feature_weights["decision"]
        }

    def _create_attention_extractor(self) -> Dict[str, Any]:
        """Create extractor for attention pattern features."""
        return {
            "features": [
                "focus_duration",
                "distraction_resistance",
                "multi_tasking"
            ],
            "weights": self.feature_weights["attention"]
        }

    def _create_skill_extractor(self) -> Dict[str, Any]:
        """Create extractor for skill level features."""
        return {
            "features": [
                "mechanical_skill",
                "strategic_planning",
                "resource_management",
                "spatial_awareness",
                "timing_precision",
                "coordination"
            ],
            "weights": self.feature_weights["skill"]
        }

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process player data and update cognitive model."""
        try:
            player_id = input_data.get("player_id")
            game_state = input_data.get("game_state", {})

            # Extract cognitive features
            learning_features = self._extract_learning_features(game_state)
            decision_features = self._extract_decision_features(game_state)
            attention_features = self._extract_attention_features(game_state)
            skill_features = self._extract_skill_features(game_state)

            # Update or create cognitive profile
            profile = self._update_cognitive_profile(
                player_id,
                learning_features,
                decision_features,
                attention_features,
                skill_features
            )

            return profile.dict()

        except Exception as e:
            logger.error(f"Error in cognitive model processing: {str(e)}")
            raise

    def _extract_learning_features(self, game_state: Dict[str, Any]) -> Dict[str, float]:
        """Extract learning-related features from game state."""
        features = {}
        extractor = self.extractors["learning"]

        for feature in extractor["features"]:
            value = self._calculate_learning_metric(feature, game_state)
            features[feature] = float(value)

        return features

    def _extract_decision_features(self, game_state: Dict[str, Any]) -> Dict[str, float]:
        """Extract decision-making features from game state."""
        features = {}
        extractor = self.extractors["decision"]

        for feature in extractor["features"]:
            value = self._calculate_decision_metric(feature, game_state)
            features[feature] = float(value)

        return features

    def _extract_attention_features(self, game_state: Dict[str, Any]) -> Dict[str, float]:
        """Extract attention-related features from game state."""
        features = {}
        extractor = self.extractors["attention"]

        for feature in extractor["features"]:
            value = self._calculate_attention_metric(feature, game_state)
            features[feature] = float(value)

        return features

    def _extract_skill_features(self, game_state: Dict[str, Any]) -> Dict[str, float]:
        """Extract skill-related features from game state."""
        features = {}
        extractor = self.extractors["skill"]

        for feature in extractor["features"]:
            value = self._calculate_skill_metric(feature, game_state)
            features[feature] = float(value)

        return features

    def _calculate_learning_metric(self, feature: str, game_state: Dict[str, Any]) -> float:
        """Calculate specific learning-related metric."""
        metrics = {
            "improvement_rate": lambda: self._calc_improvement_rate(game_state),
            "error_correction": lambda: self._calc_error_correction(game_state),
            "pattern_recognition": lambda: self._calc_pattern_recognition(game_state),
            "knowledge_retention": lambda: self._calc_knowledge_retention(game_state),
            "adaptation_speed": lambda: self._calc_adaptation_speed(game_state)
        }
        return metrics.get(feature, lambda: 0.0)()

    def _calculate_decision_metric(self, feature: str, game_state: Dict[str, Any]) -> float:
        """Calculate specific decision-making metric."""
        metrics = {
            "reaction_time": lambda: self._calc_reaction_time(game_state),
            "risk_taking": lambda: self._calc_risk_taking(game_state),
            "strategic_depth": lambda: self._calc_strategic_depth(game_state),
            "tactical_awareness": lambda: self._calc_tactical_awareness(game_state)
        }
        return metrics.get(feature, lambda: 0.0)()

    def _calculate_attention_metric(self, feature: str, game_state: Dict[str, Any]) -> float:
        """Calculate specific attention-related metric."""
        metrics = {
            "focus_duration": lambda: self._calc_focus_duration(game_state),
            "distraction_resistance": lambda: self._calc_distraction_resistance(game_state),
            "multi_tasking": lambda: self._calc_multi_tasking(game_state)
        }
        return metrics.get(feature, lambda: 0.0)()

    def _calculate_skill_metric(self, feature: str, game_state: Dict[str, Any]) -> float:
        """Calculate specific skill-related metric."""
        metrics = {
            "mechanical_skill": lambda: self._calc_mechanical_skill(game_state),
            "strategic_planning": lambda: self._calc_strategic_planning(game_state),
            "resource_management": lambda: self._calc_resource_management(game_state),
            "spatial_awareness": lambda: self._calc_spatial_awareness(game_state),
            "timing_precision": lambda: self._calc_timing_precision(game_state),
            "coordination": lambda: self._calc_coordination(game_state)
        }
        return metrics.get(feature, lambda: 0.0)()

    # Calculation methods for learning metrics
    def _calc_improvement_rate(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("performance_delta", 0.0))

    def _calc_error_correction(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("error_correction_rate", 0.0))

    def _calc_pattern_recognition(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("pattern_recognition_score", 0.0))

    def _calc_knowledge_retention(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("knowledge_retention_rate", 0.0))

    def _calc_adaptation_speed(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("adaptation_speed", 0.0))

    # Calculation methods for decision metrics
    def _calc_reaction_time(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("avg_reaction_time", 0.0))

    def _calc_risk_taking(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("risk_taking_score", 0.0))

    def _calc_strategic_depth(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("strategic_depth_score", 0.0))

    def _calc_tactical_awareness(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("tactical_awareness_score", 0.0))

    # Calculation methods for attention metrics
    def _calc_focus_duration(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("focus_duration", 0.0))

    def _calc_distraction_resistance(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("distraction_resistance", 0.0))

    def _calc_multi_tasking(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("multi_tasking_score", 0.0))

    # Calculation methods for skill metrics
    def _calc_mechanical_skill(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("mechanical_skill_score", 0.0))

    def _calc_strategic_planning(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("strategic_planning_score", 0.0))

    def _calc_resource_management(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("resource_management_score", 0.0))

    def _calc_spatial_awareness(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("spatial_awareness_score", 0.0))

    def _calc_timing_precision(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("timing_precision_score", 0.0))

    def _calc_coordination(self, game_state: Dict[str, Any]) -> float:
        return float(game_state.get("coordination_score", 0.0))

    def _update_cognitive_profile(
        self,
        player_id: str,
        learning_features: Dict[str, float],
        decision_features: Dict[str, float],
        attention_features: Dict[str, float],
        skill_features: Dict[str, float]
    ) -> CognitiveProfile:
        """Update or create cognitive profile for player."""
        import time

        # Calculate learning style
        learning_style = self._determine_learning_style(learning_features)

        # Create or update profile
        profile = CognitiveProfile(
            player_id=player_id,
            learning_style=learning_style,
            decision_making=decision_features,
            attention_patterns=attention_features,
            skill_levels=skill_features,
            adaptability=self._calculate_adaptability(learning_features),
            last_updated=time.time()
        )

        self.profiles[player_id] = profile
        return profile

    def _determine_learning_style(self, learning_features: Dict[str, float]) -> str:
        """Determine player's learning style based on features."""
        styles = {
            "visual": self._calc_visual_score(learning_features),
            "kinesthetic": self._calc_kinesthetic_score(learning_features),
            "analytical": self._calc_analytical_score(learning_features)
        }
        return max(styles.items(), key=lambda x: x[1])[0]

    def _calc_visual_score(self, features: Dict[str, float]) -> float:
        """Calculate score for visual learning style."""
        return features.get("pattern_recognition", 0.0) * 0.6 + features.get("knowledge_retention", 0.0) * 0.4

    def _calc_kinesthetic_score(self, features: Dict[str, float]) -> float:
        """Calculate score for kinesthetic learning style."""
        return features.get("improvement_rate", 0.0) * 0.5 + features.get("adaptation_speed", 0.0) * 0.5

    def _calc_analytical_score(self, features: Dict[str, float]) -> float:
        """Calculate score for analytical learning style."""
        return features.get("error_correction", 0.0) * 0.7 + features.get("pattern_recognition", 0.0) * 0.3

    def _calculate_adaptability(self, learning_features: Dict[str, float]) -> float:
        """Calculate player's adaptability score."""
        weights = {
            "improvement_rate": 0.3,
            "adaptation_speed": 0.4,
            "error_correction": 0.3
        }

        adaptability = sum(
            learning_features.get(feature, 0.0) * weight
            for feature, weight in weights.items()
        )

        return float(max(0.0, min(1.0, adaptability)))

    async def update(self, feedback: Dict[str, Any]) -> None:
        """Update cognitive model based on feedback."""
        try:
            player_id = feedback.get("player_id")
            if player_id not in self.profiles:
                logger.warning(
                    f"No cognitive profile found for player {player_id}")
                return

            # Update feature weights based on feedback
            self._update_feature_weights(feedback)

            # Re-initialize feature extractors with updated weights
            self._initialize_feature_extractors()

            logger.info(f"Updated cognitive model for player {player_id}")

        except Exception as e:
            logger.error(f"Error updating cognitive model: {str(e)}")
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
