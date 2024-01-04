from functools import cache

from .base_strategy import BaseStrategy


class Square(BaseStrategy):
    """Crop image by its shorter dimension to make it a square.

    Image is resized after cropping to the specified size.
    """

    def __init__(self, size: int) -> None:
        """Initializes a new Square instance."""
        super().__init__()
        self._size = size

    @cache
    def json(self) -> dict[str, int | str]:
        """Returns a dict with strategy attributes to be used with requests."""
        return super().json() | {"size": self.size}

    @property
    def size(self) -> int:
        """Size to resize the cropped image to."""
        return self._size
