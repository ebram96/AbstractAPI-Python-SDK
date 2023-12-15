from abstract_api.image_processing.strategies import BaseStrategy


class TestBaseStrategy:
    def test_json(self, mocker):
        # Given
        instance = mocker.Mock()

        # When
        json = BaseStrategy.json(self=instance)

        # Then
        assert json == {'strategy': mocker.Mock.__name__.lower()}
