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


@pytest.fixture
def timezone_conversion_sample():
    return {
        "base_location": {
            "datetime": "2023-12-24 23:30:57",
            "timezone_name": "Eastern European Standard Time",
            "timezone_location": "Africa/Cairo",
            "timezone_abbreviation": "EET",
            "gmt_offset": 2,
            "is_dst": False,
            "requested_location": "Cairo, Egypt",
            "latitude": 30.0443879,
            "longitude": 31.2357257
        },
        "target_location": {
            "datetime": "2023-12-24 16:30:58",
            "timezone_name": "Eastern Standard Time",
            "timezone_location": "America/Toronto",
            "timezone_abbreviation": "EST",
            "gmt_offset": -5,
            "is_dst": False,
            "requested_location": "Montreal, Canada",
            "latitude": 45.5031824,
            "longitude": -73.5698065
        }
    }
