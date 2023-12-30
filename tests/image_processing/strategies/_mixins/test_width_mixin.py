from abstract_api.image_processing.strategies import BaseStrategy
from abstract_api.image_processing.strategies._mixins import WidthMixin


class ConcreteExample(WidthMixin, BaseStrategy):
    pass


class TestWidthMixin:
    def test_initialization(self):
        # Given
        width = 100

        # When
        instance = WidthMixin(width=width)

        # Then
        assert instance.width == width

    def test_json(self):
        # Given
        width = 100
        instance = ConcreteExample(width=width)

        # When
        json = instance.json()

        # Then
        assert json == {
            "strategy": ConcreteExample.__name__.lower(),
            "width": width
        }
