from abstract_api.exchange_rates import HistoricalExchangeRatesResponse
from abstract_api.exchange_rates._multiple_exchange_rates_response import (
    MultipleExchangeRatesResponse
)
from abstract_api.exchange_rates._response_fields import (
    HISTORICAL_RESPONSE_FIELDS
)
from tests.common_assertions import assert_response_fields
from tests.utils import generate_response


class TestHistoricalExchangeRatesResponse:
    def test_initialization(self, blank_response, mocker):
        # Given
        mocked_init = mocker.patch.object(
            MultipleExchangeRatesResponse,
            "__init__",
            wraps=MultipleExchangeRatesResponse.__init__
        )
        mocked_init.return_value = None

        # When
        HistoricalExchangeRatesResponse(blank_response)

        # Then
        mocked_init.assert_called_once_with(
            blank_response, HISTORICAL_RESPONSE_FIELDS
        )

    def test_instance(self, exchange_rates_historical_sample, mocker):
        # Given
        sample = exchange_rates_historical_sample
        response = generate_response(sample)

        # When
        instance = HistoricalExchangeRatesResponse(response)

        # Then
        assert_response_fields(
            instance,
            HISTORICAL_RESPONSE_FIELDS,
            sample,
            mocker,
            ignore=["exchange_rates"]
        )
