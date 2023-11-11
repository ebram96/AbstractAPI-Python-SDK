from typing import Any

import requests

from abstract_api.bases import JSONResponse

from .response_fields import RESPONSE_FIELDS


class Holiday:
    """Holiday entity in VAT Holidays response."""

    def __init__(
        self,
        name: str,
        name_local: str,
        language: str,
        description: str,
        country: str,
        location: str,
        type: str,
        date: str,
        date_year: str,
        date_month: str,
        date_day: str,
        week_day: str
    ) -> None:
        """Initializes a new Holiday."""
        self._name = name
        self._name_local = name_local
        self._language = language
        self._description = description
        self._country = country
        self._location = location
        self._type = type
        self._date = date
        self._date_year = date_year
        self._date_month = date_month
        self._date_day = date_day
        self._week_day = week_day

    @property
    def name(self) -> str:
        """The name of the holiday."""
        return self._name

    @property
    def name_local(self) -> str:
        """The local name of the holiday."""
        return self._name_local

    @property
    def language(self) -> str:
        """The language in which name_local is in."""
        return self._language

    @property
    def description(self) -> str:
        """A short description or additional details on the holiday.

        Such as the holiday is a part of a long weekend.
        """
        return self._description

    @property
    def country(self) -> str:
        """The country in which the holiday occurs.

        Returned directly from the request.
        """
        return self._country

    @property
    def location(self) -> str:
        """The location or region in which the holiday occurs.

        If the holiday is that specific.
        """
        return self._location

    @property
    def type(self) -> str:
        """The type of holiday it is.

        (e.g., public holiday, religious holiday, etc.).
        """
        return self._type

    @property
    def date(self) -> str:
        """The date on which the holiday occurs."""
        return self._date

    @property
    def date_year(self) -> str:
        """The year in which the holiday occurs."""
        return self._date_year

    @property
    def date_month(self) -> str:
        """The month in which the holiday occurs."""
        return self._date_month

    @property
    def date_day(self) -> str:
        """The day in which the holiday occurs."""
        return self._date_day

    @property
    def week_day(self) -> str:
        """The day of the week on which the holiday occurs.

        (Monday, Tuesday, Wednesday, etc.).
        """
        return self._week_day


class HolidaysResponse(JSONResponse):
    """Holidays service response."""

    def _init_response_field(self, field: str, value: Any) -> None:
        """TODO."""
        holidays = []
        for c in value:
            holidays.append(Holiday(**c))
        self._holidays = frozenset(holidays)

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new VATValidationResponse."""
        super().__init__(response, RESPONSE_FIELDS, list_response=True)

    @property
    def holidays(self) -> frozenset[Holiday]:
        """The returned holidays."""
        return self._get_response_field("holidays")
