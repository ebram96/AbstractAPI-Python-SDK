import json
from typing import Any, BinaryIO

from ..core.bases import BaseService
from ..core.exceptions import ClientRequestError
from .image_processing_response import ImageProcessingResponse
from .strategies import BaseStrategy


class ImageProcessing(BaseService[ImageProcessingResponse]):
    """AbstractAPI image processing service.

    Used to convert, compress, or optimize an image.

    Attributes:
        _subdomain: Image processing service subdomain.
    """
    _subdomain = "images"

    def upload(
        self,
        image: BinaryIO,
        lossy: bool | None = None,
        quality: int | None = None,
        resize: BaseStrategy | None = None
    ) -> ImageProcessingResponse:
        """Can convert, compress, or optimize an image.

        Args:
            image: The image to be processed, it should be a file-like or a
                file opened in binary reading mode.
            lossy: If True, the API will perform a lossy compression on the
                image, reducing the size massively with a small drop in
                image quality. If False, the image size will only be reduced
                slightly (10% - 20% at most), but there will be no reduction
                in image quality. The default value is False if this is not
                provided.
            quality: This is an integer between 0 and 100 that determines
                the quality level for lossy compression. If not submitted
                it will be determined intelligently by AbstractAPI.
                Generally a quality above 95 is useless and may result in
                an image that is larger than the input image, and a quality
                below 25 will result in an image so low in quality that it
                will be useless.
            resize: This is an instance of BaseStrategy subclasses that
                specifies how to resize the image. If not provided, we will
                only compress the image as desired.

        Returns:
            ImageProcessingResponse representing API call response.
        """
        return self._process(
            image=image,
            lossy=lossy,
            quality=quality,
            resize=resize
        )

    def url(
        self,
        url: str,
        lossy: bool | None = None,
        quality: int | None = None,
        resize: BaseStrategy | None = None
    ) -> ImageProcessingResponse:
        """Can convert, compress, or optimize an image in the given URL.

        Args:
            url: The URL of the image that you would like to edit.
                Note that is cannot be more than 32 MB in size.
            lossy: If True, the API will perform a lossy compression on the
                image, reducing the size massively with a small drop in
                image quality. If False, the image size will only be reduced
                slightly (10% - 20% at most), but there will be no reduction
                in image quality. The default value is False if this is not
                provided.
            quality: This is an integer between 0 and 100 that determines
                the quality level for lossy compression. If not submitted
                it will be determined intelligently by AbstractAPI.
                Generally a quality above 95 is useless and may result in
                an image that is larger than the input image, and a quality
                below 25 will result in an image so low in quality that it
                will be useless.
            resize: This is an instance of BaseStrategy subclasses that
                specifies how to resize the image. If not provided, we will
                only compress the image as desired.

        Returns:
            ImageProcessingResponse representing API call response.
        """
        return self._process(
            url=url,
            lossy=lossy,
            quality=quality,
            resize=resize
        )

    def _process(
        self,
        image: BinaryIO | None = None,
        url: str | None = None,
        lossy: bool | None = None,
        quality: int | None = None,
        resize: BaseStrategy | None = None
    ) -> ImageProcessingResponse:

        if image is None and url is None:
            raise ClientRequestError("Image or URL must be passed")

        data: dict[str, Any] = {"api_key": self._api_key}
        if resize is not None:
            data["resize"] = resize.json()
        if lossy is not None:
            data["lossy"] = lossy
        if quality is not None:
            data["quality"] = quality

        action = "upload/" if image is not None else "url/"
        service_kwargs: dict[str, Any] = {
            "_response_class": ImageProcessingResponse,
            "_action": action,
            "_method": "POST"
        }
        if action == "upload/":
            service_kwargs["_files"] = {
                "image": image,
                "data": (None, json.dumps(data))
            }
        else:
            service_kwargs["_body"] = data | {"url": url}

        return self._service_request(**service_kwargs)
