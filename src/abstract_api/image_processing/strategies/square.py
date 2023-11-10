from .base_strategy import BaseStrategy


class Square(BaseStrategy):
    """Crop image by its shorter dimension to make it a square.

    Image is resized after cropping to the specified size.
    """

    def __init__(self, size: int) -> None:
        """Initialize a new Square instance."""
        self._size = size

    def json(self) -> dict[str, int | str]:
        """Returns a dict with strategy attributes to be used with requests."""
        return super().json() | {"size": self.size}

    @property
    def size(self) -> int:
        """Size to resize the cropped image to."""
        return self._size
