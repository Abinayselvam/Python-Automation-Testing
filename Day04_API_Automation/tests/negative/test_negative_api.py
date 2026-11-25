def test_invalid_token_returns_401(playwright, api_base_url):

    context = playwright.request.new_context(
        base_url=api_base_url,
        extra_http_headers={
            "Authorization": "Bearer invalid_token"
        }
    )

    try:
        response = context.get("/api/notebooks")

        assert response.status == 401

        error_data = response.json()

        assert "message" in error_data

    finally:
        context.dispose()