import pytest


@pytest.fixture
def current_timezone_sample():
    return {
        "datetime": "2023-12-24 00:48:51",
        "timezone_name": "Eastern European Standard Time",
        "timezone_location": "Africa/Cairo",
        "timezone_abbreviation": "EET",
        "gmt_offset": 2,
        "is_dst": False,
        "requested_location": "Cairo, Egypt",
        "latitude": 30.0443879,
        "longitude": 31.2357257
    }
