from ._mixins import HeightMixin, WidthMixin
from .base_strategy import BaseStrategy


class Auto(HeightMixin, WidthMixin, BaseStrategy):
    """Use auto selected strategy.

    The best strategy (portrait or landscape) will be selected according to its
    aspect ratio.
    """
