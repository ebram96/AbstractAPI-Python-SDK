from functools import cached_property
from typing import Optional

import requests

from ..core.bases import JSONResponse
from ..core.common_entities import Country as CommonCountry
from ..core.mixins import NestedEntitiesMixin
from ._response_fields import RESPONSE_FIELDS


class Format:
    """Format entity in phone validation response."""

    def __init__(self, international: str, local: str) -> None:
        """Initializes a new Format."""
        self._international = international
        self._local = local

    @property
    def international(self) -> str:
        """The international format of the submitted phone number.

        This means appending the phone number's country code and a "+" at
        the beginning.
        """
        return self._international

    @property
    def local(self) -> str:
        """The local or national format of the submitted phone number.

        For example, it removes any international formatting, such as "+1"
        in the case of the US.
        """
        return self._local


class Country(CommonCountry):
    """Country entity in phone validation response."""

    def __init__(self, prefix: str, **kwargs) -> None:
        """Initializes a new Country."""
        super().__init__(**kwargs)
        self._prefix = prefix

    @property
    def prefix(self) -> Optional[str]:
        """The country's calling code prefix."""
        return self._prefix


class PhoneValidationResponse(NestedEntitiesMixin, JSONResponse):
    """Phone validation service response."""

    _nested_entities = {
        "format": Format,
        "country": Country
    }

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new PhoneValidationResponse."""
        super().__init__(response, RESPONSE_FIELDS)

    @cached_property
    def phone(self) -> Optional[str]:
        """The phone number submitted for validation and verification."""
        return self._get_response_field("phone")

    @cached_property
    def valid(self) -> Optional[bool]:
        """Is true if the phone number submitted is valid."""
        return self._get_response_field("valid")

    @cached_property
    def format(self) -> Optional[Format]:
        """International and local formats of the submitted number."""
        return self._get_response_field("format")

    @cached_property
    def country(self) -> Optional[Country]:
        """The of the phone number's country."""
        return self._get_response_field("country")

    @cached_property
    def location(self) -> Optional[str]:
        """As much location details as are available from AbstractAPI's data.

        This can include the region, state / province, and in some cases down
        to the city.
        """
        return self._get_response_field("location")

    @cached_property
    def type(self) -> Optional[str]:
        """The type of phone number.

        The possible values are: Landline, Mobile, Satellite, Premium,
        Paging, Special, Toll_Free, and Unknown.
        """
        return self._get_response_field("type")

    @cached_property
    def carrier(self) -> Optional[str]:
        """The carrier that the number is registered with."""
        return self._get_response_field("carrier")
