from typing import Iterable

from ..bases import BaseService
from ..mixins import ResponseFieldsMixin
from .ip_geolocation_response import IPGeolocationResponse


class IPGeolocation(ResponseFieldsMixin, BaseService[IPGeolocationResponse]):
    """AbstractAPI IP geolocation service.

    Used to determine the location and other details of IP addresses.

    Attributes:
        _subdomain: IP Geolocation service subdomain.
        _response_fields: Selected response fields to be returned from IP
            Geolocation service endpoint.
    """
    _subdomain: str = "ipgeolocation"
    _response_fields = frozenset({
        "ip_address",
        "city",
        "city_geoname_id",
        "region",
        "region_iso_code",
        "region_geoname_id",
        "postal_code",
        "country",
        "country_code",
        "country_geoname_id",
        "country_is_eu",
        "continent",
        "continent_code",
        "continent_geoname_id",
        "longitude",
        "latitude",
        "security",
        "timezone",
        "flag",
        "currency",
        "connection"
    })

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
            IPGeolocationResponse representing API call response.
        """
        if fields:
            self._validate_response_fields(fields)
            response_fields = frozenset(fields)
        else:
            response_fields = self.response_fields

        return self._service_request(
            _response_class=IPGeolocationResponse,
            _response_class_kwargs={"response_fields": response_fields},
            ip_address=ip,
            fields=self._response_fields_as_param(response_fields)
        )
