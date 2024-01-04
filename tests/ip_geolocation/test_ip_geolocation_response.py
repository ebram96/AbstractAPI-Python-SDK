from abstract_api.ip_geolocation import IPGeolocationResponse
from abstract_api.ip_geolocation._response_fields import RESPONSE_FIELDS
from tests.common_assertions import (
    assert_response_fields,
    assert_unchangeable_fields
)
from tests.utils import generate_response


class TestIPGeolocationResponse:
    def test_instance(self, ip_geolocation_sample, mocker):
        # Given
        response = generate_response(ip_geolocation_sample)

        # When
        instance = IPGeolocationResponse(response, RESPONSE_FIELDS)
        mocked__get_response_field = mocker.patch.object(
            instance,
            "_get_response_field",
            wraps=instance._get_response_field
        )

        # Then
        assert_response_fields(
            instance,
            RESPONSE_FIELDS,
            ip_geolocation_sample,
            mocker,
            ignore=IPGeolocationResponse._nested_entities
        )
        for field, cls in IPGeolocationResponse._nested_entities.items():
            assert isinstance(getattr(instance, field), cls)
            mocked__get_response_field.assert_called_with(field)
        assert_unchangeable_fields(
            instance,
            IPGeolocationResponse._nested_entities.keys()
        )
        assert mocked__get_response_field.call_count == len(RESPONSE_FIELDS)
