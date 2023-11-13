from functools import cached_property

import requests

from ..core.bases import JSONResponse
from .response_fields import CONVERSION_RESPONSE_FIELDS


class ExchangeRatesConversionResponse(JSONResponse):
    """Exchange rate conversion service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new ExchangeRateConversionResponse."""
        super().__init__(response, CONVERSION_RESPONSE_FIELDS)

    @cached_property
    def base(self) -> str | None:
        """The base currency used to get the exchange rates."""
        return self._get_response_field("base")

    @cached_property
    def target(self) -> str | None:
        """The target currency that the base_amount was converted into."""
        return self._get_response_field("target")

    @cached_property
    def date(self) -> str | None:
        """The date the currencies were pulled from.

        This is per successful request.
        """
        return self._get_response_field("date")

    @cached_property
    def base_amount(self) -> float | None:
        """The amount of the base currency from the request."""
        return self._get_response_field("base_amount")

    @cached_property
    def converted_amount(self) -> float | None:
        """The amount after conversion.

        The amount of the target currency that the base_amount has been
        converted into.
        """
        return self._get_response_field("converted_amount")

    @cached_property
    def exchange_rate(self) -> float | None:
        """The exchange rate used in conversion."""
        return self._get_response_field("exchange_rate")

    @cached_property
    def last_updated(self) -> int | None:
        """The Unix timestamp of when the returned data was last updated."""
        return self._get_response_field("last_updated")
