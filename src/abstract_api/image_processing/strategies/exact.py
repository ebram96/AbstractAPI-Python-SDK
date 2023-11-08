from ._mixins import HeightMixin
from .base_strategy import BaseStrategy


class Exact(HeightMixin, BaseStrategy):
    """Resize to exact width and height.

    Aspect ratio will not be maintained.
    """
    def __init__(self, width: int, height: int) -> None:
        """Initializes a new Exact instance."""
        super().__init__(height=height)
        self._width = width

    def json(self) -> dict[str, int | str]:
        """Returns a dict with strategy attributes to be used with requests."""
        return super().json() | {"width": self.width}

    @property
    def width(self):
        """Width to resize the image to."""
        return self._width
