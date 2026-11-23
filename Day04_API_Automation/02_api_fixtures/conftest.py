import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright):
    api_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        timeout=15000
    )

    yield api_context

    api_context.dispose()