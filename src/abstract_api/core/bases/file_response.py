from typing import ClassVar, Type

import requests

from ._base_response import BaseResponse, BaseResponseMeta


class FileResponseMeta(BaseResponseMeta):
    """Meta data about a file-based API response."""


class FileResponse(BaseResponse):
    """File-based API response."""
    _meta_class: ClassVar[Type[FileResponseMeta]] = FileResponseMeta
    meta: FileResponseMeta

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new FileResponse."""
        super().__init__(response)
        self._content: bytes = response.content

    @property
    def content(self) -> bytes:
        """Raw response body returned from API request."""
        return self._content
