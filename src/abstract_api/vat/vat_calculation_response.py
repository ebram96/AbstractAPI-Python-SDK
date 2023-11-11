from typing import Any, Type

import requests

from ..bases import JSONResponse
from .response_fields.calculation import CALCULATION_RESPONSE_FIELDS


class Country:
    """Country entity in VAT calculation response."""

    def __init__(self, code: str, name: str) -> None:
        """Initializes a new Country."""
        self._code = code
        self._name = name

    @property
    def code(self) -> str | None:
        """The two-letter ISO 3166-1 alpha-2 code of the country.

        It is the code of the country in which the transaction takes place.
        """
        return self._code

    @property
    def name(self) -> str | None:
        """The name of the country the VAT is being calculated from."""
        return self._name


class VATCalculationResponse(JSONResponse):
    """VAT calculation service response."""

    _nested_entities: dict[str, Type] = {
        "country": Country
    }

    def _init_response_field(self, field: str, value: Any) -> None:
        """TODO."""
        setattr(
            self,
            f"_{field}",
            value if field not in self._nested_entities
            else self._nested_entities[field](**value)
        )

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new PhoneCalculationResponse."""
        super().__init__(response, CALCULATION_RESPONSE_FIELDS)

    @property
    def amount_excluding_vat(self) -> float | None:
        """The amount excluding the VAT."""
        return self._get_response_field("amount_excluding_vat")

    @property
    def amount_including_vat(self) -> float | None:
        """The calculated amount of VAT."""
        return self._get_response_field("amount_including_vat")

    @property
    def vat_amount(self) -> float | None:
        """The sum of the base amount and the VAT.

        It is amount_excl_vat + vat_amount.
        """
        return self._get_response_field("vat_amount")

    @property
    def vat_category(self) -> str | None:
        """The optional category of the purchase.

        Used to determine whether it qualifies for a reduced rate.
        """
        return self._get_response_field("vat_category")

    @property
    def vat_rate(self) -> float | None:
        """The VAT rate, from 0.01 to 0.99."""
        return self._get_response_field("vat_rate")

    @property
    def country(self) -> Country | None:
        """Details of the country the VAT is calculated from."""
        return self._get_response_field("country")
