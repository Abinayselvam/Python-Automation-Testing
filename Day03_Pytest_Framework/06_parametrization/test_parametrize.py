import pytest


@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("admin", "admin123", True),
        ("admin", "wrong123", False),
        ("", "", False),
        ("user1", "password123", False),
    ]
)
def test_login_validation(username, password, expected):
    is_valid = (
        username == "admin"
        and password == "admin123"
    )

    assert is_valid == expected