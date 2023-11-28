from io import BytesIO

import pytest
import requests


@pytest.fixture
def base_url():
    """Base service URL."""
    return "https://{subdomain}.abstractapi.com/v1/"


@pytest.fixture
def blank_response(request):
    """Blank Response instance, no status_code, no content."""
    return requests.Response()


@pytest.fixture(scope="function")
def ok_response(blank_response):
    """Response instance with status_code = OK."""
    r = blank_response
    r.status_code = requests.codes.OK
    return r


_DEFAULT_CONTENT = BytesIO(b"some-random-testing-content")
_DEFAULT_STATUS_CODE = requests.codes.OK


@pytest.fixture(
    scope="function",
    params=[dict(raw=_DEFAULT_CONTENT, status_code=_DEFAULT_STATUS_CODE)]
)
def content_response(request, blank_response):
    """Response instance with given raw content and status code.

    If raw content or status_code were omitted, default values are used.
    """
    r = blank_response
    r.raw = request.param.get("raw", _DEFAULT_CONTENT)
    r.status_code = request.param.get("status_code", _DEFAULT_STATUS_CODE)
    return r
