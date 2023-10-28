from abc import ABC
from typing import Final

import requests
from requests import codes

from abstract_api.exceptions import APIRequestError


class BaseService(ABC):
    """Base class for all AbstractAPI service classes.

    Attributes:
        __base_url: Base AbstractAPI services URL.
            Used to generate service-specific API URL.
        _subdomain: A service's subdomain.
            Used with __base_url to generate service-specific API URL.
        _api_key: API key to be used to authenticate with AbstractAPI.
    """
    __base_url: Final[str] = "https://{subdomain}.abstractapi.com/v1/"
    _subdomain: str

    def __init__(self, api_key: str) -> None:
        """Constructs a BaseService.

        Args:
            api_key: API key to be used to authenticate with AbstractAPI.
        """
        self._api_key = api_key

    def _service_url(self, action: str = "") -> str:
        """Builds and returns an API URL for a service using its subdomain.

        Args:
            action: Action to be performed using the service.
                Only for services that have it (i.e. VAT).

        Returns:
            A str that can be used to make API calls to a service.
        """
        return self.__base_url.format(subdomain=self._subdomain) + action

    def _service_request(
        self,
        action: str = "",
        **params
    ) -> requests.models.Response:
        """Makes the HTTP call to Abstract API service endpoint.

        Args:
            action: Action to be performed using the service.
                Only for services that have it (i.e. VAT).
            params: The URL parameter that should be used when calling the API
                endpoints.

        Returns:
            AbstractAPI's response.
        """
        response = requests.get(
            self._service_url(action),
            params={"api_key": self._api_key} | params
        )
        if response.status_code not in [codes.OK, codes.NO_CONTENT]:
            APIRequestError.raise_from_response(response)
        return response
