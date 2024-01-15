from typing import ClassVar, Optional

from ..core.bases import BaseService
from ..core.exceptions import ClientRequestError
from ..core.validators import numerical
from .website_screenshot_response import WebsiteScreenshotResponse


class WebsiteScreenshot(BaseService[WebsiteScreenshotResponse]):
    """AbstractAPI website screenshot service.

    Used to request a screenshot of a webpage in a given URL.

    Attributes:
        _subdomain: Website screenshot service subdomain.
    """
    _subdomain = "screenshot"
    _service_name_env_var: ClassVar[str] = "WEBSITE_SCREENSHOT"

    @staticmethod
    def _validate_params(**kwargs) -> None:
        """Validates passed service parameters.

        Raises:
            ClientRequestError if a parameter has invalid/not acceptable value.
        """
        capture_full_page = kwargs["capture_full_page"]
        dimensions = ["width", "height"]
        for d in dimensions:
            value = kwargs[d]
            if value is not None:
                if capture_full_page is not None and capture_full_page:
                    raise ClientRequestError(
                        f"'{d}' is not a valid option when"
                        f" 'capture_full_page' is True"
                    )
                numerical.greater_or_equal(d, value, 0)

    def capture(
        self,
        url: str,
        capture_full_page: Optional[bool] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        delay: Optional[int] = None,
        css_injection: Optional[str] = None,
        user_agent: Optional[str] = None,
        export_format: Optional[str] = None
    ) -> WebsiteScreenshotResponse:
        """Captures a screenshot of a webpage in the given URL.

        Args:
            url: The URL to get the screenshot of. Note that this parameter
                should include the full HTTP Protocol (http:// or https://).
            capture_full_page: If true the request will capture the entire
                height and width of the page. Defaults to True.
            width: The width in pixels of the view port to use to capture
                the image.
            height: The height in pixels of the view port to use to capture
                the image.
            delay: The time in seconds to wait between loading the page and
                taking the screenshot.
            css_injection: A CSS string to inject into the website before
                capturing the image.
            user_agent: The User Agent to use when capturing the screenshot.
            export_format: The image format to use for the screenshot.
                Can be jpeg or png, and defaults to jpeg.

        Returns:
            WebsiteScreenshotResponse representing API call response.
        """
        self._validate_params(**locals())
        return self._service_request(
            _response_class=WebsiteScreenshotResponse,
            url=url,
            capture_full_page=capture_full_page,
            width=width,
            height=height,
            delay=delay,
            css_injection=css_injection,
            user_agent=user_agent,
            export_format=export_format
        )
