from unittest.mock import call

from abstract_api import Holidays
from abstract_api.core.validators import numerical
from abstract_api.holidays import HolidaysResponse


class TestHolidays:
    def test__validate_params(self, mocker):
        # Given
        kwargs = {
            "year": 2023,
            "month": 1,
            "day": 1
        }
        mocked_between = mocker.patch.object(
            numerical, "between", wraps=numerical.between
        )

        # When
        Holidays._validate_params(**kwargs)

        # Then
        mocked_between.assert_has_calls([
            call("year", kwargs["year"], 1800, 2100),
            call("month", kwargs["month"], 1, 12),
            call("day", kwargs["day"], 1, 31)
        ])
        assert mocked_between.call_count == 3

    def test_lookup(
        self,
        holidays_sample,
        base_url,
        mocker,
        requests_mock
    ):
        # Given
        country = "EG"
        year = 2023
        month = 6
        day = 30
        url = base_url.format(subdomain=Holidays._subdomain)
        requests_mock.get(url, json=holidays_sample)
        service = Holidays(api_key="no-api-key")
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )
        mocked__validate_params = mocker.patch.object(
            service, "_validate_params", wraps=service._validate_params
        )

        # When
        response = service.lookup(country, year, month, day)

        # Then
        assert isinstance(response, HolidaysResponse)
        mocked__validate_params.assert_called_once_with(
            self=service,
            country=country,
            year=year,
            month=month,
            day=day
        )
        mocked__service_request.assert_called_once_with(
            _response_class=HolidaysResponse,
            country=country,
            year=year,
            month=month,
            day=day
        )
