from ..core.bases import BaseService
from ..core.validators import numerical
from .holidays_response import HolidaysResponse


class Holidays(BaseService[HolidaysResponse]):
    """AbstractAPI Holidays service.

    Used to get the public, local, religious, and other holidays of a
    particular country.

    Attributes:
        _subdomain: Holidays service subdomain.
    """
    _subdomain = "holidays"

    @staticmethod
    def _validate_params(**kwargs) -> None:
        """Validates passed service parameters."""
        ranged = {
            "year": (1800, 2100),
            "month": (1, 12),
            "day": (1, 31)
        }
        for param, allowed_range in ranged.items():
            numerical.between(param, kwargs[param], *allowed_range)

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
            country: The country's two-letter ISO 3166-1 alpha-2 code.
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
        self._validate_params(**locals())
        return self._service_request(
            _response_class=HolidaysResponse,
            country=country,
            year=year,
            month=month,
            day=day
        )
