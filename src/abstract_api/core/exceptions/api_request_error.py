from typing import Any, NoReturn, Optional

import requests.models

from .abstract_api_exception import AbstractAPIException


class APIRequestError(AbstractAPIException):
    """Raised when there's a problem with returned in API response."""
    def __init__(
        self,
        http_status: int,
        body: bytes,
        raised_error_message: str,
        message: Optional[str] = None,
        code: Optional[str] = None,
        details: Optional[dict[str, Any]] = None,
    ) -> None:
        """Initializes a new APIRequestError."""
        super().__init__(raised_error_message)
        self._http_status = http_status
        self._body = body
        self._message = message
        self._code = code
        self._details = details

    @property
    def http_status(self) -> int:
        """HTTP status code."""
        return self._http_status

    @property
    def body(self) -> bytes:
        """Response body."""
        return self._body

    @property
    def message(self) -> Optional[str]:
        """Error message returned from API."""
        return self._message

    @property
    def code(self) -> Optional[str]:
        """Error code returned from API."""
        return self._code

    @property
    def details(self) -> Optional[dict[str, Any]]:
        """Error details returned from API."""
        return self._details

    @staticmethod
    def _get_error_details(response_json: dict[str, Any]) -> dict[str, Any]:
        """Extracts error details from response.

        Args:
            response_json: Returned response body as JSON.

        Returns:
            A dict containing error details: message, code, and details.
        """
        error_details = {}

        if response_json and response_json.get("error"):
            error_details["message"] = response_json["error"].get("message")
            error_details["code"] = response_json["error"].get("code")
            error_details["details"] = response_json["error"].get("details")

        return error_details

    @classmethod
    def _build_raised_error_message(
        cls,
        error_details: dict[str, Any],
        http_status: int
    ) -> str:
        """Builds raised error message.

        Args:
            error_details: A dict containing error details.
            http_status: HTTP status code returned with response.

        Returns:
            Raised exception error message.
        """
        raised_error_message = f"API request failed "\
                               f"(HTTP status: {http_status})."
        if error_details.get("message"):
            raised_error_message += f" {error_details['message']}"
            if error_details["details"]:
                raised_error_message += " Details: "
                raised_error_message += str(error_details["details"])
        return raised_error_message

    @classmethod
    def raise_from_response(
        cls,
        response: requests.models.Response
    ) -> NoReturn:
        """Raises an exception from given response.

        Args:
            response: HTTP response object returned from API call.

        Raises:
            APIRequestError: An exception with returned HTTP status code and
                error details returned from API when available.
        """
        try:
            response_json = response.json()
        except Exception:
            response_json = {}

        error_details = cls._get_error_details(response_json)
        raised_error_message = cls._build_raised_error_message(
            error_details, response.status_code
        )
        exc = cls(
            raised_error_message=raised_error_message,
            http_status=response.status_code,
            body=response.content,
            **error_details
        )
        raise exc
