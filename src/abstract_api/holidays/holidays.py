from abstract_api.bases import BaseService
from abstract_api.exceptions import ResponseParseError

from .holidays_response import HolidaysResponse


class Holidays(BaseService):
    """AbstractAPI Holidays service.

    Used to get the public, local, religious, and other holidays of a
    particular country.

    Attributes:
        _subdomain: Holidays service subdomain.
    """
    _subdomain: str = "holidays"

    def lookup(
        self,
        country: str,
        year: int | None = None,
        month: int | None = None,
        day: int | None = None
    ) -> HolidaysResponse:
        """Gets the list of holidays of a particular country.

        Can get the public, local, religious, and other holidays.

        Args:
            country: The country’s two-letter ISO 3166-1 alpha-2 code.
            year: The year to get the holiday(s) from. Note that this is
                optional on paid plans and required on free plans, and if left
                blank it will default to the current year.
            month: The month to get the holiday(s) from, in the format
                of 1-12 (e.g., 1 is January, 2 is February, etc.).
                Note that this is optional on paid plans and required on
                free plans, and if left blank it will default to the current
                month.
            day: The day to get the holiday(s) from, in the format of 1-31.
                Note that this is optional on paid plans and required on free
                plans, and if left blank it will default to the current day.

        Returns:
            HolidaysResponse representing API call response.
        """
        response = self._service_request(
            country=country,
            year=year,
            month=month,
            day=day
        )

        try:
            holidays_response = HolidaysResponse(response=response)
        except Exception as e:
            raise ResponseParseError(
                "Failed to parse response as HolidaysResponse"
            ) from e

        return holidays_response
