from abstract_api.iban_validation import IBANValidationResponse
from abstract_api.iban_validation._response_fields import RESPONSE_FIELDS
from tests.common_assertions import assert_response_fields
from tests.utils import generate_response


class TestIBANValidationResponse:
    def test_instance(self, iban_validation_sample, mocker):
        response = generate_response(iban_validation_sample)

        instance = IBANValidationResponse(response)

        assert_response_fields(
            instance, RESPONSE_FIELDS, iban_validation_sample, mocker
        )
