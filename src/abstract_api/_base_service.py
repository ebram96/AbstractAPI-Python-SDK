from abc import ABC


class _BaseService(ABC):
    """Base class for all AbstractAPI service classes.

    Attributes:
        __base_url: Base AbstractAPI services URL.
            Used to generate service-specific API URL.
        _subdomain: A service's subdomain.
            Used with __base_url to generate service-specific API URL.
        _api_key: API key to be used to authenticate with AbstractAPI.
    """
    __base_url: str = "https://{subdomain}.abstractapi.com/v1/"
    _subdomain: str = None
    _api_key: str = None

    def __init__(self, api_key: str) -> None:
        """Constructs a _BaseService.

        Args:
            api_key: API key to be used to authenticate with AbstractAPI.
        """
        self._api_key = api_key

    @property
    def _service_url(self):
        """Builds and returns an API URL for a service using its subdomain

        Returns:
            A str that can be used to make API calls to a service.
        """
        return self.__base_url.format(subdomain=self._subdomain)
