import os
from functools import lru_cache
from io import BytesIO
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Final,
    Generic,
    Optional,
    Type,
    TypeVar
)

import requests
from requests import codes

from ..exceptions import (
    APIRequestError,
    ClientRequestError,
    ResponseParseError
)

if TYPE_CHECKING:
    from ._base_response import BaseResponse
BaseResponseT = TypeVar("BaseResponseT", bound="BaseResponse")


class BaseService(Generic[BaseResponseT]):
    """Base class for all AbstractAPI service classes.

    Attributes:
        __base_url: Base AbstractAPI services URL.
            Used to generate service-specific API URL.
        _subdomain: A service's subdomain.
            Used with __base_url to generate service-specific API URL.
        _api_key: API key to be used to authenticate with AbstractAPI.
        _service_name_env_var: Service name that should be used to read API key
            from environment variables.
    """
    __base_url: Final[str] = "https://{subdomain}.abstractapi.com/v1/"
    _subdomain: str
    _service_name_env_var: ClassVar[str]

    @classmethod
    def _read_api_key_from_env(cls) -> Optional[str]:
        """Reads service API key from environment variables.

        API key exposed as an environment variable must be exposed using a
        variable name with the pattern:
        ABSTRACTAPI_{SERVICE_NAME}_API_KEY
        Where SERVICE_NAME is the service name that the API key is for.
        (service_name must be uppercase.)

        Returns: API key read from environment variable.
        """
        pattern = "ABSTRACTAPI_{service_name}_API_KEY"
        return os.environ.get(
            pattern.format(service_name=cls._service_name_env_var)
        )

    def __init__(self, api_key: Optional[str] = None) -> None:
        """Constructs a BaseService.

        Args:
            api_key: API key to be used to authenticate with AbstractAPI.
        """
        api_key = api_key or self._read_api_key_from_env()
        if api_key is None:
            raise ValueError(
                "API key was not provided nor exposed as an"
                " environment variable"
            )
        self._api_key: str = api_key

    @lru_cache(maxsize=5)
    def __service_url(self, action: str = "") -> str:
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
        _response_class: Type[BaseResponseT],
        _response_class_kwargs: Optional[dict[str, Any]] = None,
        _method: str = "GET",
        _body: Optional[dict[str, Any]] = None,
        _files: Optional[dict[str, BytesIO]] = None,
        _action: str = "",
        **params
    ) -> BaseResponseT:
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
            Parsed AbstractAPI's response.
        """
        # Prepare HTTP method
        _method = _method.upper()
        if _method not in ["GET", "POST"]:
            raise ClientRequestError(
                f"Invalid or not allowed HTTP method '{_method}'"
            )

        # Build request kwargs
        request_kwargs: dict[str, Any] = {
            "method": _method,
            "url": self.__service_url(_action)
        }
        if _method == "GET":
            request_kwargs["params"] = {"api_key": self._api_key} | {
                # Ignore all None parameters, no need to transfer them over
                # the network call.
                param: value
                for param, value in params.items()
                if value is not None
            }
        else:
            if _files is not None:
                request_kwargs["files"] = _files
            if _body is not None:
                request_kwargs["json"] = _body

        # Make call
        response = requests.request(**request_kwargs)

        # Ensure accepted response
        if response.status_code not in [codes.OK, codes.NO_CONTENT]:
            APIRequestError.raise_from_response(response)

        # Parse response
        if _response_class_kwargs is None:
            _response_class_kwargs = {}

        try:
            parsed_response = _response_class(
                response=response, **_response_class_kwargs
            )
        except Exception as e:
            raise ResponseParseError(
                f"Failed to parse response as {_response_class.__name__}"
            ) from e

        return parsed_response
