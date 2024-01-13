from typing import Annotated, ClassVar, Optional, Union

from ..core.bases import BaseService
from ..core.exceptions import ClientRequestError
from .current_timezone_response import CurrentTimezoneResponse
from .timezone_conversion_response import TimezoneConversionResponse

Location = Union[str, Annotated[list[float], 2], tuple[float, float]]


class Timezone(BaseService):
    """AbstractAPI timezone service.

    Used to find, convert, and manage time and timezone data across the world.

    Attributes:
        _subdomain: Timezone service subdomain.
    """
    _subdomain = "timezone"
    _service_name_env_var: ClassVar[str] = "TIMEZONE"

    @staticmethod
    def _validate_location(param: str, location: Location) -> None:
        """Validates a given location.

        Args:
            param: Name of the parameter passed to service.
            location: Value of location passed.
        """
        if isinstance(location, (list, tuple)):
            if len(location) != 2:
                raise ClientRequestError(
                    f"'{param}' must contain both/only longitude and latitude."
                )

    @staticmethod
    def _location_as_param(location: Location) -> str:
        """Converts location to a request query parameter value.

        This method converts the location from list/tuple of floats to a
        string if the location given is a list/tuple.
        It does nothing if the given location is already a string.

        Args:
            location: Location to be converted.

        Returns:
            A string with location as query parameter value.
        """
        if isinstance(location, (list, tuple)):
            location = ",".join(map(str, location))
        return location

    def current(self, location: Location) -> CurrentTimezoneResponse:
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
        self._validate_location("location", location)
        return self._service_request(
            _response_class=CurrentTimezoneResponse,
            _action="current_time",
            location=self._location_as_param(location)
        )

    def convert(
        self,
        base_location: Location,
        target_location: Location,
        base_datetime: Optional[str] = None
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
            base_datetime: The datetime you're converting.

        Returns:
            TimezoneConversionResponse representing API call response.
        """
        self._validate_location("base_location", base_location)
        self._validate_location("target_location", target_location)
        return self._service_request(
            _response_class=TimezoneConversionResponse,
            _action="convert_time",
            base_location=self._location_as_param(base_location),
            target_location=self._location_as_param(target_location),
            base_datetime=base_datetime
        )
