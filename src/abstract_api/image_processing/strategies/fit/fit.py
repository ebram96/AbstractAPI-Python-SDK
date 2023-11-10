from .._mixins import CropModeMixin, HeightMixin, WidthMixin
from ..base_strategy import BaseStrategy


class Fit(HeightMixin, WidthMixin, CropModeMixin, BaseStrategy):
    """Crop and resize the image to fit the desired width and height."""
