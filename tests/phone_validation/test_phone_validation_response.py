from abstract_api.phone_validation import PhoneValidationResponse
from abstract_api.phone_validation.response_fields import RESPONSE_FIELDS
from tests.common_assertions import (
    assert_response_fields,
    assert_unchangeable_fields
)
from tests.utils import generate_response


class TestPhoneValidationResponse:
    def test_instance(self, phone_validation_sample, mocker):
        # Given
        response = generate_response(phone_validation_sample)

        # When
        instance = PhoneValidationResponse(response)

        # Then
        assert_response_fields(
            instance,
            RESPONSE_FIELDS,
            phone_validation_sample,
            mocker,
            ignore=PhoneValidationResponse._nested_entities
        )
        mocked__get_response_field = mocker.patch.object(
            instance,
            "_get_response_field",
            wraps=instance._get_response_field
        )
        for field, cls in PhoneValidationResponse._nested_entities.items():
            assert isinstance(getattr(instance, field), cls)
            mocked__get_response_field.assert_called_with(field)
        assert_unchangeable_fields(
            instance,
            PhoneValidationResponse._nested_entities.keys()
        )
