from typing import TYPE_CHECKING

import requests

from abstract_api.bases import JSONResponse

from .response_fields import CONVERSION_RESPONSE_FIELDS


class ExchangeRatesConversionResponse(JSONResponse):
    """Exchange rate conversion service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new ExchangeRateConversionResponse."""
        super().__init__(response)
        self._response_fields = CONVERSION_RESPONSE_FIELDS
        not_in_response = object()
        for field in CONVERSION_RESPONSE_FIELDS:
            if TYPE_CHECKING:
                assert isinstance(self.meta.body_json, dict)
            value = self.meta.body_json.get(field, not_in_response)
            # Set property only if field was returned
            if value is not not_in_response:
                # TODO: Move to parent class
                setattr(self, f"_{field}", value)

    @property
    def base(self) -> str | None:
        """The base currency used to get the exchange rates."""
        return self._get_response_field("base")

    @property
    def target(self) -> str | None:
        """The target currency that the base_amount was converted into."""
        return self._get_response_field("target")

    @property
    def date(self) -> str | None:
        """The date the currencies were pulled from.

        This is per successful request.
        """
        return self._get_response_field("date")

    @property
    def base_amount(self) -> str | None:
        """The amount of the base currency from the request."""
        return self._get_response_field("base_amount")

    @property
    def converted_amount(self) -> str | None:
        """The amount after conversion.

        The amount of the target currency that the base_amount has been
        converted into.
        """
        return self._get_response_field("converted_amount")

    @property
    def exchange_rate(self) -> str | None:
        """The exchange rate used in conversion."""
        return self._get_response_field("exchange_rate")

    @property
    def last_updated(self) -> str | None:
        """The exchange rate used in conversion."""
        return self._get_response_field("last_updated")
