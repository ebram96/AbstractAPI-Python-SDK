from abstract_api.core.common_entities import Country
from tests.common_assertions import assert_unchangeable_fields


class TestCountry:
    def test_initialization(self):
        # Given
        data = {"name": "Egypt", "code": "EG"}

        # When
        instance = Country(**data)

        # Then
        assert_unchangeable_fields(instance, data.keys())
