from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional

from schemas.ai_model import AIModelCreate, AIModelRead, AIModelUpdate
from services import AIModelService
from core.database import get_db
from models.cognitive_profile import CognitiveProfile

router = APIRouter(prefix="/ai_models", tags=["ai_models"])


@router.post("/", response_model=AIModelRead)
async def create_model(
    model_data: AIModelCreate,
    db: Session = Depends(get_db)
):
    """Create a new AI model."""
    service = AIModelService(db)
    return await service.create_model(model_data)


@router.get("/{model_id}", response_model=AIModelRead)
async def get_model(
    model_id: int,
    db: Session = Depends(get_db)
):
    """Get AI model by ID."""
    service = AIModelService(db)
    model = await service.get_model(model_id)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return model


@router.put("/{model_id}", response_model=AIModelRead)
async def update_model(
    model_id: int,
    model_data: AIModelUpdate,
    db: Session = Depends(get_db)
):
    """Update AI model configuration."""
    service = AIModelService(db)
    return await service.update_model(model_id, model_data)


@router.post("/{model_id}/predict")
async def predict(
    model_id: int,
    input_data: Dict[str, Any],
    cognitive_profile: Optional[CognitiveProfile] = None,
    db: Session = Depends(get_db)
):
    """Generate predictions using the AI model."""
    service = AIModelService(db)
    return await service.predict(model_id, input_data, cognitive_profile)


@router.post("/{model_id}/explain")
async def explain(
    model_id: int,
    input_data: Dict[str, Any],
    db: Session = Depends(get_db)
):
    """Generate model explanations."""
    service = AIModelService(db)
    return await service.explain(model_id, input_data)
