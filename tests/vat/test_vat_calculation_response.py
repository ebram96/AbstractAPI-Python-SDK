from abstract_api.vat import VATCalculationResponse
from abstract_api.vat.response_fields import CALCULATION_RESPONSE_FIELDS
from tests.common_assertions import (
    assert_response_fields,
    assert_unchangeable_fields
)
from tests.utils import generate_response


class TestVATCalculationResponse:
    def test_instance(self, vat_calculation_sample, mocker):
        # Given
        response = generate_response(vat_calculation_sample)

        # When
        instance = VATCalculationResponse(response)

        # Then
        assert_response_fields(
            instance,
            CALCULATION_RESPONSE_FIELDS,
            vat_calculation_sample,
            mocker,
            ignore=VATCalculationResponse._nested_entities
        )
        mocked__get_response_field = mocker.patch.object(
            instance,
            "_get_response_field",
            wraps=instance._get_response_field
        )
        for field, cls in VATCalculationResponse._nested_entities.items():
            assert isinstance(getattr(instance, field), cls)
            mocked__get_response_field.assert_called_with(field)
        assert_unchangeable_fields(
            instance,
            VATCalculationResponse._nested_entities.keys()
        )
