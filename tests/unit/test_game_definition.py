import pytest
from crud.game_definition import GameDefinition


def test_create_game_definition():
    """
    Test the creation of a game definition.
    """
    game_def = GameDefinition(name="Test Game", description="A test game")
    assert game_def.name == "Test Game"
    assert game_def.description == "A test game"


def test_update_game_definition():
    """
    Test the updating of a game definition.
    """
    game_def = GameDefinition(name="Test Game", description="A test game")
    game_def.update(name="Updated Game")
    assert game_def.name == "Updated Game"


def test_delete_game_definition():
    """
    Test the deletion of a game definition.
    """
    game_def = GameDefinition(name="Test Game", description="A test game")
    game_def.delete()
    assert game_def.is_deleted() is True


def test_game_definition_repr():
    """
    Test the string representation of a game definition.
    """
    game_def = GameDefinition(name="Test Game", description="A test game")
    assert repr(game_def) == "GameDefinition(name='Test Game', description='A test game')"