from .abstract_api_exception import AbstractAPIException


class ClientRequestError(AbstractAPIException):
    """Raised when there's a problem on our side before making API request."""
