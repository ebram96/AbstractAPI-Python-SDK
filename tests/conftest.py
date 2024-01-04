import pytest
import requests

from tests.utils import generate_response


@pytest.fixture
def base_url():
    """Base service URL."""
    return "https://{subdomain}.abstractapi.com/v1/"


@pytest.fixture
def blank_response(request):
    """Blank Response instance, no status_code, no content."""
    return generate_response(data=None, status_code=requests.codes.NO_CONTENT)


_DEFAULT_CONTENT = b"some-random-testing-content"
_DEFAULT_STATUS_CODE = requests.codes.OK


@pytest.fixture(
    scope="function",
    params=[dict(data=_DEFAULT_CONTENT, status_code=_DEFAULT_STATUS_CODE)]
)
def content_response(request):
    """Response instance with given data and status code.

    If data or status_code were omitted, default values are used.
    """
    return generate_response(
        request.param.get("data", _DEFAULT_CONTENT),
        request.param.get("status_code", _DEFAULT_STATUS_CODE)
    )


@pytest.fixture
def json_response():
    """Response instance with given JSON data."""
    return generate_response(
        data={"sample1": "value1", "sample2": "value2"},
        status_code=requests.codes.OK
    )
