from typing import TYPE_CHECKING

import requests

from abstract_api.bases import JSONResponse

from .response_fields import LIVE_RESPONSE_FIELDS


class ExchangeRate:
    """Exchange rate entity in live exchange rates response."""

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


class LiveExchangeRatesResponse(JSONResponse):
    """Live exchange rates service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new LiveExchangeRatesResponse."""
        super().__init__(response)
        self._response_fields = LIVE_RESPONSE_FIELDS
        not_in_response = object()
        for field in LIVE_RESPONSE_FIELDS:
            if TYPE_CHECKING:
                assert isinstance(self.meta.body_json, dict)
            value = self.meta.body_json.get(field, not_in_response)
            # Set property only if field was returned
            if value is not not_in_response:
                # TODO: Move to parent class
                if field == "exchange_rates":
                    print(value)
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
    def last_updated(self) -> int | None:
        """The Unix timestamp of when the returned data was last updated."""
        return self._get_response_field("last_updated")

    @property
    def exchange_rates(self) -> frozenset[ExchangeRate] | None:
        """Target currencies exchange rates versus the base currency."""
        return self._get_response_field("exchange_rates")
