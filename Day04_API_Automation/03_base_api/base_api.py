import logging
from typing import Any

from playwright.sync_api import APIRequestContext, APIResponse

logger = logging.getLogger(__name__)

class BaseAPI:
    #constructor
    def __init__(self, request: APIRequestContext):
        self.request = request

    def get(self, endpoint: str, **kwargs) -> APIResponse:
        logger.info("GET %s", endpoint)
        return self.request.get(endpoint, **kwargs)

    def post(
        self,
        endpoint: str,
        payload: dict[str, Any],
        **kwargs
    ) -> APIResponse:
        logger.info("POST %s", endpoint)
        return self.request.post(
            endpoint,
            data=payload,
            **kwargs
        )

    def patch(
        self,
        endpoint: str,
        payload: dict[str, Any],
        **kwargs
    ) -> APIResponse:
        logger.info("PATCH %s", endpoint)
        return self.request.patch(
            endpoint,
            data=payload,
            **kwargs
        )

    def delete(self, endpoint: str, **kwargs) -> APIResponse:
        logger.info("DELETE %s", endpoint)
        return self.request.delete(endpoint, **kwargs)

    @staticmethod
    def safe_extract_json(response: APIResponse):
        if response.status == 204:
            return None

        content_type = response.headers.get("content-type", "")

        if "application/json" not in content_type.lower():
            logger.warning(
                "Response is not JSON. Status: %s",
                response.status
            )
            return None

        try:
            return response.json()
        except (ValueError, TypeError):
            logger.exception("Unable to parse JSON response")
            return None
