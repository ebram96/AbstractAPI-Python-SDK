from functools import cached_property
from typing import Optional

import requests

from ..core.bases import JSONResponse
from ._response_fields import CONVERSION_RESPONSE_FIELDS


class ExchangeRatesConversionResponse(JSONResponse):
    """Exchange rate conversion service response."""

    def __init__(
        self,
        response: requests.models.Response,
        date_included_in_request: Optional[bool] = False
    ) -> None:
        """Initializes a new ExchangeRateConversionResponse."""
        super().__init__(
            response,
            CONVERSION_RESPONSE_FIELDS - {
                "last_updated"
                if date_included_in_request
                else "date"
            }
        )

    @cached_property
    def base(self) -> Optional[str]:
        """The base currency used to get the exchange rates."""
        return self._get_response_field("base")

    @cached_property
    def target(self) -> Optional[str]:
        """The target currency that the base_amount was converted into."""
        return self._get_response_field("target")

    @cached_property
    def date(self) -> Optional[str]:
        """The date the currencies were pulled from.

        This is per successful request and returned only when 'date' parameter
        is passed in request.
        This is mutually-exclusive with 'last_updated' in response.
        """
        return self._get_response_field("date")

    @cached_property
    def base_amount(self) -> Optional[float]:
        """The amount of the base currency from the request."""
        return self._get_response_field("base_amount")

    @cached_property
    def converted_amount(self) -> Optional[float]:
        """The amount after conversion.

        The amount of the target currency that the base_amount has been
        converted into.
        """
        return self._get_response_field("converted_amount")

    @cached_property
    def exchange_rate(self) -> Optional[float]:
        """The exchange rate used in conversion."""
        return self._get_response_field("exchange_rate")

    @cached_property
    def last_updated(self) -> Optional[int]:
        """The Unix timestamp of when the returned data was last updated.

        This is returned if 'date' parameter was not passed in request.
        This is mutually-exclusive with 'date' in response.
        """
        return self._get_response_field("last_updated")
