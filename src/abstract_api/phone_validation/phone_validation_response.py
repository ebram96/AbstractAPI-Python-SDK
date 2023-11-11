import requests

from ..core.bases import JSONResponse
from ..core.mixins import NestedEntitiesMixin
from .response_fields import RESPONSE_FIELDS


class Format:
    """Format entity in phone validation response."""

    def __init__(self, international: str, local: str) -> None:
        """Initializes a new Format."""
        self._international = international
        self._local = local

    @property
    def international(self) -> str:
        """The international format of the submitted phone number.

        This means appending the phone number’s country code and a "+" at
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


class Country:
    """Country entity in phone validation response."""

    def __init__(self, code: str, name: str, prefix: str) -> None:
        """Initializes a new Country."""
        self._code = code
        self._name = name
        self._prefix = prefix

    @property
    def code(self) -> str | None:
        """The country’s two-letter ISO 3166-1 alpha-2 code."""
        return self._code

    @property
    def name(self) -> str | None:
        """The name of the country in which the phone number is registered."""
        return self._name

    @property
    def prefix(self) -> str | None:
        """The country’s calling code prefix."""
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

    @property
    def phone(self) -> str | None:
        """The phone number submitted for validation and verification."""
        return self._get_response_field("phone")

    @property
    def valid(self) -> bool | None:
        """Is true if the phone number submitted is valid."""
        return self._get_response_field("valid")

    @property
    def format(self) -> Format | None:
        """International and local formats of the submitted number."""
        return self._get_response_field("format")

    @property
    def country(self) -> Country | None:
        """The of the phone number’s country."""
        return self._get_response_field("country")

    @property
    def location(self) -> str | None:
        """As much location details as are available from AbstractAPI's data.

        This can include the region, state / province, and in some cases down
        to the city.
        """
        return self._get_response_field("location")

    @property
    def type(self) -> str | None:
        """The type of phone number.

        The possible values are: Landline, Mobile, Satellite, Premium,
        Paging, Special, Toll_Free, and Unknown.
        """
        # TODO: Use enum.
        return self._get_response_field("type")

    @property
    def carrier(self) -> str | None:
        """The carrier that the number is registered with."""
        return self._get_response_field("carrier")
