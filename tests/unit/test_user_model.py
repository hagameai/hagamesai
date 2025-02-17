import pytest
from models.user import User


def test_user_creation():
    """Test the creation of a User instance."""
    user = User(username='test_user', email='test@example.com')
    assert user.username == 'test_user'
    assert user.email == 'test@example.com'


def test_user_str():
    """Test the string representation of a User instance."""
    user = User(username='test_user', email='test@example.com')
    assert str(user) == 'User(test_user, test@example.com)'


def test_user_email_validation():
    """Test email validation for User instance."""
    with pytest.raises(ValueError):
        User(username='test_user', email='invalid_email')


def test_user_update():
    """Test updating user details."""
    user = User(username='test_user', email='test@example.com')
    user.update(username='new_user', email='new@example.com')
    assert user.username == 'new_user'
    assert user.email == 'new@example.com'


def test_user_profile_link():
    """Test the link to the user profile."""
    user = User(username='test_user', email='test@example.com')
    assert user.get_profile_link() == '/profiles/test_user'