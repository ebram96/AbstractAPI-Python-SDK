from abstract_api.email_validation import EmailValidationResponse
from abstract_api.email_validation._response_fields import RESPONSE_FIELDS
from tests.common_assertions import assert_unchangeable_fields
from tests.utils import generate_response


class TestEmailValidationResponse:
    def test_instance(self, email_validation_sample, mocker):
        response = generate_response(email_validation_sample)

        instance = EmailValidationResponse(response)

        mocked__get_response_field = mocker.patch.object(
            instance,
            "_get_response_field",
            wraps=instance._get_response_field
        )
        for field in RESPONSE_FIELDS:
            if field in EmailValidationResponse._complex_bool_fields:
                assert getattr(instance, field) == email_validation_sample[field]["value"]
            else:
                assert getattr(instance, field) == email_validation_sample[field]
            mocked__get_response_field.assert_called_with(field)
        assert mocked__get_response_field.call_count == len(RESPONSE_FIELDS)
        assert_unchangeable_fields(instance, RESPONSE_FIELDS)
