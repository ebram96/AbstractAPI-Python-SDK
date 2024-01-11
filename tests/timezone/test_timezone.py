from unittest.mock import call

import pytest

from abstract_api import Timezone
from abstract_api.core.exceptions import ClientRequestError
from abstract_api.timezone import (
    CurrentTimezoneResponse,
    TimezoneConversionResponse
)


class TestTimezone:
    @pytest.fixture
    def service(self):
        return Timezone(api_key="no-api-key")

    @pytest.fixture
    def service_url(self, base_url, service):
        return base_url.format(subdomain=service._subdomain)

    @pytest.mark.parametrize(
        # Given
        "location",
        [
            (30.0594627,),
            (30.0594627, 31.1758899, 1.0),
            [30.0594627],
            [30.0594627, 31.1758899, 1.0]
        ]
    )
    def test__validate_location(self, location):
        # Then
        with pytest.raises(ClientRequestError):
            # When
            Timezone._validate_location("location", location)

    @pytest.mark.parametrize(
        # Given
        ["location", "expected"],
        [
            [(30.0594627, 31.1758899), "30.0594627,31.1758899"],
            [[30.0594627, 31.1758899], "30.0594627,31.1758899"],
            ["30.0594627,31.1758899", "30.0594627,31.1758899"],
            ["156.200.2.159", "156.200.2.159"],
            ["Cairo, Egypt", "Cairo, Egypt"],
        ]
    )
    def test__location_as_param(self, location, expected):
        # When
        location_param = Timezone._location_as_param(location)

        # Then
        assert location_param == expected

    @pytest.mark.parametrize(
        "location",
        [
            "Cairo, Egypt",
            "156.200.2.159",
            "30.0594627,31.1758899",
            [30.0594627, 31.1758899],
            (30.0594627, 31.1758899)
        ]
    )
    def test_current(
        self,
        location,
        service,
        service_url,
        current_timezone_sample,
        requests_mock,
        mocker
    ):
        # Given
        action = "current_time"
        requests_mock.get(service_url + action, json=current_timezone_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )
        mocked__validate_location = mocker.patch.object(
            service, "_validate_location", wraps=service._validate_location
        )

        # When
        response = service.current(location=location)

        # Then
        assert isinstance(response, CurrentTimezoneResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=CurrentTimezoneResponse,
            _action=action,
            location=service._location_as_param(location)
        )
        mocked__validate_location.assert_called_once_with("location", location)

    @pytest.mark.parametrize(
        ["base_location", "target_location"],
        [
            ["Cairo, Egypt", "Montreal, Canada"],
            ["Cairo, Egypt", "99.79.91.62"],
            ["Cairo, Egypt", "45.5587066,-74.0422178"],
            ["156.200.2.159", "Montreal, Canada"],
            ["156.200.2.159", "99.79.91.62"],
            ["30.0594627,31.1758899", "Montreal, Canada"],
            ["30.0594627,31.1758899", "99.79.91.62"],
            [[30.0594627, 31.1758899], "Montreal, Canada"],
            [[30.0594627, 31.1758899], "99.79.91.62"],
            [(30.0594627, 31.1758899), "Montreal, Canada"],
            [(30.0594627, 31.1758899), "99.79.91.62"],
        ]
    )
    def test_convert(
        self,
        base_location,
        target_location,
        service,
        service_url,
        current_timezone_sample,
        requests_mock,
        mocker
    ):
        # Given
        action = "convert_time"
        requests_mock.get(service_url + action, json=current_timezone_sample)
        mocked__service_request = mocker.patch.object(
            service, "_service_request", wraps=service._service_request
        )
        mocked__validate_location = mocker.patch.object(
            service, "_validate_location", wraps=service._validate_location
        )

        # When
        response = service.convert(base_location, target_location)

        # Then
        assert isinstance(response, TimezoneConversionResponse)
        mocked__service_request.assert_called_once_with(
            _response_class=TimezoneConversionResponse,
            _action=action,
            base_location=service._location_as_param(base_location),
            target_location=service._location_as_param(target_location),
            base_datetime=None
        )
        mocked__validate_location.assert_has_calls([
            call("base_location", base_location),
            call("target_location", target_location)
        ])
