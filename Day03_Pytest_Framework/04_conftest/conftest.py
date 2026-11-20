import pytest


@pytest.fixture
def sample_user():
    return {
        "username": "admin",
        "password": "admin123"
    }


@pytest.fixture
def application_url():
    return "https://example.com"