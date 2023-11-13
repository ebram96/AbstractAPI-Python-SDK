from functools import cached_property
from typing import Any

from ..core.bases import JSONResponse


class ExchangeRate:
    """Exchange rate entity in response."""

    def __init__(self, currency: str, rate: float) -> None:
        """Initializes a new ExchangeRate."""
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
        """Sets a response field's value during instance initialization.

        This should be used in/as a part of __init__ method.

        Args:
            field: Field name.
            value: Value to be set. The value is parsed to a nested entity
                if the field is a nested entity.
        """
        if field == "exchange_rates":
            exchange_rates = []
            for currency, rate in value.items():
                exchange_rates.append(
                    ExchangeRate(currency=currency, rate=rate)
                )
            value = tuple(exchange_rates)
        super()._init_response_field(field, value)

    @cached_property
    def base(self) -> str | None:
        """The base currency used to get the exchange rates."""
        return self._get_response_field("base")

    @cached_property
    def exchange_rates(self) -> tuple[ExchangeRate] | None:
        """Target currencies exchange rates versus the base currency."""
        return self._get_response_field("exchange_rates")
