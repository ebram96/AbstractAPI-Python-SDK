import pytest

from abstract_api.image_processing.strategies import Crop


class TestCrop:
    @pytest.fixture
    def kwargs(self):
        return {
            "scale": 50,
            "x": 100,
            "y": 200,
            "height": 250,
            "width": 300
        }

    def test_initialization(self, kwargs):
        # When
        instance = Crop(**kwargs)

        # Then
        for k in kwargs:
            assert getattr(instance, k) == kwargs[k]

    def test_json(self, kwargs):
        # Given
        instance = Crop(**kwargs)

        # When
        json = instance.json()

        # Then
        assert json == {
            'strategy': 'crop',
            'width': kwargs['width'],
            'height': kwargs['height'],
            'x': kwargs['x'],
            'y': kwargs['y'],
            'scale': kwargs['scale']
        }
