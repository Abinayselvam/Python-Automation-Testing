import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright):

    # SETUP
    api_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        timeout=15000
    )

    # Provide the API context to tests
    yield api_context

    # TEARDOWN
    api_context.dispose()



from Day04_API_Automation.framework.clients.notebook_client import (
    NotebookClient
)


@pytest.fixture
def notebook_client(api_request_context):

    return NotebookClient(api_request_context)