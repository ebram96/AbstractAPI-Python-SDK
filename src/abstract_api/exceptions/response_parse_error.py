from .abstract_api_exception import AbstractAPIException


class ResponseParseError(AbstractAPIException):
    """Raised when an attempt to parse a response body fails."""
