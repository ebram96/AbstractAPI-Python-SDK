from abstract_api.image_processing.strategies import BaseStrategy
from abstract_api.image_processing.strategies._mixins import HeightMixin


class ConcreteExample(HeightMixin, BaseStrategy):
    pass


class TestHeightMixin:
    def test_initialization(self):
        # Given
        height = 100

        # When
        instance = HeightMixin(height=height)

        # Then
        assert instance.height == height

    def test_json(self):
        # Given
        height = 100
        instance = ConcreteExample(height=height)

        # When
        json = instance.json()

        # Then
        assert json == {
            "strategy": ConcreteExample.__name__.lower(),
            "height": height
        }
