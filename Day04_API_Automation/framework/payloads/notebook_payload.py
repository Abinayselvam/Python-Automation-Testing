from datetime import datetime, timezone
from uuid import uuid4


def create_notebook_payload():

    unique_id = uuid4().hex[:8]

    timestamp = datetime.now(
        timezone.utc
    ).strftime("%Y%m%d%H%M%S")

    payload = {
        "title": f"Automation_Notebook_{timestamp}_{unique_id}",
        "description": "Created using Playwright API automation"
    }

    return payload