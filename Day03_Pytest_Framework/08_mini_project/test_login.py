import pytest


@pytest.fixture
def valid_credentials():
    return {
        "username": "admin",
        "password": "admin123"
    }


def authenticate(username, password):
    if username == "admin" and password == "admin123":
        return "success"

    return "failure"


@pytest.mark.smoke
@pytest.mark.login
def test_successful_login(valid_credentials):
    result = authenticate(
        valid_credentials["username"],
        valid_credentials["password"]
    )

    assert result == "success"


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("admin", "wrong123", "failure"),
        ("", "", "failure"),
        ("user1", "password123", "failure"),
        ("admin", "admin123", "success")
    ]
)
def test_login_scenarios(username, password, expected):
    result = authenticate(username, password)

    assert result == expected