import requests

from ._multiple_exchange_rates_response import MultipleExchangeRatesResponse
from .response_fields import LIVE_RESPONSE_FIELDS


class HistoricalExchangeRatesResponse(MultipleExchangeRatesResponse):
    """Historical exchange rates service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new HistoricalExchangeRatesResponse."""
        super().__init__(response, LIVE_RESPONSE_FIELDS)

    @property
    def date(self) -> str | None:
        """The date the currencies were pulled from.

        This is per successful request.
        """
        return self._get_response_field("date")
