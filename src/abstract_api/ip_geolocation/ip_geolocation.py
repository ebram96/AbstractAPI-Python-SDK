from typing import Iterable

from abstract_api._base_service import BaseService
from abstract_api.exceptions import ResponseParseError

from .acceptable_fields import ACCEPTABLE_FIELDS
from .ip_geolocation_response import IPGeolocationResponse


class IPGeolocation(BaseService):
    """AbstractAPI IP geolocation service

    Used to determine the location and other details of IP addresses.

    Attributes:
        _subdomain: IP Geolocation service subdomain.
        _response_fields: Selected response fields to be returned from IP
            Geolocation service endpoint.
    """
    _subdomain: str = "ipgeolocation"
    _response_fields: frozenset[str] | None = None

    def __init__(
        self,
        *,
        response_fields: Iterable[str] | None = None,
        **kwargs
    ) -> None:
        """Constructs an IPGeolocation.

        Args:
            response_fields: Selected response fields.
        """
        super().__init__(**kwargs)
        if response_fields is not None:
            self.response_fields = response_fields

    @property
    def response_fields(self) -> frozenset[str]:
        """Gets selected response fields."""
        if self._response_fields:
            return self._response_fields
        return ACCEPTABLE_FIELDS

    @response_fields.setter
    def response_fields(self, fields: Iterable[str]) -> None:
        """Sets selected response fields."""
        if any(f not in ACCEPTABLE_FIELDS for f in fields):
            # TODO: Enhance this
            raise ValueError
        self._response_fields = frozenset(fields)

    def _response_fields_as_param(
        self,
        response_fields: Iterable[str] | None = None
    ) -> str:
        """Builds a string that contains selected return fields that can be
        used as a URL query parameter.

        Args:
            response_fields: Selected response fields.

        Returns:
            Comma-separated string with all selected response fields.
        """
        return ",".join(response_fields or self.response_fields)

    def check(
        self,
        ip: str,
        fields: Iterable[str] | None = None
    ) -> IPGeolocationResponse:
        """Analyzes an IP address for geographical data

        Args:
            ip: A valid IP address to analyze.
            fields: Selected return fields.

        Returns:
            A dict that contains the response to API call.
        """
        # TODO: Handle request errors.
        response = self._service_request(
            ip_address=ip,
            fields=self._response_fields_as_param(fields)
        )

        try:
            ip_geolocation_response = IPGeolocationResponse(response)
        except Exception as e:
            raise ResponseParseError(
                "Failed to parse response as IPGeolocationResponse"
            ) from e

        return ip_geolocation_response
