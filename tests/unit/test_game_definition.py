import pytest
from crud.game_definition import GameDefinition


def test_game_definition_creation():
    """Test the creation of a game definition."""
    game_def = GameDefinition(
        title="Test Game",
        description="A basic test game",
        rules="These are the rules of the test game."
    )
    assert game_def.title == "Test Game"
    assert game_def.description == "A basic test game"
    assert game_def.rules == "These are the rules of the test game."


def test_game_definition_invalid_title():
    """Test that creating a game definition with an invalid title raises an error."""
    with pytest.raises(ValueError):
        GameDefinition(title="", description="A game with no title", rules="Some rules")


def test_game_definition_update():
    """Test updating a game definition."""
    game_def = GameDefinition(
        title="Initial Title",
        description="Initial Description",
        rules="Initial rules"
    )
    game_def.title = "Updated Title"
    assert game_def.title == "Updated Title"


def test_game_definition_serialization():
    """Test that a game definition can be serialized correctly."""
    game_def = GameDefinition(
        title="Serializable Game",
        description="Can be serialized",
        rules="Different rules"
    )
    serialized = game_def.serialize()  # Assuming serialize method exists
    expected_serialized = {
        "title": "Serializable Game",
        "description": "Can be serialized",
        "rules": "Different rules"
    }
    assert serialized == expected_serialized
