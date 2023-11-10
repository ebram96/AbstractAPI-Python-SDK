from typing import TYPE_CHECKING

import requests

from abstract_api.bases import JSONResponse

from .response_fields import RESPONSE_FIELDS


class ImageProcessingResponse(JSONResponse):
    """Image processing service response."""
    def __init__(
        self,
        response: requests.models.Response
    ) -> None:
        """Initializes a new ImageProcessingResponse."""
        super().__init__(response)
        self._response_fields = RESPONSE_FIELDS
        not_in_response = object()
        for field in RESPONSE_FIELDS:
            if TYPE_CHECKING:
                assert isinstance(self.meta.body_json, dict)
            value = self.meta.body_json.get(field, not_in_response)
            # Set property only if field was returned
            if value is not not_in_response:
                setattr(self, f"_{field}", value)

    @property
    def original_size(self) -> str | None:
        """The original size of the provided image, in bytes."""
        return self._get_response_field("original_size")

    @property
    def original_height(self) -> str | None:
        """The original height of the provided image, in bytes."""
        return self._get_response_field("original_height")

    @property
    def original_width(self) -> str | None:
        """The original width of the provided image, in bytes."""
        return self._get_response_field("original_width")

    @property
    def final_size(self) -> str | None:
        """The final size of the processed image, in bytes."""
        return self._get_response_field("final_size")

    @property
    def bytes_saved(self) -> str | None:
        """The number of bytes saved by optimizing the image, in bytes."""
        return self._get_response_field("bytes_saved")

    @property
    def final_height(self) -> str | None:
        """The final height of the processed image, in bytes."""
        return self._get_response_field("final_height")

    @property
    def final_width(self) -> str | None:
        """The final width of the processed image, in bytes."""
        return self._get_response_field("final_width")

    @property
    def url(self) -> str | None:
        """The URL with the new processed image."""
        return self._get_response_field("url")
