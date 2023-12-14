import pytest


@pytest.fixture
def iban_validation_sample():
    return {
        "iban": "EG380019000500000000263180002",
        "is_valid": True
    }
