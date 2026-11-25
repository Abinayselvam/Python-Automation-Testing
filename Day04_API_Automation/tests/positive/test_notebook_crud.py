from Day04_API_Automation.framework.payloads.notebook_payload import (
    create_notebook_payload
)


def test_notebook_crud_lifecycle(notebook_client):

    notebook_id = None

    try:

        # STEP 1: CREATE
        create_payload = create_notebook_payload()

        create_response = notebook_client.create_notebook(
            create_payload
        )

        assert create_response.status == 201

        created_data = notebook_client.safe_extract_json(
            create_response
        )

        assert created_data is not None

        notebook_id = created_data["id"]

        assert created_data["title"] == create_payload["title"]

        # STEP 2: READ
        get_response = notebook_client.get_notebook(
            notebook_id
        )

        assert get_response.status == 200

        notebook_data = notebook_client.safe_extract_json(
            get_response
        )

        assert notebook_data is not None

        assert notebook_data["id"] == notebook_id

        assert notebook_data["title"] == create_payload["title"]

        # STEP 3: UPDATE
        update_payload = {
            "title": f"Updated_{create_payload['title']}"
        }

        update_response = notebook_client.update_notebook(
            notebook_id,
            update_payload
        )

        assert update_response.status == 200

        updated_data = notebook_client.safe_extract_json(
            update_response
        )

        assert updated_data is not None

        assert updated_data["title"] == update_payload["title"]

        # STEP 4: DELETE
        delete_response = notebook_client.delete_notebook(
            notebook_id
        )

        assert delete_response.status == 204

        assert (
            notebook_client.safe_extract_json(delete_response)
            is None
        )

        notebook_id = None

    finally:

        # CLEANUP
        if notebook_id is not None:

            cleanup_response = notebook_client.delete_notebook(
                notebook_id
            )

            assert cleanup_response.status in (200, 202, 204, 404)