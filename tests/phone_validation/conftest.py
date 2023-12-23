import pytest


@pytest.fixture
def phone_validation_sample():
    return {
        "phone": "201201234567",
        "valid": True,
        "format": {
            "international": "+201201234567",
            "local": "0120 123 4567"
        },
        "country": {
            "code": "EG",
            "name": "Egypt",
            "prefix": "+20"
        },
        "location": "Egypt",
        "type": "mobile",
        "carrier": "Orange"
    }
