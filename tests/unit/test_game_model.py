import pytest
from models.game_definition import GameDefinition  # Import the GameDefinition model to be tested


def test_game_definition_creation():
    """
    Test the creation of a GameDefinition object.
    """
    game = GameDefinition(name="Chess", description="A strategic board game.")
    assert game.name == "Chess"
    assert game.description == "A strategic board game."


def test_game_definition_str():
    """
    Test the string representation of the GameDefinition object.
    """
    game = GameDefinition(name="Checkers", description="A game played on an 8x8 board.")
    assert str(game) == "Checkers: A game played on an 8x8 board."


def test_game_definition_update():
    """
    Test updating the GameDefinition attributes.
    """
    game = GameDefinition(name="Tic Tac Toe", description="A simple game.")
    game.name = "Tic Tac Toe Updated"
    game.description = "An updated description."
    assert game.name == "Tic Tac Toe Updated"
    assert game.description == "An updated description."


def test_game_definition_invalid_name():
    """
    Test creating a GameDefinition with an invalid name (e.g., empty string).
    """
    with pytest.raises(ValueError):
        GameDefinition(name="", description="Invalid game definition.")


def test_game_definition_invalid_description():
    """
    Test creating a GameDefinition with an invalid description (e.g., none).
    """
    with pytest.raises(ValueError):
        GameDefinition(name="Valid Game", description=None) 
