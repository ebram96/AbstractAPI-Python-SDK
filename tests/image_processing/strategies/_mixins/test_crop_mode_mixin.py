import pytest

from abstract_api.image_processing.strategies import BaseStrategy
from abstract_api.image_processing.strategies._mixins import CropModeMixin
from abstract_api.image_processing.strategies._mixins.crop_mode_mixin import (
    CropMode
)


class ConcreteExample(CropModeMixin, BaseStrategy):
    pass


class TestCropModeMixin:
    def test_initialization(self):
        # Given
        mode = "r"

        # When
        instance = CropModeMixin(crop_mode=mode)

        # Then
        assert instance.crop_mode == CropMode(mode)

    @pytest.mark.parametrize(
        # Given
        "mode",
        ["r ", "nx"]
    )
    def test_initialization_with_wrong_crop_mode(self, mode):
        # Then
        with pytest.raises(ValueError):
            # When
            CropModeMixin(crop_mode=mode)

    def test_json(self):
        # Given
        mode = CropMode("n")
        instance = ConcreteExample(crop_mode=mode)

        # When
        json = instance.json()

        # Then
        assert json == {
            "strategy": ConcreteExample.__name__.lower(),
            "crop_mode": "n"
        }
