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
