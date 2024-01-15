from functools import cached_property
from typing import Optional

import requests

from ..core.bases import JSONResponse
from ._response_fields import RESPONSE_FIELDS


class ImageProcessingResponse(JSONResponse):
    """Image processing service response."""
    def __init__(
        self,
        response: requests.models.Response
    ) -> None:
        """Initializes a new ImageProcessingResponse."""
        super().__init__(response, RESPONSE_FIELDS)

    @cached_property
    def original_size(self) -> Optional[int]:
        """The original size of the provided image, in bytes."""
        return self._get_response_field("original_size")

    @cached_property
    def original_height(self) -> Optional[int]:
        """The original height of the provided image, in bytes."""
        return self._get_response_field("original_height")

    @cached_property
    def original_width(self) -> Optional[int]:
        """The original width of the provided image, in bytes."""
        return self._get_response_field("original_width")

    @cached_property
    def final_size(self) -> Optional[int]:
        """The final size of the processed image, in bytes."""
        return self._get_response_field("final_size")

    @cached_property
    def bytes_saved(self) -> Optional[int]:
        """The number of bytes saved by optimizing the image, in bytes."""
        return self._get_response_field("bytes_saved")

    @cached_property
    def final_height(self) -> Optional[int]:
        """The final height of the processed image, in bytes."""
        return self._get_response_field("final_height")

    @cached_property
    def final_width(self) -> Optional[int]:
        """The final width of the processed image, in bytes."""
        return self._get_response_field("final_width")

    @cached_property
    def url(self) -> Optional[str]:
        """The URL with the new processed image."""
        return self._get_response_field("url")
