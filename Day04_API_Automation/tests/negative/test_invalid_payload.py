def test_empty_notebook_title(authenticated_api):

    invalid_payload = {
        "title": "",
        "description": "Testing invalid data"
    }

    response = authenticated_api.post(
        "/api/notebooks",
        data=invalid_payload
    )

    assert response.status == 400