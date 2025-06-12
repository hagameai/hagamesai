"""API router for AI Engine endpoints."""

from typing import Dict, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from core.auth import get_current_user
from core.ai_engine import (
    AIEngine,
    AdaptivePredictionEngine,
    CognitiveModelBuilder,
    QuantumUncertaintyGenerator,
    CollectiveWisdomAggregator,
    ExplainableAI
)
from schemas.user import User
from schemas.game import GameState

router = APIRouter(prefix="/ai", tags=["AI Engine"])

# Initialize AI Engine components
ai_engine = AIEngine()


@router.on_event("startup")
async def initialize_ai_engine():
    """Initialize AI Engine components on startup."""
    await ai_engine.initialize_components()


@router.post("/predict")
async def predict_game_state(
    game_state: GameState,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """
    Process current game state and make predictions.

    This endpoint:
    1. Generates uncertainty factors
    2. Updates cognitive model
    3. Makes predictions
    4. Aggregates collective wisdom
    5. Provides explanations
    """
    try:
        # Prepare input data
        input_data = {
            "game_id": game_state.game_id,
            "player_id": current_user.id,
            "game_state": game_state.dict(),
            "player_state": {
                "id": current_user.id,
                "profile": current_user.profile.dict() if current_user.profile else {}
            }
        }

        # Process game state through AI Engine
        result = await ai_engine.process_game_state(input_data)

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing game state: {str(e)}"
        )


@router.post("/feedback")
async def provide_feedback(
    feedback: Dict[str, Any],
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, str]:
    """
    Provide feedback to update AI models.

    This endpoint accepts feedback about:
    - Prediction accuracy
    - Cognitive model accuracy
    - Uncertainty estimation accuracy
    - Collective wisdom relevance
    - Explanation clarity
    """
    try:
        # Add user context to feedback
        feedback["player_id"] = current_user.id

        # Update AI components with feedback
        await ai_engine.update_components(feedback)

        return {"status": "Feedback processed successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing feedback: {str(e)}"
        )


@router.get("/cognitive-profile/{player_id}")
async def get_cognitive_profile(
    player_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """Get cognitive profile for a player."""
    try:
        if current_user.id != player_id and not current_user.is_admin:
            raise HTTPException(
                status_code=403,
                detail="Not authorized to access this profile"
            )

        cognitive_builder = ai_engine.cognitive_builder
        if not cognitive_builder:
            raise HTTPException(
                status_code=500,
                detail="Cognitive Model Builder not initialized"
            )

        profile = cognitive_builder.profiles.get(player_id)
        if not profile:
            raise HTTPException(
                status_code=404,
                detail="Cognitive profile not found"
            )

        return profile.dict()

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving cognitive profile: {str(e)}"
        )


@router.get("/collective-wisdom/{game_id}")
async def get_collective_wisdom(
    game_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """Get collective wisdom insights for a game."""
    try:
        wisdom_aggregator = ai_engine.wisdom_aggregator
        if not wisdom_aggregator:
            raise HTTPException(
                status_code=500,
                detail="Collective Wisdom Aggregator not initialized"
            )

        # Get latest knowledge for the game
        knowledge = next(
            (k for k in reversed(wisdom_aggregator.knowledge_base)
             if k.game_id == game_id),
            None
        )

        if not knowledge:
            raise HTTPException(
                status_code=404,
                detail="No collective wisdom found for this game"
            )

        return knowledge.dict()

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving collective wisdom: {str(e)}"
        )


@router.get("/explanations/{game_id}")
async def get_explanations(
    game_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """Get AI explanations for a game."""
    try:
        xai_system = ai_engine.xai_system
        if not xai_system:
            raise HTTPException(
                status_code=500,
                detail="Explainable AI system not initialized"
            )

        # Get latest explanation for the game
        explanation = next(
            (e for e in reversed(xai_system.explanation_history)
             if e.game_id == game_id),
            None
        )

        if not explanation:
            raise HTTPException(
                status_code=404,
                detail="No explanations found for this game"
            )

        return explanation.dict()

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving explanations: {str(e)}"
        )


@router.get("/uncertainty/{game_id}")
async def get_uncertainty_factors(
    game_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """Get uncertainty factors for a game."""
    try:
        uncertainty_generator = ai_engine.quantum_generator
        if not uncertainty_generator:
            raise HTTPException(
                status_code=500,
                detail="Quantum Uncertainty Generator not initialized"
            )

        # Get latest uncertainty factors for the game
        factors = next(
            (f for f in reversed(uncertainty_generator.uncertainty_history)
             if f.game_id == game_id),
            None
        )

        if not factors:
            raise HTTPException(
                status_code=404,
                detail="No uncertainty factors found for this game"
            )

        return factors.dict()

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving uncertainty factors: {str(e)}"
        )
