"""Collective Wisdom Aggregator for HAGAME."""

from typing import Any, Dict, List, Optional, Tuple
import logging
import numpy as np
from pydantic import BaseModel
from .base import AIComponent

logger = logging.getLogger(__name__)


class CollectiveKnowledge(BaseModel):
    """Model for collective knowledge data."""
    game_id: str
    timestamp: float
    patterns: Dict[str, float]
    strategies: Dict[str, float]
    meta_insights: Dict[str, Any]
    confidence_scores: Dict[str, float]


class CollectiveWisdomAggregator(AIComponent):
    """Component for aggregating and analyzing collective game knowledge."""

    def __init__(self):
        self.knowledge_base: List[CollectiveKnowledge] = []
        self.pattern_weights: Dict[str, np.ndarray] = {}
        self.strategy_weights: Dict[str, np.ndarray] = {}
        self.meta_analyzers: Dict[str, Any] = {}
        self.confidence_threshold: float = 0.7

    async def initialize(self) -> None:
        """Initialize collective wisdom system."""
        logger.info("Initializing Collective Wisdom Aggregator")
        self._initialize_pattern_recognition()
        self._initialize_strategy_analysis()
        self._initialize_meta_analyzers()

    def _initialize_pattern_recognition(self) -> None:
        """Initialize pattern recognition components."""
        self.pattern_weights = {
            "behavioral": np.random.randn(5),  # Behavioral patterns
            "temporal": np.random.randn(4),    # Time-based patterns
            "spatial": np.random.randn(6),     # Spatial patterns
            "strategic": np.random.randn(4)    # Strategic patterns
        }

    def _initialize_strategy_analysis(self) -> None:
        """Initialize strategy analysis components."""
        self.strategy_weights = {
            "offensive": np.random.randn(3),   # Offensive strategies
            "defensive": np.random.randn(3),   # Defensive strategies
            "resource": np.random.randn(4),    # Resource management strategies
            "social": np.random.randn(3)       # Social interaction strategies
        }

    def _initialize_meta_analyzers(self) -> None:
        """Initialize meta-analysis components."""
        self.meta_analyzers = {
            "trend_analyzer": self._create_trend_analyzer(),
            "correlation_analyzer": self._create_correlation_analyzer(),
            "anomaly_detector": self._create_anomaly_detector()
        }

    def _create_trend_analyzer(self) -> Dict[str, Any]:
        """Create trend analysis component."""
        return {
            "window_size": 10,
            "weights": np.random.randn(10),
            "threshold": 0.5
        }

    def _create_correlation_analyzer(self) -> Dict[str, Any]:
        """Create correlation analysis component."""
        return {
            "matrix_size": 8,
            "correlation_matrix": np.random.randn(8, 8),
            "significance_threshold": 0.3
        }

    def _create_anomaly_detector(self) -> Dict[str, Any]:
        """Create anomaly detection component."""
        return {
            "baseline": np.zeros(5),
            "variance_threshold": 2.0,
            "history_size": 100
        }

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process game data and aggregate collective wisdom."""
        try:
            game_id = input_data.get("game_id")
            game_state = input_data.get("game_state", {})
            predictions = input_data.get("predictions", {})
            cognitive_state = input_data.get("cognitive_state", {})

            # Analyze patterns
            patterns = self._analyze_patterns(game_state, predictions)

            # Analyze strategies
            strategies = self._analyze_strategies(game_state, cognitive_state)

            # Perform meta-analysis
            meta_insights = self._perform_meta_analysis(patterns, strategies)

            # Calculate confidence scores
            confidence_scores = self._calculate_confidence_scores(
                patterns,
                strategies,
                meta_insights
            )

            # Create collective knowledge model
            import time
            knowledge = CollectiveKnowledge(
                game_id=game_id,
                timestamp=time.time(),
                patterns=patterns,
                strategies=strategies,
                meta_insights=meta_insights,
                confidence_scores=confidence_scores
            )

            self.knowledge_base.append(knowledge)

            return knowledge.dict()

        except Exception as e:
            logger.error(f"Error in collective wisdom processing: {str(e)}")
            raise

    def _analyze_patterns(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> Dict[str, float]:
        """Analyze various patterns in game data."""
        patterns = {}

        # Analyze behavioral patterns
        behavioral = self._analyze_behavioral_patterns(game_state, predictions)
        patterns.update(behavioral)

        # Analyze temporal patterns
        temporal = self._analyze_temporal_patterns(game_state)
        patterns.update(temporal)

        # Analyze spatial patterns
        spatial = self._analyze_spatial_patterns(game_state)
        patterns.update(spatial)

        # Analyze strategic patterns
        strategic = self._analyze_strategic_patterns(game_state, predictions)
        patterns.update(strategic)

        return patterns

    def _analyze_behavioral_patterns(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> Dict[str, float]:
        """Analyze behavioral patterns."""
        features = self._extract_behavioral_features(game_state, predictions)
        weights = self.pattern_weights["behavioral"]
        scores = np.dot(features, weights)

        return {
            "aggression_pattern": float(self._sigmoid(scores[0])),
            "cooperation_pattern": float(self._sigmoid(scores[1])),
            "risk_pattern": float(self._sigmoid(scores[2])),
            "learning_pattern": float(self._sigmoid(scores[3])),
            "adaptation_pattern": float(self._sigmoid(scores[4]))
        }

    def _analyze_temporal_patterns(self, game_state: Dict[str, Any]) -> Dict[str, float]:
        """Analyze temporal patterns."""
        features = self._extract_temporal_features(game_state)
        weights = self.pattern_weights["temporal"]
        scores = np.dot(features, weights)

        return {
            "cycle_pattern": float(self._sigmoid(scores[0])),
            "progression_pattern": float(self._sigmoid(scores[1])),
            "timing_pattern": float(self._sigmoid(scores[2])),
            "sequence_pattern": float(self._sigmoid(scores[3]))
        }

    def _analyze_spatial_patterns(self, game_state: Dict[str, Any]) -> Dict[str, float]:
        """Analyze spatial patterns."""
        features = self._extract_spatial_features(game_state)
        weights = self.pattern_weights["spatial"]
        scores = np.dot(features, weights)

        return {
            "clustering_pattern": float(self._sigmoid(scores[0])),
            "distribution_pattern": float(self._sigmoid(scores[1])),
            "movement_pattern": float(self._sigmoid(scores[2])),
            "territory_pattern": float(self._sigmoid(scores[3])),
            "position_pattern": float(self._sigmoid(scores[4])),
            "formation_pattern": float(self._sigmoid(scores[5]))
        }

    def _analyze_strategic_patterns(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> Dict[str, float]:
        """Analyze strategic patterns."""
        features = self._extract_strategic_features(game_state, predictions)
        weights = self.pattern_weights["strategic"]
        scores = np.dot(features, weights)

        return {
            "resource_pattern": float(self._sigmoid(scores[0])),
            "combat_pattern": float(self._sigmoid(scores[1])),
            "development_pattern": float(self._sigmoid(scores[2])),
            "social_pattern": float(self._sigmoid(scores[3]))
        }

    def _analyze_strategies(
        self,
        game_state: Dict[str, Any],
        cognitive_state: Dict[str, Any]
    ) -> Dict[str, float]:
        """Analyze various strategies in game data."""
        strategies = {}

        # Analyze offensive strategies
        offensive = self._analyze_offensive_strategies(game_state)
        strategies.update(offensive)

        # Analyze defensive strategies
        defensive = self._analyze_defensive_strategies(game_state)
        strategies.update(defensive)

        # Analyze resource strategies
        resource = self._analyze_resource_strategies(game_state)
        strategies.update(resource)

        # Analyze social strategies
        social = self._analyze_social_strategies(game_state, cognitive_state)
        strategies.update(social)

        return strategies

    def _analyze_offensive_strategies(self, game_state: Dict[str, Any]) -> Dict[str, float]:
        """Analyze offensive strategies."""
        features = self._extract_offensive_features(game_state)
        weights = self.strategy_weights["offensive"]
        scores = np.dot(features, weights)

        return {
            "aggressive_strategy": float(self._sigmoid(scores[0])),
            "tactical_strategy": float(self._sigmoid(scores[1])),
            "opportunistic_strategy": float(self._sigmoid(scores[2]))
        }

    def _analyze_defensive_strategies(self, game_state: Dict[str, Any]) -> Dict[str, float]:
        """Analyze defensive strategies."""
        features = self._extract_defensive_features(game_state)
        weights = self.strategy_weights["defensive"]
        scores = np.dot(features, weights)

        return {
            "protective_strategy": float(self._sigmoid(scores[0])),
            "reactive_strategy": float(self._sigmoid(scores[1])),
            "preventive_strategy": float(self._sigmoid(scores[2]))
        }

    def _analyze_resource_strategies(self, game_state: Dict[str, Any]) -> Dict[str, float]:
        """Analyze resource management strategies."""
        features = self._extract_resource_features(game_state)
        weights = self.strategy_weights["resource"]
        scores = np.dot(features, weights)

        return {
            "gathering_strategy": float(self._sigmoid(scores[0])),
            "conservation_strategy": float(self._sigmoid(scores[1])),
            "investment_strategy": float(self._sigmoid(scores[2])),
            "distribution_strategy": float(self._sigmoid(scores[3]))
        }

    def _analyze_social_strategies(
        self,
        game_state: Dict[str, Any],
        cognitive_state: Dict[str, Any]
    ) -> Dict[str, float]:
        """Analyze social interaction strategies."""
        features = self._extract_social_features(game_state, cognitive_state)
        weights = self.strategy_weights["social"]
        scores = np.dot(features, weights)

        return {
            "cooperative_strategy": float(self._sigmoid(scores[0])),
            "competitive_strategy": float(self._sigmoid(scores[1])),
            "diplomatic_strategy": float(self._sigmoid(scores[2]))
        }

    def _perform_meta_analysis(
        self,
        patterns: Dict[str, float],
        strategies: Dict[str, float]
    ) -> Dict[str, Any]:
        """Perform meta-analysis on patterns and strategies."""
        meta_insights = {}

        # Analyze trends
        trends = self._analyze_trends(patterns, strategies)
        meta_insights["trends"] = trends

        # Analyze correlations
        correlations = self._analyze_correlations(patterns, strategies)
        meta_insights["correlations"] = correlations

        # Detect anomalies
        anomalies = self._detect_anomalies(patterns, strategies)
        meta_insights["anomalies"] = anomalies

        return meta_insights

    def _analyze_trends(
        self,
        patterns: Dict[str, float],
        strategies: Dict[str, float]
    ) -> Dict[str, List[float]]:
        """Analyze trends in patterns and strategies."""
        analyzer = self.meta_analyzers["trend_analyzer"]
        combined_data = list(patterns.values()) + list(strategies.values())

        if len(self.knowledge_base) >= analyzer["window_size"]:
            historical_data = np.array([
                list(k.patterns.values()) + list(k.strategies.values())
                for k in self.knowledge_base[-analyzer["window_size"]:]
            ])

            trends = np.mean(
                (historical_data - np.mean(historical_data, axis=0)) *
                analyzer["weights"][:len(combined_data)],
                axis=0
            )
        else:
            trends = np.zeros(len(combined_data))

        return {
            "pattern_trends": trends[:len(patterns)].tolist(),
            "strategy_trends": trends[len(patterns):].tolist()
        }

    def _analyze_correlations(
        self,
        patterns: Dict[str, float],
        strategies: Dict[str, float]
    ) -> Dict[str, List[Tuple[str, str, float]]]:
        """Analyze correlations between patterns and strategies."""
        analyzer = self.meta_analyzers["correlation_analyzer"]
        combined_data = list(patterns.items()) + list(strategies.items())
        significant_correlations = []

        for i, (name1, value1) in enumerate(combined_data):
            for j, (name2, value2) in enumerate(combined_data[i+1:], i+1):
                correlation = analyzer["correlation_matrix"][i, j]
                if abs(correlation) > analyzer["significance_threshold"]:
                    significant_correlations.append(
                        (name1, name2, float(correlation)))

        return {
            "significant_correlations": significant_correlations
        }

    def _detect_anomalies(
        self,
        patterns: Dict[str, float],
        strategies: Dict[str, float]
    ) -> Dict[str, List[str]]:
        """Detect anomalies in patterns and strategies."""
        analyzer = self.meta_analyzers["anomaly_detector"]
        combined_data = np.array(
            list(patterns.values()) + list(strategies.values()))

        # Update baseline if enough history
        if len(self.knowledge_base) > 0:
            historical_data = np.array([
                list(k.patterns.values()) + list(k.strategies.values())
                for k in self.knowledge_base[-analyzer["history_size"]:]
            ])
            analyzer["baseline"] = np.mean(historical_data, axis=0)

        # Detect anomalies
        deviations = np.abs(combined_data - analyzer["baseline"])
        anomaly_indices = np.where(
            deviations > analyzer["variance_threshold"])[0]

        # Map anomalies to pattern/strategy names
        combined_names = list(patterns.keys()) + list(strategies.keys())
        anomalies = [combined_names[i] for i in anomaly_indices]

        return {
            "detected_anomalies": anomalies
        }

    def _calculate_confidence_scores(
        self,
        patterns: Dict[str, float],
        strategies: Dict[str, float],
        meta_insights: Dict[str, Any]
    ) -> Dict[str, float]:
        """Calculate confidence scores for different aspects."""
        confidence_scores = {}

        # Pattern confidence
        pattern_confidence = np.mean(list(patterns.values()))
        confidence_scores["pattern_confidence"] = float(pattern_confidence)

        # Strategy confidence
        strategy_confidence = np.mean(list(strategies.values()))
        confidence_scores["strategy_confidence"] = float(strategy_confidence)

        # Trend confidence
        trend_confidence = self._calculate_trend_confidence(
            meta_insights["trends"])
        confidence_scores["trend_confidence"] = float(trend_confidence)

        # Correlation confidence
        correlation_confidence = self._calculate_correlation_confidence(
            meta_insights["correlations"]
        )
        confidence_scores["correlation_confidence"] = float(
            correlation_confidence)

        # Overall confidence
        confidence_scores["overall_confidence"] = float(np.mean([
            pattern_confidence,
            strategy_confidence,
            trend_confidence,
            correlation_confidence
        ]))

        return confidence_scores

    def _calculate_trend_confidence(self, trends: Dict[str, List[float]]) -> float:
        """Calculate confidence in trend analysis."""
        all_trends = trends["pattern_trends"] + trends["strategy_trends"]
        return float(np.mean(np.abs(all_trends)))

    def _calculate_correlation_confidence(
        self,
        correlations: Dict[str, List[Tuple[str, str, float]]]
    ) -> float:
        """Calculate confidence in correlation analysis."""
        if not correlations["significant_correlations"]:
            return 0.0
        return float(np.mean([abs(c[2]) for c in correlations["significant_correlations"]]))

    def _extract_behavioral_features(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> np.ndarray:
        """Extract behavioral features from game state."""
        return np.array([
            float(game_state.get("aggression_level", 0.0)),
            float(game_state.get("cooperation_level", 0.0)),
            float(game_state.get("risk_level", 0.0)),
            float(game_state.get("learning_rate", 0.0)),
            float(game_state.get("adaptation_rate", 0.0))
        ])

    def _extract_temporal_features(self, game_state: Dict[str, Any]) -> np.ndarray:
        """Extract temporal features from game state."""
        return np.array([
            float(game_state.get("cycle_phase", 0.0)),
            float(game_state.get("progression_rate", 0.0)),
            float(game_state.get("timing_accuracy", 0.0)),
            float(game_state.get("sequence_position", 0.0))
        ])

    def _extract_spatial_features(self, game_state: Dict[str, Any]) -> np.ndarray:
        """Extract spatial features from game state."""
        return np.array([
            float(game_state.get("clustering_density", 0.0)),
            float(game_state.get("distribution_spread", 0.0)),
            float(game_state.get("movement_speed", 0.0)),
            float(game_state.get("territory_control", 0.0)),
            float(game_state.get("position_advantage", 0.0)),
            float(game_state.get("formation_cohesion", 0.0))
        ])

    def _extract_strategic_features(
        self,
        game_state: Dict[str, Any],
        predictions: Dict[str, Any]
    ) -> np.ndarray:
        """Extract strategic features from game state."""
        return np.array([
            float(game_state.get("resource_efficiency", 0.0)),
            float(game_state.get("combat_effectiveness", 0.0)),
            float(game_state.get("development_progress", 0.0)),
            float(game_state.get("social_influence", 0.0))
        ])

    def _extract_offensive_features(self, game_state: Dict[str, Any]) -> np.ndarray:
        """Extract offensive strategy features."""
        return np.array([
            float(game_state.get("attack_frequency", 0.0)),
            float(game_state.get("tactical_advantage", 0.0)),
            float(game_state.get("opportunity_usage", 0.0))
        ])

    def _extract_defensive_features(self, game_state: Dict[str, Any]) -> np.ndarray:
        """Extract defensive strategy features."""
        return np.array([
            float(game_state.get("protection_level", 0.0)),
            float(game_state.get("reaction_speed", 0.0)),
            float(game_state.get("prevention_effectiveness", 0.0))
        ])

    def _extract_resource_features(self, game_state: Dict[str, Any]) -> np.ndarray:
        """Extract resource strategy features."""
        return np.array([
            float(game_state.get("gathering_rate", 0.0)),
            float(game_state.get("conservation_rate", 0.0)),
            float(game_state.get("investment_ratio", 0.0)),
            float(game_state.get("distribution_efficiency", 0.0))
        ])

    def _extract_social_features(
        self,
        game_state: Dict[str, Any],
        cognitive_state: Dict[str, Any]
    ) -> np.ndarray:
        """Extract social strategy features."""
        return np.array([
            float(game_state.get("cooperation_rate", 0.0)),
            float(game_state.get("competition_level", 0.0)),
            float(game_state.get("diplomatic_influence", 0.0))
        ])

    def _sigmoid(self, x: float) -> float:
        """Apply sigmoid function to scalar value."""
        return 1 / (1 + np.exp(-x))

    async def update(self, feedback: Dict[str, Any]) -> None:
        """Update collective wisdom model based on feedback."""
        try:
            # Update pattern recognition weights
            self._update_pattern_weights(feedback)

            # Update strategy analysis weights
            self._update_strategy_weights(feedback)

            # Update meta-analyzers
            self._update_meta_analyzers(feedback)

            logger.info("Updated collective wisdom model")

        except Exception as e:
            logger.error(f"Error updating collective wisdom model: {str(e)}")
            raise

    def _update_pattern_weights(self, feedback: Dict[str, Any]) -> None:
        """Update pattern recognition weights based on feedback."""
        learning_rate = 0.01

        for pattern_type, weights in self.pattern_weights.items():
            if f"{pattern_type}_accuracy" in feedback:
                accuracy = feedback[f"{pattern_type}_accuracy"]
                gradient = np.array(feedback.get(
                    f"{pattern_type}_gradient", [0] * len(weights)))
                self.pattern_weights[pattern_type] += learning_rate * \
                    accuracy * gradient

    def _update_strategy_weights(self, feedback: Dict[str, Any]) -> None:
        """Update strategy analysis weights based on feedback."""
        learning_rate = 0.01

        for strategy_type, weights in self.strategy_weights.items():
            if f"{strategy_type}_accuracy" in feedback:
                accuracy = feedback[f"{strategy_type}_accuracy"]
                gradient = np.array(feedback.get(
                    f"{strategy_type}_gradient", [0] * len(weights)))
                self.strategy_weights[strategy_type] += learning_rate * \
                    accuracy * gradient

    def _update_meta_analyzers(self, feedback: Dict[str, Any]) -> None:
        """Update meta-analyzers based on feedback."""
        # Update trend analyzer
        if "trend_accuracy" in feedback:
            self.meta_analyzers["trend_analyzer"]["weights"] *= (
                1 + 0.1 * (feedback["trend_accuracy"] - 0.5))

        # Update correlation analyzer
        if "correlation_matrix_update" in feedback:
            update = np.array(feedback["correlation_matrix_update"])
            self.meta_analyzers["correlation_analyzer"]["correlation_matrix"] += 0.1 * update

        # Update anomaly detector
        if "anomaly_feedback" in feedback:
            self.meta_analyzers["anomaly_detector"]["variance_threshold"] *= (
                1 + 0.1 * (feedback["anomaly_feedback"] - 0.5)
            )
