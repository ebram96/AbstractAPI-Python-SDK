from unittest.mock import call

import pytest
import requests

from abstract_api import WebsiteScreenshot
from abstract_api.core.exceptions import ClientRequestError
from abstract_api.core.validators import numerical
from abstract_api.website_screenshot import WebsiteScreenshotResponse


class TestWebsiteScreenshot:
    """WebsiteScreenshot service tests."""
    @pytest.fixture
    def service(self) -> WebsiteScreenshot:
        return WebsiteScreenshot("no-api-key")

    @pytest.mark.parametrize(
        ("width", "height"),
        [(None, 100), (200, None), (200, 100)]
    )
    def test__validate_params_with_capture_full_page(
        self, service, width, height
    ):
        # Given
        capture_full_page = True

        # Then
        with pytest.raises(ClientRequestError):
            # When
            service._validate_params(
                capture_full_page=capture_full_page,
                height=height,
                width=width
            )

    def test__validate_params_without_capture_full_page(self, service, mocker):
        # Given
        capture_full_page = False
        width = 100
        height = 200
        mocked_greater_or_equal = mocker.patch.object(
            numerical,
            "greater_or_equal",
            wraps=numerical.greater_or_equal
        )

        # When
        service._validate_params(
            capture_full_page=capture_full_page,
            height=height,
            width=width
        )

        # Then
        mocked_greater_or_equal.assert_has_calls((
            call("width", width, 0),
            call("height", height, 0)
        ))
        assert mocked_greater_or_equal.call_count == 2

    def test_capture(self, service, base_url, mocker, requests_mock):
        # Given
        website = "https://example.com"
        url = base_url.format(subdomain=WebsiteScreenshot._subdomain)
        content = b'some-website-screenshot-content'
        requests_mock.get(url, content=content)
        mocked__validate_params = mocker.patch.object(
            service,
            "_validate_params",
            wraps=service._validate_params
        )
        mocked__service_request = mocker.patch.object(
            service,
            "_service_request",
            wraps=service._service_request
        )

        # When
        response = service.capture(website)

        # Then
        mocked__validate_params.assert_called_once_with(
            self=service,
            url=website,
            capture_full_page=None,
            width=None,
            height=None,
            delay=None,
            css_injection=None,
            user_agent=None,
            export_format=None
        )
        mocked__service_request.assert_called_once_with(
            _response_class=WebsiteScreenshotResponse,
            url=website,
            capture_full_page=None,
            width=None,
            height=None,
            delay=None,
            css_injection=None,
            user_agent=None,
            export_format=None
        )
        assert isinstance(response, WebsiteScreenshotResponse)
        assert response.content == content
        assert response.meta.body == content
        assert response.meta.http_status == requests.codes.OK
