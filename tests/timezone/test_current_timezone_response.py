from abstract_api.timezone import CurrentTimezoneResponse
from abstract_api.timezone.response_fields import CURRENT_RESPONSE_FIELDS
from tests.common_assertions import assert_response_fields
from tests.utils import generate_response


class TestCurrentTimezoneResponse:
    def test_instance(self, current_timezone_sample, mocker):
        # Given
        response = generate_response(current_timezone_sample)

        # When
        instance = CurrentTimezoneResponse(response)

        # Then
        assert_response_fields(
            instance, CURRENT_RESPONSE_FIELDS, current_timezone_sample, mocker
        )
