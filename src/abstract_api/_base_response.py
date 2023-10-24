from abc import ABC
from typing import Any

import requests.models


class ResponseMeta:
    """Response meta data for Abstract API service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initialize a new ResponseMeta."""
        self._http_status: int = response.status_code
        self._body: bytes = response.content
        try:
            self._body_json = response.json()
        except:  # noqa: E722
            self._body_json = None

    @property
    def http_status(self) -> int:
        """HTTP status code of API request."""
        return self._http_status

    @property
    def body(self) -> bytes:
        """Raw response body returned from API request."""
        return self._body

    @property
    def body_json(self) -> dict[str, Any]:
        """JSON representation of response body returned from API request."""
        return self._body_json


class BaseResponse(ABC):
    """Base Abstract API service response."""
    meta: ResponseMeta
    _response_fields: frozenset[str]

    def __init__(self, response: requests.models.Response) -> None:
        """Initialize a new BaseResponse."""
        self.meta = ResponseMeta(response)

    def _get_response_field(self, attr_name: str) -> Any:
        """Gets the value of a field that was returned in response.

        Raises:
            AttributeError: When trying to get a value of a field that was
                not returned in response.
        """
        if attr_name not in self._response_fields:
            raise AttributeError(
                f"Field '{attr_name}' was not returned in API response. "
            )

        return getattr(self, f"_{attr_name}")
