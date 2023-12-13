import pytest

from abstract_api.core.bases import JSONResponse
from abstract_api.exchange_rates import ExchangeRatesConversionResponse
from abstract_api.exchange_rates.response_fields import (
    CONVERSION_RESPONSE_FIELDS
)
from tests.common_assertions import assert_response_fields
from tests.utils import generate_response


class TestExchangeRatesConversionResponse:
    @pytest.mark.parametrize(
        "ignorable_field", ["date", "last_updated"]
    )
    def test_initialization(self, ignorable_field, blank_response, mocker):
        # Given
        mocked_init = mocker.patch.object(
            JSONResponse,
            "__init__",
            wraps=JSONResponse.__init__
        )
        mocked_init.return_value = None

        # When
        ExchangeRatesConversionResponse(blank_response, ignorable_field == "last_updated")

        # Then
        mocked_init.assert_called_once_with(
            blank_response,
            CONVERSION_RESPONSE_FIELDS - {
                "last_updated"
                if ignorable_field == "last_updated"
                else "date"
            }
        )

    @pytest.mark.parametrize(
        "ignorable_field", ["date", "last_updated"]
    )
    def test_instance(
        self,
        ignorable_field,
        exchange_rates_conversion_sample,
        mocker
    ):
        # Given
        sample = exchange_rates_conversion_sample
        if ignorable_field == "last_updated":
            sample["date"] = "2023-12-13"
        response = generate_response(sample)

        # When
        instance = ExchangeRatesConversionResponse(response, ignorable_field != "date")

        # Then
        assert_response_fields(
            instance,
            CONVERSION_RESPONSE_FIELDS,
            sample,
            mocker,
            ignore=[ignorable_field]
        )
        with pytest.raises(AttributeError):
            getattr(instance, ignorable_field)
