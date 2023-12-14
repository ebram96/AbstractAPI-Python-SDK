import pytest


@pytest.fixture
def iban_validation_sample():
    return {
        "iban": "BE71096123456769",
        "is_valid": True
    }
