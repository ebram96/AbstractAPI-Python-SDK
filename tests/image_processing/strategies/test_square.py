import pytest

from abstract_api.image_processing.strategies import Square


class TestSquare:
    @pytest.fixture
    def kwargs(self):
        return {"size": 500}

    def test_initialization(self, kwargs):
        # When
        instance = Square(**kwargs)

        # Then
        assert instance.size == kwargs["size"]

    def test_json(self, kwargs):
        # Given
        instance = Square(**kwargs)

        # When
        json = instance.json()

        # Then
        assert json == {
            'strategy': 'square',
            'size': kwargs["size"]
        }
