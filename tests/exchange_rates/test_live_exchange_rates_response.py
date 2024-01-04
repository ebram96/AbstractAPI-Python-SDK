from abstract_api.exchange_rates import LiveExchangeRatesResponse
from abstract_api.exchange_rates._multiple_exchange_rates_response import (
    MultipleExchangeRatesResponse
)
from abstract_api.exchange_rates._response_fields import LIVE_RESPONSE_FIELDS
from tests.common_assertions import assert_response_fields
from tests.utils import generate_response


class TestLiveExchangeRatesResponse:
    def test_initialization(self, blank_response, mocker):
        # Given
        mocked_init = mocker.patch.object(
            MultipleExchangeRatesResponse,
            "__init__",
            wraps=MultipleExchangeRatesResponse.__init__
        )
        mocked_init.return_value = None

        # When
        LiveExchangeRatesResponse(blank_response)

        # Then
        mocked_init.assert_called_once_with(
            blank_response, LIVE_RESPONSE_FIELDS
        )

    def test_instance(self, exchange_rates_live_sample, mocker):
        # Given
        sample = exchange_rates_live_sample
        response = generate_response(sample)

        # When
        instance = LiveExchangeRatesResponse(response)

        # Then
        assert_response_fields(
            instance,
            LIVE_RESPONSE_FIELDS,
            sample,
            mocker,
            ignore=["exchange_rates"]
        )
