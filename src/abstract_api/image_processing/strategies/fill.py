from functools import cache
from typing import Optional, Union

from ._mixins import HeightMixin, WidthMixin
from .base_strategy import BaseStrategy


class Fill(HeightMixin, WidthMixin, BaseStrategy):
    """Resize image to fit the specified bounds while preserving aspect ratio.

    The optional background parameter allows you to specify a color which will
    be used to fill the unused portions of the specified bounds.
    The default background color is black.
    """

    def __init__(self, background: Optional[str] = None, **kwargs) -> None:
        """Initializes a new Square instance."""
        super().__init__(**kwargs)
        self._background = background

    @cache
    def json(self) -> dict[str, Union[int, str]]:
        """Returns a dict with strategy attributes to be used with requests."""
        json = super().json()
        if self.background is not None:
            json["background"] = self.background
        return json

    @property
    def background(self) -> Optional[str]:
        """The color to be used to fill the unused portions."""
        return self._background
