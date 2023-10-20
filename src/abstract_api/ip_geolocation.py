from typing import Iterable, Any

from ._base_service import _BaseService


class IPGeolocation(_BaseService):
    """AbstractAPI IP geolocation service

    Used to determine the location and other details of IP addresses.

    Attributes:
        _subdomain: IP Geolocation service subdomain.
        _acceptable_fields: Fields that are available to be returned from
            IP Geolocation service endpoint.
        _fields: Fields selected by user to be returned from IP Geolocation
            service endpoint.
    """
    _subdomain: str = "ipgeolocation"
    _acceptable_fields: frozenset[str] = {
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
      "security"
    }
    _fields: frozenset[str] | None = None

    def __init__(self, *, fields: Iterable[str] | None = None, **kwargs) -> None:
        """Constructs an IPGeolocation.

        Args:
            fields: Iterable of strings that should be retrieved for each
                IP analysis.
        """
        super().__init__(**kwargs)
        if fields is not None:
            self.fields = fields

    @property
    def fields(self) -> frozenset[str]:
        """Gets selected return fields."""
        if self._fields:
            return self._fields
        return self._acceptable_fields

    @fields.setter
    def fields(self, fields: Iterable[str]) -> None:
        """Sets selected return fields."""
        if any(f not in self._acceptable_fields for f in fields):
            # TODO: Enhance this
            raise ValueError
        self._fields = frozenset(fields)

    def _request_fields(self, fields: Iterable[str] | None = None) -> str:
        """Builds a string that contains selected return fields that can be
        used as a URL query parameter.

        Args:
            fields: Selected return fields.

        Returns:
            Comma-separated string with all selected return fields.
        """
        return ",".join(fields or self.fields)

    def analyze(self, ip: str, fields: Iterable[str] | None = None) -> dict[str | Any]:
        """Analyzes an IP address for geographical data

        Args:
            ip: A valid IP address to analyze.
            fields: Selected return fields.

        Returns:
            A dict that contains the response to API call.
        """
        result = self._service_request(
            ip_address=ip, fields=self._request_fields(fields)
        )
        return result
