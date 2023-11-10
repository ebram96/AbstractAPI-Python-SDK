from enum import Enum

from ._mixins import HeightMixin, WidthMixin
from .base_strategy import BaseStrategy


class CropMode(Enum):
    """Direction of cropping."""
    NORTH = "n"
    TOP = "t"
    NORTH_WEST = "nw"
    TOP_LEFT = "tl"
    NORTH_EAST = "ne"
    TOP_RIGHT = "tr"
    WEST = "w"
    LEFT = "l"
    CENTER = "c"
    EAST = "e"
    RIGHT = "r"
    SOUTH_EAST = "se"
    BOTTOM_RIGHT = "br"
    SOUTH_WEST = "sw"
    BOTTOM_LEFT = "bl"
    SOUTH = "s"
    BOTTOM = "b"


class Crop(HeightMixin, WidthMixin, BaseStrategy):
    """Crop an image to a specified exact size.

    The resulting cropped image can optionally be scaled by inclusion of a
    scale, which accepts a number representing the percentage by which the
    image should be scaled.

    If you want to crop from a direction other than the default “center”, you
    can specify a crop_mode parameter, which can take one of the following
    gravity (or direction) values:
    n or t    - North / Top
    nw or tl  - North West / Top Left
    ne or tr  - North East / Top Right
    w or l    - West / Left
    c         - Center - this is the default gravity or direction, and applied
                when the crop_mode parameter is left out, or an invalid value
                is passed.
    e or r    - East / Right
    se or br  - South East / Bottom Right
    sw or bl  - South West / Bottom Left
    s or b    - South / Bottom

    You can also use CropMode enum to pass the crop_mode parameter.

    If you would like to crop a custom area from an image, you can do so by
    specifying the rectangular region you wish to extract as x, y, width and
    height. Optionally, you can pass a scale parameter (as mentioned above),
    which must be a number representing the percentage by which you would like
    to scale the image.
    """

    def __init__(
        self,
        scale: int,
        x: int | None = None,
        y: int | None = None,
        crop_mode: CropMode | str | None = None,
        *args,
        **kwargs
    ) -> None:
        """Initializes a new Crop instance."""
        super().__init__(*args, **kwargs)
        self._scale = scale
        self._x = x
        self._y = y

        if crop_mode is not None:
            if isinstance(crop_mode, str):
                if crop_mode not in CropMode:
                    raise ValueError(
                        f"'{crop_mode}' is not a valid crop mode"
                    )
                crop_mode = CropMode(crop_mode)

        self._crop_mode = crop_mode

    def json(self) -> dict[str, int | str]:
        """Returns a dict with strategy attributes to be used with requests."""
        json = super().json()
        json["scale"] = self.scale
        optionals = ["x", "y", "crop_mode"]
        for attr in optionals:
            if getattr(self, attr) is not None:
                if attr == "crop_mode":
                    # TODO: Not clean but no worries, it'll be moved to a mixin
                    assert self.crop_mode is not None
                    json[attr] = self.crop_mode.value
                else:
                    json[attr] = getattr(self, attr)
        return json

    @property
    def scale(self) -> int:
        """The percentage by which you would like to scale the image."""
        return self._scale

    @property
    def x(self) -> int | None:
        """X dimension of the rectangular area to be cropped, if needed."""
        return self._x

    @property
    def y(self) -> int | None:
        """Y dimension of the rectangular area to be cropped, if needed."""
        return self._y

    @property
    def crop_mode(self) -> CropMode | None:
        """Direction of cropping."""
        return self._crop_mode
