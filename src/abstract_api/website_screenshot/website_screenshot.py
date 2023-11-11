from ..core.bases import BaseService
from .website_screenshot_response import WebsiteScreenshotResponse


class WebsiteScreenshot(BaseService[WebsiteScreenshotResponse]):
    """AbstractAPI website screenshot service.

    Used to request a screenshot of a webpage in a given URL.

    Attributes:
        _subdomain: Website screenshot service subdomain.
    """
    _subdomain: str = "screenshot"

    def capture(
        self,
        url: str,
        capture_full_page: bool | None = None,
        width: int | None = None,
        height: int | None = None,
        delay: int | None = None,
        css_injection: str | None = None,
        user_agent: str | None = None,
        export_format: str | None = None
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
