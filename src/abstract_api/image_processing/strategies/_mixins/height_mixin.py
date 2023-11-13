from functools import cache
from typing import TYPE_CHECKING

from ._json_representable_protocol import JSONRepresentableProtocol

if TYPE_CHECKING:
    _Base = JSONRepresentableProtocol
else:
    _Base = object


class HeightMixin(_Base):
    """Height mixin."""
    def __init__(self, *, height: int, **kwargs) -> None:
        """Initializes a new instance."""
        super().__init__(**kwargs)
        self._height = height

    @cache
    def json(self) -> dict[str, int | str]:
        """Returns a dict with strategy attributes to be used with requests."""
        return super().json() | {  # type: ignore[safe-super]
            "height": self.height
        }

    @property
    def height(self) -> int:
        """Height to resize the image to."""
        return self._height
