from ._mixins import HeightMixin, WidthMixin
from .base_strategy import BaseStrategy


class Fit(HeightMixin, WidthMixin, BaseStrategy):
    """Crop and resize the image to fit the desired width and height."""
