from functools import cached_property

import requests

from ..core.bases import JSONResponse
from ..core.common_entities import Country
from ..core.mixins import NestedEntitiesMixin
from .response_fields.calculation import CALCULATION_RESPONSE_FIELDS


class VATCalculationResponse(NestedEntitiesMixin, JSONResponse):
    """VAT calculation service response."""

    _nested_entities = {
        "country": Country
    }

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new VATCalculationResponse."""
        super().__init__(response, CALCULATION_RESPONSE_FIELDS)

    @cached_property
    def amount_excluding_vat(self) -> float | None:
        """The amount excluding the VAT."""
        return self._get_response_field("amount_excluding_vat")

    @cached_property
    def amount_including_vat(self) -> float | None:
        """The sum of the base amount and the VAT.

        It is amount_excl_vat + vat_amount.
        """
        return self._get_response_field("amount_including_vat")

    @cached_property
    def vat_amount(self) -> float | None:
        """The calculated amount of VAT."""
        return self._get_response_field("vat_amount")

    @cached_property
    def vat_category(self) -> str | None:
        """The optional category of the purchase.

        Used to determine whether it qualifies for a reduced rate.
        """
        return self._get_response_field("vat_category")

    @cached_property
    def vat_rate(self) -> float | None:
        """The VAT rate, from 0.01 to 0.99."""
        return self._get_response_field("vat_rate")

    @cached_property
    def country(self) -> Country | None:
        """Details of the country the VAT is calculated from."""
        return self._get_response_field("country")
