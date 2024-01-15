from enum import Enum
from typing import TYPE_CHECKING, Optional, Union

from ._json_representable_protocol import JSONRepresentableProtocol

if TYPE_CHECKING:
    _Base = JSONRepresentableProtocol
else:
    _Base = object


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


class CropModeMixin(_Base):
    """Crop mode mixin."""

    def __init__(
        self,
        *,
        crop_mode: Optional[Union[CropMode, str]] = None,
        **kwargs
    ) -> None:
        """Initializes a new instance."""
        super().__init__(**kwargs)

        if crop_mode is not None:
            if isinstance(crop_mode, str):
                crop_mode = crop_mode.lower()
                if crop_mode not in [m.value for m in CropMode]:
                    raise ValueError(
                        f"'{crop_mode}' is not a valid crop mode"
                    )
                crop_mode = CropMode(crop_mode)

        self._crop_mode = crop_mode

    def json(self) -> dict[str, Union[int, str]]:
        """Returns a dict with strategy attributes to be used with requests."""
        json = super().json()  # type: ignore[safe-super]
        if self.crop_mode is not None:
            json["crop_mode"] = self.crop_mode.value
        return json

    @property
    def crop_mode(self) -> Optional[CropMode]:
        """Direction of cropping."""
        return self._crop_mode
