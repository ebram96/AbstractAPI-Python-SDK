from abstract_api.iban_validation import IBANValidationResponse
from abstract_api.iban_validation._response_fields import RESPONSE_FIELDS
from tests.common_assertions import assert_response_fields
from tests.utils import generate_response


class TestIBANValidationResponse:
    def test_instance(self, iban_validation_sample, mocker):
        # Given
        response = generate_response(iban_validation_sample)

        # When
        instance = IBANValidationResponse(response)

        # Then
        assert_response_fields(
            instance, RESPONSE_FIELDS, iban_validation_sample, mocker
        )
