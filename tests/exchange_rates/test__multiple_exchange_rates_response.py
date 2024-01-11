from abstract_api.exchange_rates._multiple_exchange_rates_response import (
    ExchangeRate,
    MultipleExchangeRatesResponse
)
from tests.utils import generate_response


class TestMultipleExchangeRatesResponse:
    def test__init_response_field(
        self, exchange_rates_historical_sample
    ):
        # Given
        response = generate_response(exchange_rates_historical_sample)
        instance = MultipleExchangeRatesResponse(
            response, response_fields=frozenset(["base", "exchange_rates"])
        )
        exchange_rates = exchange_rates_historical_sample["exchange_rates"]

        # When
        instance._init_response_field("exchange_rates", exchange_rates)

        # Then
        assert instance.base == exchange_rates_historical_sample["base"]
        assert isinstance(instance.exchange_rates, tuple)
        assert len(instance.exchange_rates) == len(exchange_rates)
        for er in instance.exchange_rates:
            assert isinstance(er, ExchangeRate)
