import pytest


@pytest.fixture
def vat_validation_sample():
    return {
        "vat_number": "SE556656688001",
        "valid": True,
        "company": {
            "name": "GOOGLE SWEDEN AB",
            "address": "GOOGLE IRLAND LTD \nM COLLINS, GORDON HOUSE \nBARROW STREET, DUBLIN 4 \nIRLAND"
        },
        "country": {
            "code": "SE",
            "name": "Sweden"
        }
    }


@pytest.fixture
def vat_calculation_sample():
    return {
        "amount_excluding_vat": "100.00",
        "amount_including_vat": "119.00",
        "vat_amount": "19.00",
        "vat_category": "standard",
        "vat_rate": "0.190",
        "country": {
            "code": "DE",
            "name": "Germany"
        }
    }
