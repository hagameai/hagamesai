from fastapi import APIRouter, HTTPException, Depends
from typing import List

from crud.game_definition import GameDefinitionCRUD
from crud.game_instance import GameInstanceCRUD
from schemas.game_definition import GameDefinitionCreate, GameDefinitionUpdate, GameDefinition
from schemas.game_instance import GameInstanceCreate, GameInstanceUpdate, GameInstance

router = APIRouter()

def get_game_definition_crud():
    return GameDefinitionCRUD()

def get_game_instance_crud():
    return GameInstanceCRUD()

@router.post('/game-definitions/', response_model=GameDefinition)
async def create_game_definition(game_definition: GameDefinitionCreate, crud: GameDefinitionCRUD = Depends(get_game_definition_crud)):
    return await crud.create(game_definition)

@router.get('/game-definitions/', response_model=List[GameDefinition])
async def list_game_definitions(crud: GameDefinitionCRUD = Depends(get_game_definition_crud)):
    return await crud.get_all()

@router.put('/game-definitions/{game_id}', response_model=GameDefinition)
async def update_game_definition(game_id: int, game_definition: GameDefinitionUpdate, crud: GameDefinitionCRUD = Depends(get_game_definition_crud)):
    existing_definition = await crud.get(game_id)
    if not existing_definition:
        raise HTTPException(status_code=404, detail='Game definition not found')
    return await crud.update(game_id, game_definition)

@router.delete('/game-definitions/{game_id}', status_code=204)
async def delete_game_definition(game_id: int, crud: GameDefinitionCRUD = Depends(get_game_definition_crud)):
    existing_definition = await crud.get(game_id)
    if not existing_definition:
        raise HTTPException(status_code=404, detail='Game definition not found')
    await crud.delete(game_id)

@router.post('/game-instances/', response_model=GameInstance)
async def create_game_instance(game_instance: GameInstanceCreate, crud: GameInstanceCRUD = Depends(get_game_instance_crud)):
    return await crud.create(game_instance)

@router.get('/game-instances/', response_model=List[GameInstance])
async def list_game_instances(crud: GameInstanceCRUD = Depends(get_game_instance_crud)):
    return await crud.get_all()

@router.put('/game-instances/{instance_id}', response_model=GameInstance)
async def update_game_instance(instance_id: int, game_instance: GameInstanceUpdate, crud: GameInstanceCRUD = Depends(get_game_instance_crud)):
    existing_instance = await crud.get(instance_id)
    if not existing_instance:
        raise HTTPException(status_code=404, detail='Game instance not found')
    return await crud.update(instance_id, game_instance)

@router.delete('/game-instances/{instance_id}', status_code=204)
async def delete_game_instance(instance_id: int, crud: GameInstanceCRUD = Depends(get_game_instance_crud)):
    existing_instance = await crud.get(instance_id)
    if not existing_instance:
        raise HTTPException(status_code=404, detail='Game instance not found')
    await crud.delete(instance_id)