from ..core.bases import BaseService
from ..core.exceptions import ClientRequestError
from ..core.validators import numerical
from .avatars_response import AvatarsResponse


class Avatars(BaseService[AvatarsResponse]):
    """AbstractAPI avatar generation service.

    Used for creating highly customizable avatar images with a person's name or
    initials to improve your user experience.

    Attributes:
        _subdomain: Avatars service subdomain.
    """
    _subdomain = "avatars"

    @staticmethod
    def _validate_params(**kwargs) -> None:
        """Validates passed service parameters."""
        ranged = {
            "image_size": (6, 512),
            "font_size": (0.1, 1.0),
            "char_limit": (1, 2)
        }
        for param, allowed_range in ranged.items():
            numerical.between(param, kwargs[param], *allowed_range)

        image_format = kwargs["image_format"]
        if image_format and image_format not in ["png", "svg"]:
            raise ClientRequestError(
                "'image_format' must be either 'png' or 'svg'"
            )

    def create(
        self,
        name: str,
        image_size: int | None = None,
        image_format: str | None = None,
        font_size: float | None = None,
        char_limit: int | None = None,
        background_color: str | None = None,
        font_color: str | None = None,
        is_rounded: bool | None = None,
        is_uppercase: bool | None = None,
        is_italic: bool | None = None,
        is_bold: bool | None = None
    ) -> AvatarsResponse:
        """Create a new avatar with the given parameters.

        Args:
            name: The name you want to create an avatar for.
                You can submit multiple names (such as first, middle, and last)
                and the API will default to displaying two letters in
                the avatar. You can change the number of letters displayed with
                the char_limit parameter.
            image_size: The size of the square avatar image in pixels.
                It defaults to 128 pixels, and is available in sizes
                from 6 to 512 pixels.
            image_format: The desired format of the returned image. It defaults
                to “png”, but can also be specified as “svg”.
            font_size: The size of the font as a percent of the image_size.
                It defaults to 0.7, but it can be set between 0.1 and 1.0.
            char_limit: The maximum number of characters displayed in
                the avatar. It defaults to 2. The actual number of characters
                displayed can be less than this number, but it cannot be more.
                The characters will first be chosen from distinct words, then
                from the second letter of distinct words.
            background_color: The hex color for the background.
                It defaults to #335eea.
            font_color: The hex color for the font.
                It defaults to white, i.e.,ffffff.
            is_rounded: Create a rounded avatar picture instead of squared one.
                It defaults to false.
            is_uppercase: Set the initials in the avatar to all capitals.
                It defaults to true.
            is_italic: Set the initials in the avatar to all italics.
                It defaults to false.
            is_bold: Set the initials in the avatar to bold.
                It defaults to false.

        Returns:
            AvatarsResponse representing API call response.
        """
        self._validate_params(**locals())
        return self._service_request(
            _response_class=AvatarsResponse,
            name=name,
            image_size=image_size,
            image_format=image_format,
            font_size=font_size,
            char_limit=char_limit,
            background_color=background_color,
            font_color=font_color,
            is_rounded=is_rounded,
            is_uppercase=is_uppercase,
            is_italic=is_italic,
            is_bold=is_bold
        )
