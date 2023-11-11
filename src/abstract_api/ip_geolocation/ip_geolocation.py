from typing import Iterable

from ..core.bases import BaseService
from ..core.mixins import ResponseFieldsMixin
from .ip_geolocation_response import IPGeolocationResponse
from .response_fields import RESPONSE_FIELDS


class IPGeolocation(ResponseFieldsMixin, BaseService[IPGeolocationResponse]):
    """AbstractAPI IP geolocation service.

    Used to determine the location and other details of IP addresses.

    Attributes:
        _subdomain: IP Geolocation service subdomain.
        _response_fields: Selected response fields to be returned from IP
            Geolocation service endpoint.
    """
    _subdomain: str = "ipgeolocation"
    _response_fields = RESPONSE_FIELDS

    def check(
        self,
        ip: str,
        fields: Iterable[str] | None = None
    ) -> IPGeolocationResponse:
        """Analyzes an IP address for geographical data.

        Args:
            ip: A valid IP address to analyze.
            fields: Selected response fields (optional)..

        Returns:
            IPGeolocationResponse representing API call response.
        """
        selected_fields = self._prepare_selected_fields(fields)

        return self._service_request(
            _response_class=IPGeolocationResponse,
            _response_class_kwargs={"response_fields": selected_fields},
            ip_address=ip,
            fields=self._response_fields_as_param(selected_fields)
        )
