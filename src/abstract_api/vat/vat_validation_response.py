from functools import cached_property
from typing import Optional

import requests

from ..core.bases import JSONResponse
from ..core.common_entities import Country
from ..core.mixins import NestedEntitiesMixin
from ._response_fields.validation import VALIDATION_RESPONSE_FIELDS


class Company:
    """Company entity in VAT validation response."""

    def __init__(self, address: str, name: str) -> None:
        """Initializes a new Company."""
        self._address = address
        self._name = name

    @property
    def address(self) -> Optional[str]:
        """The address of the company associated with the VAT number."""
        return self._address

    @property
    def name(self) -> Optional[str]:
        """The name of the company associated with the VAT number."""
        return self._name


class VATValidationResponse(NestedEntitiesMixin, JSONResponse):
    """VAT validation service response."""

    _nested_entities = {
        "company": Company,
        "country": Country
    }

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new VATValidationResponse."""
        super().__init__(response, VALIDATION_RESPONSE_FIELDS)

    @cached_property
    def vat_number(self) -> Optional[str]:
        """The submitted VAT number."""
        return self._get_response_field("vat_number")

    @cached_property
    def valid(self) -> Optional[bool]:
        """Is true if the submitted VAT number is valid."""
        return self._get_response_field("valid")

    @cached_property
    def company(self) -> Optional[Company]:
        """Company details."""
        return self._get_response_field("company")

    @cached_property
    def country(self) -> Optional[Country]:
        """Country details."""
        return self._get_response_field("country")
