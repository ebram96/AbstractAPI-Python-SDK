from abstract_api.bases import BaseService
from abstract_api.exceptions import ResponseParseError

from .current_timezone_response import CurrentTimezoneResponse


class Timezone(BaseService):
    """AbstractAPI timezone service.

    Used to find, convert, and manage time and timezone data across the world.

    Attributes:
        _subdomain: timezone service subdomain.
    """
    _subdomain: str = "timezone"

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
        if isinstance(location, list) or isinstance(location, tuple):
            location = ",".join(map(str, location))

        response = self._service_request(
            action="current_time",
            location=location
        )

        try:
            current_timezone_response = CurrentTimezoneResponse(
                response=response
            )
        except Exception as e:
            raise ResponseParseError(
                "Failed to parse response as CurrentTimezoneResponse"
            ) from e

        return current_timezone_response
