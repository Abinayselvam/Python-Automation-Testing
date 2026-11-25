from Day04_API_Automation.framework.base_api import BaseAPI


def test_base_api_get(api_request_context):

    api = BaseAPI(api_request_context)

    response = api.get("/posts/1")

    assert response.status == 200

    data = api.safe_extract_json(response)

    assert data is not None
    assert data["id"] == 1