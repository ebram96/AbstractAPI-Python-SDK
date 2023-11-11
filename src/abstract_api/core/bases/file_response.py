from typing import ClassVar, Type

import requests

from ._base_response import BaseResponse, BaseResponseMeta


class FileResponseMeta(BaseResponseMeta):
    """TODO."""


class FileResponse(BaseResponse):
    """TODO."""
    _meta_class: ClassVar[Type[FileResponseMeta]] = FileResponseMeta
    meta: FileResponseMeta

    def __init__(self, response: requests.models.Response) -> None:
        """Initialize a new ResponseMeta."""
        super().__init__(response)
        self._content: bytes = response.content

    @property
    def content(self) -> bytes:
        """Raw response body returned from API request."""
        return self._content
