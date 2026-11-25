
from Day04_API_Automation.framework.payloads.notebook_payload import create_notebook_payload


def test_notebook_crud_lifecycle(notebook_client):

    # 1. Create
    payload = create_notebook_payload()
    create_response = notebook_client.create_notebook(payload)

    assert create_response.status == 201

    created_data = notebook_client.safe_extract_json(
        create_response
    )

    assert created_data is not None

    notebook_id = created_data["id"]

    # 2. Read
    get_response = notebook_client.get_notebook(notebook_id)

    assert get_response.status == 200

    # 3. Update
    update_payload = {
        "title": "Updated_Automation_Notebook"
    }

    update_response = notebook_client.update_notebook(
        notebook_id,
        update_payload
    )

    assert update_response.status == 200

    # 4. Delete
    delete_response = notebook_client.delete_notebook(notebook_id)

    assert delete_response.status == 204