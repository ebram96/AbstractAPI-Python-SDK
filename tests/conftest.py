import pytest


@pytest.fixture
def base_url():
    return "https://{subdomain}.abstractapi.com/v1/"
