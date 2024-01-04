from abstract_api.vat import VATValidationResponse
from abstract_api.vat._response_fields import VALIDATION_RESPONSE_FIELDS
from tests.common_assertions import (
    assert_response_fields,
    assert_unchangeable_fields
)
from tests.utils import generate_response


class TestVATValidationResponse:
    def test_instance(self, vat_validation_sample, mocker):
        # Given
        response = generate_response(vat_validation_sample)

        # When
        instance = VATValidationResponse(response)

        # Then
        assert_response_fields(
            instance,
            VALIDATION_RESPONSE_FIELDS,
            vat_validation_sample,
            mocker,
            ignore=VATValidationResponse._nested_entities
        )
        mocked__get_response_field = mocker.patch.object(
            instance,
            "_get_response_field",
            wraps=instance._get_response_field
        )
        for field, cls in VATValidationResponse._nested_entities.items():
            assert isinstance(getattr(instance, field), cls)
            mocked__get_response_field.assert_called_with(field)
        assert_unchangeable_fields(
            instance,
            VATValidationResponse._nested_entities.keys()
        )
