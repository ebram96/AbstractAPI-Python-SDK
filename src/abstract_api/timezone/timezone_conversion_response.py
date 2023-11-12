import requests

from ..core.bases import JSONResponse
from ..core.mixins import NestedEntitiesMixin
from .response_fields import CONVERSION_RESPONSE_FIELDS


class Timezone:
    """Timezone entity in timezone conversion response.

    Used to represent base and target location timezones.
    """

    def __init__(
        self,
        datetime: str,
        timezone_name: str,
        timezone_location: str,
        timezone_abbreviation: str,
        gmt_offset: int,
        is_dst: bool,
        requested_location: str,
        latitude: float,
        longitude: float
    ) -> None:
        """Initializes a new Timezone."""
        self._datetime = datetime
        self._timezone_name = timezone_name
        self._timezone_location = timezone_location
        self._timezone_abbreviation = timezone_abbreviation
        self._gmt_offset = gmt_offset
        self._is_dst = is_dst
        self._requested_location = requested_location
        self._latitude = latitude
        self._longitude = longitude

    @property
    def datetime(self) -> str | None:
        """The current date and time."""
        return self._datetime

    @property
    def timezone_name(self) -> str | None:
        """Timezone's name from IANA Time Zone Database.

        Read more: https://www.iana.org/time-zones
        """
        return self._timezone_name

    @property
    def timezone_location(self) -> str | None:
        """Timezone's location."""
        return self._timezone_location

    @property
    def timezone_abbreviation(self) -> str | None:
        """Timezone's abbreviation, also from IANA Time Zone Database."""
        return self._timezone_abbreviation

    @property
    def gmt_offset(self) -> int | None:
        """Timezone's offset from Greenwich Mean Time (GMT).

        Read more: https://greenwichmeantime.com/what-is-gmt
        """
        return self._gmt_offset

    @property
    def is_dst(self) -> bool | None:
        """Whether the location is currently in Daylight Savings Time (DST).

        Read more: https://wikipedia.org/wiki/Daylight_saving_time
        """
        return self._is_dst

    @property
    def requested_location(self) -> str | None:
        """The location from the request."""
        return self._requested_location

    @property
    def latitude(self) -> float | None:
        """Decimal of the longitude found for the requested_location."""
        return self._latitude

    @property
    def longitude(self) -> float | None:
        """Decimal of the longitude found for the requested_location."""
        return self._longitude


class TimezoneConversionResponse(NestedEntitiesMixin, JSONResponse):
    """Timezone conversion service response."""

    _nested_entities = {
        "base_location": Timezone,
        "target_location": Timezone
    }

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new TimezoneConversionResponse."""
        super().__init__(response, CONVERSION_RESPONSE_FIELDS)

    @property
    def base_location(self) -> Timezone:
        """The time and timezone details of base location from request."""
        return self._get_response_field("base_location")

    @property
    def target_location(self) -> Timezone:
        """The time and timezone details of target location from request."""
        return self._get_response_field("target_location")
