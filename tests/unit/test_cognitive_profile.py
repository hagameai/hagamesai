import pytest
from models.cognitive_profile import CognitiveProfile


def test_cognitive_profile_initialization():
    """
    Test the initialization of the CognitiveProfile class.
    """
    profile = CognitiveProfile(name="Test Profile", attributes={"intelligence": 100})
    assert profile.name == "Test Profile"
    assert profile.attributes == {"intelligence": 100}


def test_cognitive_profile_add_attribute():
    """
    Test adding an attribute to the CognitiveProfile.
    """
    profile = CognitiveProfile(name="Test Profile", attributes={})
    profile.add_attribute("creativity", 85)
    assert profile.attributes["creativity"] == 85


def test_cognitive_profile_remove_attribute():
    """
    Test removing an attribute from the CognitiveProfile.
    """
    profile = CognitiveProfile(name="Test Profile", attributes={"intelligence": 100})
    profile.remove_attribute("intelligence")
    assert "intelligence" not in profile.attributes


def test_cognitive_profile_update_attribute():
    """
    Test updating an existing attribute in the CognitiveProfile.
    """
    profile = CognitiveProfile(name="Test Profile", attributes={"intelligence": 100})
    profile.update_attribute("intelligence", 120)
    assert profile.attributes["intelligence"] == 120
