from abstract_api.bases import BaseService

from .current_timezone_response import CurrentTimezoneResponse
from .timezone_conversion_response import TimezoneConversionResponse


class Timezone(BaseService):
    """AbstractAPI timezone service.

    Used to find, convert, and manage time and timezone data across the world.

    Attributes:
        _subdomain: timezone service subdomain.
    """
    _subdomain: str = "timezone"

    @staticmethod
    def _location_as_param(
        location: str | list[float] | tuple[float, ...]
    ) -> str:
        """Converts location to a request query parameter value.

        This method converts the location from list/tuple of floats to a
        string if the location given is a list/tuple.
        It does nothing if the given location is already a string.

        Args:
            location: Location to be converted.

        Returns:
            A string with location as query parameter value.
        """
        if isinstance(location, list) or isinstance(location, tuple):
            location = ",".join(map(str, location))

        return location

    def current(
        self,
        location: str | list[float] | tuple[float, ...]
    ) -> CurrentTimezoneResponse:
        """Finds the current time, date, and timezone of a given location.

        Args:
            location: The location to determine the current time and
                timezone of. This parameter accepts the location as
                a string (e.g., Los Angeles, CA),
                a longitude and latitude (e.g., -31.4173391,-64.183319),
                or an IP address (e.g., 82.111.111.111).

        Returns:
            CurrentTimezoneResponse representing API call response.
        """
        return self._service_request(
            _response_class=CurrentTimezoneResponse,
            _action="current_time",
            location=self._location_as_param(location)
        )

    def convert(
        self,
        base_location: str | list[float] | tuple[float, ...],
        target_location: str | list[float] | tuple[float, ...],
        base_datetime: str | None = None
    ) -> TimezoneConversionResponse:
        """Converts datetime of base location to target location's datetime.

        By default, it converts the current time, but the conversion can
        take place in either the past or future with a simple parameter.

        Args:
            base_location: The location you use as a base to convert the
                datetime for. This parameter accepts the location as
                a string (e.g., Los Angeles, CA),
                a longitude and latitude (e.g., -31.4173391,-64.183319),
                or an IP address (e.g., 82.111.111.111).
            target_location: The location you want to get the datetime for.
                This parameter accepts the location as
                a string (e.g., Los Angeles, CA),
                a longitude and latitude (e.g., -31.4173391,-64.183319),
                or an IP address (e.g., 82.111.111.111).
            base_datetime: The datetime you’re converting.

        Returns:
            TimezoneConversionResponse representing API call response.
        """
        return self._service_request(
            _response_class=TimezoneConversionResponse,
            _action="convert_time",
            base_location=self._location_as_param(base_location),
            target_location=self._location_as_param(target_location),
            base_datetime=base_datetime
        )
