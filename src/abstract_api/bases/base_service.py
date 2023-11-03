from abc import ABC
from io import BytesIO
from typing import Any, Final

import requests
from requests import codes

from abstract_api.exceptions import APIRequestError, ClientRequestError


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
        _method: str = "GET",
        _body: dict[str, Any] | None = None,
        _files: dict[str, BytesIO] | None = None,
        _action: str = "",
        **params
    ) -> requests.models.Response:
        """Makes the HTTP call to Abstract API service endpoint.

        Args:
            _method: HTTP method to use.
            _body: Request body.
            _files: Files to be attached to the request body (uploading files).
            _action: Action to be performed using the service.
                Only for services that have it (i.e. VAT).
            params: The URL parameter that should be used when calling the API
                endpoints.

        Returns:
            AbstractAPI's response.
        """
        if _method.lower() not in ["get", "post"]:
            raise ClientRequestError(
                f"Invalid or not allowed HTTP method '{_method}'"
            )

        request_kwargs: dict[str, Any] = {
            "method": _method,
            "url": self._service_url(_action)
        }

        _method = _method.lower()
        if _method == "get":
            request_kwargs["params"] = {"api_key": self._api_key} | params
        else:
            if _files:
                request_kwargs["files"] = _files
            if _body:
                request_kwargs["json"] = _body

        response = requests.request(**request_kwargs)

        if response.status_code not in [codes.OK, codes.NO_CONTENT]:
            APIRequestError.raise_from_response(response)
        return response
