from typing import Any

from abstract_api.bases import JSONResponse


class ExchangeRate:
    """Exchange rate entity in live/historical exchange rates response."""

    def __init__(self, currency: str, rate: float) -> None:
        """Initializes a new Country."""
        self._currency = currency
        self._rate = rate

    @property
    def currency(self) -> str:
        """Target currency."""
        return self._currency

    @property
    def rate(self) -> float:
        """Exchange rate versus the base currency."""
        return self._rate


class MultipleExchangeRatesResponse(JSONResponse):
    """Base response for services that return multiple exchange rates."""

    def _init_response_field(self, field: str, value: Any) -> None:
        """TODO."""
        if field == "exchange_rates":
            exchange_rates = []
            for currency, rate in value.items():
                exchange_rates.append(
                    ExchangeRate(currency=currency, rate=rate)
                )
            value = frozenset(exchange_rates)
        super()._init_response_field(field, value)

    @property
    def base(self) -> str | None:
        """The base currency used to get the exchange rates."""
        return self._get_response_field("base")

    @property
    def exchange_rates(self) -> frozenset[ExchangeRate] | None:
        """Target currencies exchange rates versus the base currency."""
        return self._get_response_field("exchange_rates")
