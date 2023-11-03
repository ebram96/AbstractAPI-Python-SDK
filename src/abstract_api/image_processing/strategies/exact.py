from .base_strategy import BaseStrategy


class Exact(BaseStrategy):
    """Resize to exact width and height.

    Aspect ratio will not be maintained.
    """
    def __init__(self, width: int, height: int) -> None:
        """Initializes a new Exact instance."""
        self._width = width
        self._height = height

    def json(self) -> dict[str, int | str]:
        """Returns a dict with strategy attributes to be used with requests."""
        return super().json() | {
            "width": self.width,
            "height": self.height
        }

    @property
    def width(self):
        """Width to resize the image to."""
        return self._width

    @property
    def height(self):
        """Height to resize the image to."""
        return self._height
