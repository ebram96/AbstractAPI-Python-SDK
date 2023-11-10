from ._mixins import HeightMixin, WidthMixin
from .base_strategy import BaseStrategy


class Exact(HeightMixin, WidthMixin, BaseStrategy):
    """Resize to exact width and height.

    Aspect ratio will not be maintained.
    """
