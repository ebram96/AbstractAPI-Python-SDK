import pytest

from abstract_api.image_processing.strategies import Fill


class TestFill:
    @pytest.fixture
    def kwargs(self):
        return {
            "background": "rgb(91, 126, 156)",
            "height": 250,
            "width": 300
        }

    def test_initialization(self, kwargs):
        # When
        instance = Fill(**kwargs)

        # Then
        for k in kwargs:
            assert getattr(instance, k) == kwargs[k]

    def test_json(self, kwargs):
        # Given
        instance = Fill(**kwargs)

        # When
        json = instance.json()

        # Then
        assert json == {
            'strategy': 'fill',
            'width': kwargs['width'],
            'height': kwargs['height'],
            'background': kwargs['background']
        }
