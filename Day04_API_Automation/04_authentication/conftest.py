import os
import pytest


@pytest.fixture(scope="session")
def auth_token(playwright):
    base_url = os.getenv("APP_API_URL")
    username = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")

    if not all([base_url, username, password]):
        pytest.fail("Missing API authentication configuration")

    context = playwright.request.new_context(
        base_url=base_url
    )

    try:
        response = context.post(
            "/api/auth/login",
            data={
                "username": username,
                "password": password
            }
        )

        assert response.status == 200, (
            f"Login failed: {response.status}"
        )

        body = response.json()
        token = body.get("accessToken")

        assert token, "Access token missing from login response"

        return token

    finally:
        context.dispose()


@pytest.fixture(scope="session")
def authenticated_api(playwright, auth_token):
    context = playwright.request.new_context(
        base_url=os.getenv("APP_API_URL"),
        extra_http_headers={
            "Authorization": f"Bearer {auth_token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )

    yield context

    context.dispose()