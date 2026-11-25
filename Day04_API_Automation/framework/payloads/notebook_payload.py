from datetime import datetime, timezone
from uuid import uuid4


def create_notebook_payload():

    timestamp = datetime.now(timezone.utc).strftime(
        "%Y%m%d%H%M%S"
    )

    unique_id = uuid4().hex[:8]

    return {
        "title": f"Automation_Notebook_{timestamp}_{unique_id}",
        "description": "Created using API automation"
    }