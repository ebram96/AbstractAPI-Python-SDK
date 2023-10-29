from typing import TYPE_CHECKING

import requests

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

    def __init__(
        self,
        response: requests.models.Response,
        response_fields: frozenset[str]
    ) -> None:
        """Initializes a new MultipleExchangeRatesResponse."""
        super().__init__(response)
        self._response_fields = response_fields
        not_in_response = object()
        for field in response_fields:
            if TYPE_CHECKING:
                assert isinstance(self.meta.body_json, dict)
            value = self.meta.body_json.get(field, not_in_response)
            # Set property only if field was returned
            if value is not not_in_response:
                # TODO: Move to parent class
                if field == "exchange_rates":
                    exchange_rates = []
                    for currency, rate in value.items():
                        exchange_rates.append(
                            ExchangeRate(currency=currency, rate=rate)
                        )
                    value = frozenset(exchange_rates)
                setattr(self, f"_{field}", value)

    @property
    def base(self) -> str | None:
        """The base currency used to get the exchange rates."""
        return self._get_response_field("base")

    @property
    def exchange_rates(self) -> frozenset[ExchangeRate] | None:
        """Target currencies exchange rates versus the base currency."""
        return self._get_response_field("exchange_rates")
