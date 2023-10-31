from abstract_api.bases import BaseService
from abstract_api.exceptions import ResponseParseError

from .web_scraping_response import WebScrapingResponse


class WebScraping(BaseService):
    """AbstractAPI web scraping service.

    Used to extract data from a given URL.

    Attributes:
        _subdomain: Web scraping service subdomain.
    """
    _subdomain: str = "scrape"

    def scrape(
        self,
        url: str,
        render_js: bool | None = None,
        block_ads: bool | None = None,
        proxy_country: str | None = None
    ) -> WebScrapingResponse:
        """Extracts data from the given URL.

        Args:
            url: The URL to extract the data from. Note that this parameter
                should include the full HTTP Protocol (http:// or https://).
                If your URL has parameters, you should encode it.
                For example the & character would be encoded to %26.
            render_js: If True the request will render Javascript on the
                target site. Note that Javascript is rendered via a Google
                Chrome headless browser. Defaults to False.
            block_ads: If True the request will block any advertisements it
                can identify on the target site. Defaults to False.
            proxy_country: The country to make the request from.
                The country should be submitted in the two letter,
                ISO 3166-1 alpha-2 code.

        Returns:
            WebScrapingResponse representing API call response.
        """
        response = self._service_request(
            url=url,
            render_js=render_js,
            block_ads=block_ads,
            proxy_country=proxy_country
        )

        try:
            web_scraping_response = WebScrapingResponse(response=response)
        except Exception as e:
            raise ResponseParseError(
                "Failed to parse response as WebScrapingResponse"
            ) from e

        return web_scraping_response
