import pytest


@pytest.fixture
def company_enrichment_sample():
    return {
        "name": "Google",
        "domain": "google.com",
        "year_founded": 1998,
        "industry": "Internet",
        "employees_count": 219238,
        "locality": "Mountain View",
        "country": "United States",
        "linkedin_url": "linkedin.com/company/google"
    }
