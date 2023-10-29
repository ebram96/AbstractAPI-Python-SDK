import requests

from ._multiple_exchange_rates_response import MultipleExchangeRatesResponse
from .response_fields import LIVE_RESPONSE_FIELDS


class LiveExchangeRatesResponse(MultipleExchangeRatesResponse):
    """Live exchange rates service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new LiveExchangeRatesResponse."""
        super().__init__(response, LIVE_RESPONSE_FIELDS)

    @property
    def last_updated(self) -> int | None:
        """The Unix timestamp of when the returned data was last updated."""
        return self._get_response_field("last_updated")
