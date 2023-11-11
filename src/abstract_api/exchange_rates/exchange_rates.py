from typing import Iterable

from ..bases import BaseService
from .exchange_rates_conversion_response import ExchangeRatesConversionResponse
from .historical_exchange_rates_response import HistoricalExchangeRatesResponse
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
        return self._service_request(
            _response_class=LiveExchangeRatesResponse,
            _action="live",
            base=base,
            target=self._target_as_param(target)
        )

    def convert(
        self,
        base: str,
        target: str,
        date: str | None = None,
        base_amount: float | None = None
    ) -> ExchangeRatesConversionResponse:
        """Finds exchange rates from base currency to target currency/ies.

        Args:
            base: Base currency used to get the latest exchange rate(s) for.
                Uses the ISO 4217 currency standard (e.g., USD for United
                States Dollars).
            target: The target currency to convert the base_amount to.
                Like the base parameters, any currency passed here follows the
                ISO 4217 standard. Note that unlike the other endpoints,
                convert only accepts one target currency at a time.
            date: The historical date you’d like to get rates from, in the
                format of YYYY-MM-DD. If you leave this blank, it will use the
                latest available rate.
            base_amount: The amount of the base currency you would like to
                convert to the target currency.

        Returns:
            ExchangeRatesConversionResponse representing API call response.
        """
        return self._service_request(
            _response_class=ExchangeRatesConversionResponse,
            _action="convert",
            base=base,
            target=target,
            date=date,
            base_amount=base_amount
        )

    def historical(
        self,
        base: str,
        date: str,
        target: Iterable[str] | None = None
    ) -> HistoricalExchangeRatesResponse:
        """Finds historical exchange rates from base to target currencies.

        Args:
            base: Base currency used to get the latest exchange rate(s) for.
                Uses the ISO 4217 currency standard (e.g., USD for United
                States Dollars).
            date: The historical date you’d like to get rates from, in the
                format of YYYY-MM-DD.
            target: The target currency or currencies to get the exchange rate
                of versus the base currency. Like the base parameters, any
                currency passed here follows the ISO 4217 standard.

        Returns:
            HistoricalExchangeRatesResponse representing API call response.
        """
        return self._service_request(
            _response_class=HistoricalExchangeRatesResponse,
            _action="historical",
            base=base,
            target=self._target_as_param(target),
            date=date
        )
