from typing import TYPE_CHECKING, Union

from ._json_representable_protocol import JSONRepresentableProtocol

if TYPE_CHECKING:
    _Base = JSONRepresentableProtocol
else:
    _Base = object


class WidthMixin(_Base):
    """Width mixin."""
    def __init__(self, *, width: int, **kwargs) -> None:
        """Initializes a new instance."""
        super().__init__(**kwargs)
        self._width = width

    def json(self) -> dict[str, Union[int, str]]:
        """Returns a dict with strategy attributes to be used with requests."""
        return super().json() | {  # type: ignore[safe-super]
            "width": self.width
        }

    @property
    def width(self) -> int:
        """Width to resize the image to."""
        return self._width
