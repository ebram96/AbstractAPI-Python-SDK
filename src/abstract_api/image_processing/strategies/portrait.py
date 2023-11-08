from ._mixins import HeightMixin
from .base_strategy import BaseStrategy


class Portrait(HeightMixin, BaseStrategy):
    """Resize to exact height.

    Width will be adjusted according to aspect ratio.
    """
