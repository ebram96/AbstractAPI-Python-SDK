import pytest


@pytest.fixture
def email_validation_sample():
    return {
        "email": "example@gmail.com",
        "autocorrect": "",
        "deliverability": "DELIVERABLE",
        "quality_score": "0.95",
        "is_valid_format": {
            "value": True,
            "text": "TRUE"
        },
        "is_free_email": {
            "value": True,
            "text": "TRUE"
        },
        "is_disposable_email": {
            "value": False,
            "text": "FALSE"
        },
        "is_role_email": {
            "value": False,
            "text": "FALSE"
        },
        "is_catchall_email": {
            "value": False,
            "text": "FALSE"
        },
        "is_mx_found": {
            "value": True,
            "text": "TRUE"
        },
        "is_smtp_valid": {
            "value": True,
            "text": "TRUE"
        }
    }
