from functools import cached_property
from typing import Optional

import requests

from ..core.bases import JSONResponse
from ._response_fields import CURRENT_RESPONSE_FIELDS


class CurrentTimezoneResponse(JSONResponse):
    """Current timezone service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new CurrentTimezoneResponse."""
        super().__init__(response, CURRENT_RESPONSE_FIELDS)

    @cached_property
    def datetime(self) -> Optional[str]:
        """The current date and time of the requested_location."""
        return self._get_response_field("datetime")

    @cached_property
    def timezone_name(self) -> Optional[str]:
        """Timezone's name from IANA Time Zone Database.

        Read more: https://www.iana.org/time-zones
        """
        return self._get_response_field("timezone_name")

    @cached_property
    def timezone_location(self) -> Optional[str]:
        """Timezone's location."""
        return self._get_response_field("timezone_location")

    @cached_property
    def timezone_abbreviation(self) -> Optional[str]:
        """Timezone's abbreviation, also from IANA Time Zone Database."""
        return self._get_response_field("timezone_abbreviation")

    @cached_property
    def gmt_offset(self) -> Optional[int]:
        """Timezone's offset from Greenwich Mean Time (GMT).

        Read more: https://greenwichmeantime.com/what-is-gmt
        """
        return self._get_response_field("gmt_offset")

    @cached_property
    def is_dst(self) -> Optional[bool]:
        """Whether the location is currently in Daylight Savings Time (DST).

        Read more: https://wikipedia.org/wiki/Daylight_saving_time
        """
        return self._get_response_field("is_dst")

    @cached_property
    def requested_location(self) -> Optional[str]:
        """The location from the request."""
        return self._get_response_field("requested_location")

    @cached_property
    def latitude(self) -> Optional[float]:
        """Decimal of the longitude found for the requested_location."""
        return self._get_response_field("latitude")

    @cached_property
    def longitude(self) -> Optional[float]:
        """Decimal of the longitude found for the requested_location."""
        return self._get_response_field("longitude")
