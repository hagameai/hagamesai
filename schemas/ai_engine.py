"""Pydantic schemas for AI Engine data models."""

from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class GameState(BaseModel):
    """Schema for game state data."""
    game_id: str
    state_type: str = Field(...,
                            description="Type of game state (e.g., 'in_progress', 'completed')")
    player_states: Dict[str, Dict[str, Any]
                        ] = Field(..., description="States of all players")
    game_variables: Dict[str,
                         Any] = Field(..., description="Game-specific variables")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional metadata")


class PredictionRequest(BaseModel):
    """Schema for prediction request."""
    game_state: GameState
    context: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional context")


class PredictionResponse(BaseModel):
    """Schema for prediction response."""
    predictions: Dict[str, Any] = Field(...,
                                        description="Predicted outcomes and actions")
    cognitive_state: Dict[str,
                          Any] = Field(..., description="Current cognitive model state")
    uncertainty: Dict[str, Any] = Field(..., description="Uncertainty factors")
    collective_wisdom: Dict[str,
                            Any] = Field(..., description="Aggregated insights")
    explanations: Dict[str, str] = Field(...,
                                         description="Natural language explanations")
    confidence_scores: Dict[str,
                            float] = Field(..., description="Confidence levels")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class FeedbackRequest(BaseModel):
    """Schema for feedback data."""
    game_id: str
    prediction_accuracy: Dict[str,
                              float] = Field(..., description="Accuracy of predictions")
    cognitive_accuracy: Dict[str,
                             float] = Field(..., description="Accuracy of cognitive model")
    uncertainty_accuracy: Dict[str, float] = Field(
        ..., description="Accuracy of uncertainty estimates")
    wisdom_relevance: Dict[str, float] = Field(
        ..., description="Relevance of collective insights")
    explanation_clarity: Dict[str,
                              float] = Field(..., description="Clarity of explanations")
    context: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional context")


class CognitiveProfile(BaseModel):
    """Schema for cognitive profile data."""
    player_id: str
    learning_style: str = Field(..., description="Identified learning style")
    decision_making: Dict[str,
                          float] = Field(..., description="Decision-making metrics")
    attention_patterns: Dict[str,
                             float] = Field(..., description="Attention-related metrics")
    skill_levels: Dict[str,
                       float] = Field(..., description="Various skill measurements")
    adaptability: float = Field(..., description="Overall adaptability score")
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional metadata")


class CollectiveKnowledge(BaseModel):
    """Schema for collective wisdom data."""
    game_id: str
    patterns: Dict[str, float] = Field(..., description="Identified patterns")
    strategies: Dict[str,
                     float] = Field(..., description="Effective strategies")
    meta_insights: Dict[str,
                        Any] = Field(..., description="Meta-level insights")
    confidence_scores: Dict[str,
                            float] = Field(..., description="Confidence in insights")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class UncertaintyFactors(BaseModel):
    """Schema for uncertainty data."""
    game_id: str
    player_uncertainty: Dict[str, float] = Field(
        ..., description="Player-related uncertainties")
    game_state_uncertainty: Dict[str, float] = Field(
        ..., description="Game state uncertainties")
    environmental_uncertainty: Dict[str, float] = Field(
        ..., description="Environmental uncertainties")
    composite_uncertainty: float = Field(...,
                                         description="Overall uncertainty score")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class Explanation(BaseModel):
    """Schema for AI explanations."""
    game_id: str
    decision_explanations: Dict[str,
                                str] = Field(..., description="Decision explanations")
    feature_importance: Dict[str,
                             float] = Field(..., description="Feature importance scores")
    counterfactuals: List[Dict[str, Any]
                          ] = Field(..., description="Counterfactual scenarios")
    confidence_levels: Dict[str,
                            float] = Field(..., description="Confidence in explanations")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

# Response models for API endpoints


class CognitiveProfileResponse(BaseModel):
    """Response model for cognitive profile endpoint."""
    profile: CognitiveProfile
    metadata: Optional[Dict[str, Any]] = None


class CollectiveWisdomResponse(BaseModel):
    """Response model for collective wisdom endpoint."""
    knowledge: CollectiveKnowledge
    metadata: Optional[Dict[str, Any]] = None


class UncertaintyResponse(BaseModel):
    """Response model for uncertainty factors endpoint."""
    factors: UncertaintyFactors
    metadata: Optional[Dict[str, Any]] = None


class ExplanationResponse(BaseModel):
    """Response model for explanations endpoint."""
    explanation: Explanation
    metadata: Optional[Dict[str, Any]] = None
