import requests

from abstract_api import WebScraping
from abstract_api.web_scraping import WebScrapingResponse


class TestWebScraping:
    """WebScraping service tests."""
    def test_scrape(self, base_url, requests_mock):
        service = WebScraping("no-api-key")
        website = "https://example.com"
        url = base_url.format(subdomain=WebScraping._subdomain)
        content = b'some-example-web-scraping-content'
        requests_mock.get(url, content=content)

        response = service.scrape(website)

        assert isinstance(response, WebScrapingResponse)
        assert response.content == content
        assert response.meta.body == content
        assert response.meta.http_status == requests.codes.OK
