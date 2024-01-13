from abc import ABC, abstractmethod
from typing import Union


class BaseStrategy(ABC):
    """Base class for all image processing strategies."""

    @abstractmethod
    def __init__(self) -> None:
        """This is to prevent direct instantiation of this base class."""

    def json(self) -> dict[str, Union[int, str]]:
        """Returns a dict with strategy attributes to be used with requests."""
        return {
            "strategy": self.__class__.__name__.lower()
        }
