from ..core.bases import BaseService
from .vat_calculation_response import VATCalculationResponse
from .vat_categories_response import VATCategoriesResponse
from .vat_validation_response import VATValidationResponse


class VAT(BaseService):
    """AbstractAPI VAT categories, validation, and calculation service.

    Used to validate and calculate VAT numbers and also to inquery about
    VAT categories.

    Attributes:
        _subdomain: VAT service subdomain.
    """
    _subdomain: str = "vat"

    def check(self, vat_number: str) -> VATValidationResponse:
        """Validates a VAT number.

        Args:
            vat_number: The VAT number to validate.

        Returns:
            VATValidationResponse representing API call response.
        """
        return self._service_request(
            _response_class=VATValidationResponse,
            _action="validate",
            vat_number=vat_number
        )

    def calculate(
        self,
        amount: float,
        country_code: str,
        is_vat_incl: bool | None = None,
        vat_category: str | None = None
    ) -> VATCalculationResponse:
        """Validates a VAT number.

        Args:
            amount: The amount that you would like to get the VAT amount
                for or from.
            country_code: The two-letter ISO 3166-1 alpha-2 code of the
                country in which the transaction takes place.
            is_vat_incl: If the amount already has VAT added, and you’d like
                to do the reverse calculation and split out the amount and
                VAT, set this parameter to true. If this parameter is not
                explicitly included it will default to False.
            vat_category: Some countries offer a reduced VAT rate for
                certain categories of goods. To determine if a reduced VAT
                is available and to apply it to the final amount, include
                the vat_category in the request.

        Returns:
            VATCalculationResponse representing API call response.
        """
        return self._service_request(
            _response_class=VATCalculationResponse,
            _action="calculate",
            amount=amount,
            country_code=country_code,
            is_vat_incl=is_vat_incl,
            vat_category=vat_category
        )

    def categories(self, country_code: str) -> VATCategoriesResponse:
        """Gets the list of VAT categories for a country.

        Args:
            country_code: The two-letter ISO 3166-1 alpha-2 code of the
                country in which the transaction takes place.

        Returns:
            VATCategoriesResponse representing API call response.
        """
        return self._service_request(
            _response_class=VATCategoriesResponse,
            _action="categories",
            country_code=country_code,
        )
