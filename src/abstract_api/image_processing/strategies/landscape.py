from ._mixins import WidthMixin
from .base_strategy import BaseStrategy


class Landscape(WidthMixin, BaseStrategy):
    """Resize to exact width.

    Height will be adjusted according to aspect ratio.
    """
