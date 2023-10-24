from typing import Iterable

from abstract_api._base_service import BaseService
from abstract_api.exceptions import ClientRequestError, ResponseParseError

from .acceptable_fields import ACCEPTABLE_FIELDS
from .ip_geolocation_response import IPGeolocationResponse


class IPGeolocation(BaseService):
    """AbstractAPI IP geolocation service.

    Used to determine the location and other details of IP addresses.

    Attributes:
        _subdomain: IP Geolocation service subdomain.
        _response_fields: Selected response fields to be returned from IP
            Geolocation service endpoint.
    """
    _subdomain: str = "ipgeolocation"

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
            self.response_fields = frozenset(response_fields)
        else:
            self.response_fields = ACCEPTABLE_FIELDS

    @staticmethod
    def _validate_response_fields(response_fields: Iterable[str]) -> None:
        """Validates whether all the given fields are acceptable.

        Args:
            response_fields: Selected response fields.
        """
        for field in response_fields:
            if field not in ACCEPTABLE_FIELDS:
                raise ClientRequestError(
                    f"Field '{field}' is not a valid response field for IP "
                    f"Geolocation service."
                )

    @property
    def response_fields(self) -> frozenset[str]:
        """Gets selected response fields."""
        if self._response_fields:
            return self._response_fields
        return ACCEPTABLE_FIELDS

    @response_fields.setter
    def response_fields(self, fields: Iterable[str]) -> None:
        """Sets selected response fields."""
        self._validate_response_fields(fields)
        self._response_fields = frozenset(fields)

    @staticmethod
    def _response_fields_as_param(response_fields: Iterable[str]) -> str:
        """Builds 'fields' URL query parameter.

         Builds a string that contains selected response fields to be used
         as a URL query parameter.

        Args:
            response_fields: Selected response fields.

        Returns:
            Comma-separated string with all selected response fields.
        """
        return ",".join(response_fields)

    def check(
        self,
        ip: str,
        fields: Iterable[str] | None = None
    ) -> IPGeolocationResponse:
        """Analyzes an IP address for geographical data.

        Args:
            ip: A valid IP address to analyze.
            fields: Selected response fields.

        Returns:
            A dict that contains the response to API call.
        """
        if fields:
            self._validate_response_fields(fields)
            response_fields = frozenset(fields)
        else:
            response_fields = self.response_fields

        # TODO: Handle request errors.
        response = self._service_request(
            ip_address=ip,
            fields=self._response_fields_as_param(response_fields)
        )

        try:
            ip_geolocation_response = IPGeolocationResponse(
                response=response,
                response_fields=response_fields
            )
        except Exception as e:
            raise ResponseParseError(
                "Failed to parse response as IPGeolocationResponse"
            ) from e

        return ip_geolocation_response
