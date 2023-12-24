from abstract_api.timezone import TimezoneConversionResponse
from tests.common_assertions import assert_unchangeable_fields
from tests.utils import generate_response


class TestTimezoneConversionResponse:
    def test_instance(self, timezone_conversion_sample, mocker):
        # Given
        response = generate_response(timezone_conversion_sample)

        # When
        instance = TimezoneConversionResponse(response)

        # Then
        mocked__get_response_field = mocker.patch.object(
            instance,
            "_get_response_field",
            wraps=instance._get_response_field
        )
        for field, cls in TimezoneConversionResponse._nested_entities.items():
            assert isinstance(getattr(instance, field), cls)
            mocked__get_response_field.assert_called_with(field)
        assert_unchangeable_fields(
            instance,
            TimezoneConversionResponse._nested_entities.keys()
        )
