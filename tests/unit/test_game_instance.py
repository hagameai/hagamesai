import pytest
from crud.game_instance import GameInstanceCRUD  # Import your CRUD operations
from models.game_instance import GameInstance  # Import your GameInstance model


@pytest.fixture
def game_instance_data():
    return {
        "name": "Test Game",
        "description": "A game for testing purposes",
        "status": "active"
    }


def test_create_game_instance(game_instance_data):
    instance = GameInstanceCRUD.create(**game_instance_data)
    assert instance.id is not None
    assert instance.name == game_instance_data['name']
    assert instance.description == game_instance_data['description']
    assert instance.status == game_instance_data['status']


def test_read_game_instance(game_instance_data):
    instance = GameInstanceCRUD.create(**game_instance_data)
    fetched_instance = GameInstanceCRUD.read(instance.id)
    assert fetched_instance.id == instance.id
    assert fetched_instance.name == instance.name


def test_update_game_instance(game_instance_data):
    instance = GameInstanceCRUD.create(**game_instance_data)
    updated_data = {"name": "Updated Game"}
    updated_instance = GameInstanceCRUD.update(instance.id, **updated_data)
    assert updated_instance.name == updated_data['name']


def test_delete_game_instance(game_instance_data):
    instance = GameInstanceCRUD.create(**game_instance_data)
    GameInstanceCRUD.delete(instance.id)
    fetched_instance = GameInstanceCRUD.read(instance.id)
    assert fetched_instance is None  # Assuming None is returned when not found
