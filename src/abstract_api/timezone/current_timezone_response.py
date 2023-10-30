from typing import TYPE_CHECKING

import requests

from abstract_api.bases import JSONResponse

from .response_fields import CURRENT_RESPONSE_FIELDS


class CurrentTimezoneResponse(JSONResponse):
    """Current timezone service response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new CurrentTimezoneResponse."""
        super().__init__(response)
        self._response_fields = CURRENT_RESPONSE_FIELDS
        not_in_response = object()
        for field in CURRENT_RESPONSE_FIELDS:
            if TYPE_CHECKING:
                assert isinstance(self.meta.body_json, dict)
            value = self.meta.body_json.get(field, not_in_response)
            # Set property only if field was returned
            if value is not not_in_response:
                # TODO: Move to parent class
                setattr(self, f"_{field}", value)

    @property
    def datetime(self) -> str | None:
        """The current date and time of the requested_location."""
        return self._get_response_field("datetime")

    @property
    def timezone_name(self) -> str | None:
        """Timezone’s name from IANA Time Zone Database.

        Read more: https://www.iana.org/time-zones
        """
        return self._get_response_field("timezone_name")

    @property
    def timezone_location(self) -> str | None:
        """Timezone’s location."""
        return self._get_response_field("timezone_location")

    @property
    def timezone_abbreviation(self) -> str | None:
        """Timezone’s abbreviation, also from IANA Time Zone Database."""
        return self._get_response_field("timezone_abbreviation")

    @property
    def gmt_offset(self) -> str | None:
        """Timezone’s offset from Greenwich Mean Time (GMT).

        Read more: https://greenwichmeantime.com/what-is-gmt
        """
        return self._get_response_field("gmt_offset")

    @property
    def is_dst(self) -> str | None:
        """Whether the location is currently in Daylight Savings Time (DST).

        Read more: https://wikipedia.org/wiki/Daylight_saving_time
        """
        return self._get_response_field("is_dst")

    @property
    def requested_location(self) -> str | None:
        """The location from the request."""
        return self._get_response_field("requested_location")

    @property
    def latitude(self) -> float | None:
        """Decimal of the longitude found for the requested_location."""
        return self._get_response_field("latitude")

    @property
    def longitude(self) -> float | None:
        """Decimal of the longitude found for the requested_location."""
        return self._get_response_field("longitude")