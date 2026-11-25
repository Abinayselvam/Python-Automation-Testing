import os

import pytest
from dotenv import load_dotenv


load_dotenv()


@pytest.fixture
def invalid_token_api(playwright):

    context = playwright.request.new_context(
        base_url=os.getenv("APP_API_URL"),
        extra_http_headers={
            "Authorization": "Bearer invalid_token",
            "Accept": "application/json"
        }
    )

    yield context

    context.dispose()


def test_invalid_token_returns_401(invalid_token_api):

    response = invalid_token_api.get("/api/notebooks")

    assert response.status == 401