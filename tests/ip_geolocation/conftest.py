import pytest


@pytest.fixture
def ip_geolocation_sample():
    return {
        "ip_address": "142.250.201.46",
        "city": "Montreal",
        "city_geoname_id": 6077243,
        "region": "Quebec",
        "region_iso_code": "QC",
        "region_geoname_id": 6115047,
        "postal_code": "H4X",
        "country": "United States",
        "country_code": "US",
        "country_geoname_id": 6252001,
        "country_is_eu": False,
        "continent": "North America",
        "continent_code": "NA",
        "continent_geoname_id": 6255149,
        "longitude": -97.822,
        "latitude": 37.751,
        "security": {
            "is_vpn": False
        },
        "timezone": {
            "name": "America/Chicago",
            "abbreviation": "CST",
            "gmt_offset": -6,
            "current_time": "16:20:38",
            "is_dst": False
        },
        "flag": {
            "emoji": "🇺🇸",
            "unicode": "U+1F1FA U+1F1F8",
            "png": "https://static.abstractapi.com/country-flags/US_flag.png",
            "svg": "https://static.abstractapi.com/country-flags/US_flag.svg"
        },
        "currency": {
            "currency_name": "USD",
            "currency_code": "USD"
        },
        "connection": {
            "autonomous_system_number": 15169,
            "autonomous_system_organization": "GOOGLE",
            "connection_type": "Corporate",
            "isp_name": "Google LLC",
            "organization_name": "Google LLC"
        }
    }
