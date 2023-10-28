from typing import Iterable

from abstract_api.bases import BaseService
from abstract_api.exceptions import ResponseParseError

from .live_exchange_rates_response import LiveExchangeRatesResponse


class ExchangeRates(BaseService):
    """AbstractAPI exchange rates service.

    Used to looking up the latest exchange rates for 80+ currencies, getting
    historical exchange rates, and converting an arbitrary amount from one
    currency to another.

    Attributes:
        _subdomain: Exchange rates service subdomain.
    """
    _subdomain: str = "exchange-rates"

    @staticmethod
    def _target_as_param(target: Iterable[str] | None = None) -> str | None:
        """Builds 'target' URL query parameter.

        Builds a string that contains selected target currencies to be used
        as a URL query parameter.

        Args:
            target: Selected target currencies.

        Returns:
            Comma-separated string with all selected target currencies.
        """
        if target is None:
            return None

        return ",".join(target)

    def live(
        self,
        base: str,
        target: Iterable[str] | None = None
    ) -> LiveExchangeRatesResponse:
        """Finds exchange rates from base currency to target currency/ies.

        Args:
            base: Base currency used to get the latest exchange rate(s) for.
                Uses the ISO 4217 currency standard (e.g., USD for United
                States Dollars).
            target: The target currency or currencies to get the exchange rate
                of versus the base currency. Like the base parameters, any
                currency passed here follows the ISO 4217 standard.

        Returns:
            VATValidationResponse representing API call response.
        """
        response = self._service_request(
            action="live",
            base=base,
            target=self._target_as_param(target)
        )

        try:
            live_exchange_rates_response = LiveExchangeRatesResponse(
                response=response
            )
        except Exception as e:
            raise ResponseParseError(
                "Failed to parse response as LiveExchangeRatesResponse"
            ) from e

        return live_exchange_rates_response
