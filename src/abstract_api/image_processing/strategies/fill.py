from ._mixins import HeightMixin, WidthMixin
from .base_strategy import BaseStrategy


class Fill(HeightMixin, WidthMixin, BaseStrategy):
    """Resize image to fit the specified bounds while preserving aspect ratio.

    The optional background parameter allows you to specify a color which will
    be used to fill the unused portions of the specified bounds.
    The default background color is black.
    """

    def __init__(
        self,
        background: str | None = None,
        *args,
        **kwargs
    ) -> None:
        """Initialize a new Square instance."""
        super().__init__(*args, **kwargs)
        self._background = background

    def json(self) -> dict[str, int | str]:
        """Returns a dict with strategy attributes to be used with requests."""
        json = super().json()
        if self.background is not None:
            json["background"] = self.background
        return json

    @property
    def background(self) -> str | None:
        """The color to be used to fill the unused portions."""
        return self._background