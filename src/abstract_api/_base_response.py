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

    def __init__(self, response: requests.models.Response) -> None:
        """Initialize a new BaseResponse."""
        self.meta = ResponseMeta(response)
