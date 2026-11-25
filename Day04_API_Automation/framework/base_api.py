import logging
import json

from playwright.sync_api import APIRequestContext, APIResponse


logger = logging.getLogger(__name__)


class BaseAPI:

    def __init__(self, request: APIRequestContext):
        self.request = request

    def get(self, endpoint: str, **kwargs) -> APIResponse:

        logger.info("GET request: %s", endpoint)

        response = self.request.get(
            endpoint,
            **kwargs
        )

        logger.info("GET response status: %s", response.status)

        return response

    def post(
        self,
        endpoint: str,
        payload: dict,
        **kwargs
    ) -> APIResponse:

        logger.info("POST request: %s", endpoint)

        response = self.request.post(
            endpoint,
            data=payload,
            **kwargs
        )

        logger.info("POST response status: %s", response.status)

        return response

    def patch(
        self,
        endpoint: str,
        payload: dict,
        **kwargs
    ) -> APIResponse:

        logger.info("PATCH request: %s", endpoint)

        response = self.request.patch(
            endpoint,
            data=payload,
            **kwargs
        )

        logger.info("PATCH response status: %s", response.status)

        return response

    def delete(self, endpoint: str, **kwargs) -> APIResponse:

        logger.info("DELETE request: %s", endpoint)

        response = self.request.delete(
            endpoint,
            **kwargs
        )

        logger.info("DELETE response status: %s", response.status)

        return response

    @staticmethod
    def safe_extract_json(response: APIResponse):

        # A 204 response has no body
        if response.status == 204:
            return None

        # Check the response content type
        content_type = response.headers.get(
            "content-type", ""
        )

        if "application/json" not in content_type.lower():
            logger.warning("Response does not contain JSON")
            return None

        # Safely parse the response body
        try:
            return json.loads(response.text())

        except json.JSONDecodeError:
            logger.exception("Invalid JSON response")
            return None