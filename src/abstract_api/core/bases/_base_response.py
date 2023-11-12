from abc import ABC
from typing import ClassVar, Type

import requests.models


class BaseResponseMeta(ABC):
    """Base response metadata for Abstract API service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initialize a new ResponseMeta."""
        self._http_status: int = response.status_code
        self._body: bytes = response.content

    @property
    def http_status(self) -> int:
        """HTTP status code of API request."""
        return self._http_status

    @property
    def body(self) -> bytes:
        """Raw response body returned from API request."""
        return self._body


class BaseResponse(ABC):
    """Base Abstract API service response.

    Attributes:
        _meta_class: Class (type) of response metadata instance.
    """
    _meta_class: ClassVar[Type[BaseResponseMeta]]

    def __init__(self, response: requests.models.Response) -> None:
        """Initialize a new BaseResponse."""
        self._meta: BaseResponseMeta = self._meta_class(response)

    @property
    def meta(self) -> BaseResponseMeta:
        """Metadata about response."""
        return self._meta
