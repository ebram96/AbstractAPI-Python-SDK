from typing import Type

import requests

from abstract_api.bases import JSONResponse

from .response_fields.validation import VALIDATION_RESPONSE_FIELDS


class Country:
    """Country entity in VAT validation response."""

    def __init__(self, code: str, name: str) -> None:
        """Initializes a new Country."""
        self._code = code
        self._name = name

    @property
    def code(self) -> str | None:
        """The two-letter ISO 3166-1 alpha-2 country code.

        The two-letter ISO 3166-1 alpha-2 code of the country associated
        with the VAT number.
        """
        return self._code

    @property
    def name(self) -> str | None:
        """Name of country of the company associated with the VAT number."""
        return self._name


class Company:
    """Company entity in VAT validation response."""

    def __init__(self, address: str, name: str) -> None:
        """Initializes a new Company."""
        self._address = address
        self._name = name

    @property
    def address(self) -> str | None:
        """The address of the company associated with the VAT number."""
        return self._address

    @property
    def name(self) -> str | None:
        """The name of the company associated with the VAT number."""
        return self._name


class VATValidationResponse(JSONResponse):
    """VAT validation service response."""

    _nested_entities: dict[str, Type] = {
        "company": Company,
        "country": Country
    }

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new VATValidationResponse."""
        super().__init__(response)
        self._response_fields = VALIDATION_RESPONSE_FIELDS
        not_in_response = object()
        for field in VALIDATION_RESPONSE_FIELDS:
            value = self.meta.body_json.get(field, not_in_response)
            # Set property only if field was returned
            if value is not not_in_response:
                # TODO: Move to parent class
                setattr(
                    self,
                    f"_{field}",
                    value if field not in self._nested_entities
                    else self._nested_entities[field](**value)
                )

    @property
    def vat_number(self) -> str | None:
        """The submitted VAT number."""
        return self._get_response_field("vat_number")

    @property
    def valid(self) -> bool | None:
        """Is true if the submitted VAT number is valid."""
        return self._get_response_field("valid")

    @property
    def company(self) -> Company | None:
        """Company details."""
        return self._get_response_field("company")

    @property
    def country(self) -> Country | None:
        """Country details."""
        return self._get_response_field("country")
