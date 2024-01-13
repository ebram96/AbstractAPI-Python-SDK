from functools import cached_property
from typing import Optional

import requests

from ._multiple_exchange_rates_response import MultipleExchangeRatesResponse
from ._response_fields import HISTORICAL_RESPONSE_FIELDS


class HistoricalExchangeRatesResponse(MultipleExchangeRatesResponse):
    """Historical exchange rates service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new HistoricalExchangeRatesResponse."""
        super().__init__(response, HISTORICAL_RESPONSE_FIELDS)

    @cached_property
    def date(self) -> Optional[str]:
        """The date the currencies were pulled from.

        This is per successful request.
        """
        return self._get_response_field("date")
