import pytest


@pytest.fixture
def sample_user():
    print("\nPreparing test user")
    return {
        "username": "admin",
        "password": "admin123"
    }


def test_username(sample_user):
    assert sample_user["username"] == "admin"


def test_password(sample_user):
    assert sample_user["password"] == "admin123"