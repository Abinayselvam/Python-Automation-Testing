def test_get_post(api_request_context):

    response = api_request_context.get("/posts/1")

    assert response.status == 200

    response_data = response.json()

    assert response_data["id"] == 1
    assert response_data["title"]
    assert response_data["body"]