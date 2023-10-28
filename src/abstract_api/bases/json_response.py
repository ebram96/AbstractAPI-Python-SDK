from typing import Any, ClassVar, Type, Union

import requests

from ._base_response import BaseResponse, BaseResponseMeta


class JSONResponseMeta(BaseResponseMeta):
    """TODO."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initialize a new JSONResponseMeta."""
        super().__init__(response)
        try:
            self._body_json = response.json()
        except:  # noqa: E722
            self._body_json = None

    @property
    def body_json(self) -> Union[dict[str, Any], list[dict[str, Any]]]:
        """JSON representation of response body returned from API request."""
        return self._body_json


class JSONResponse(BaseResponse):
    """TODO."""
    _response_fields: frozenset[str]
    _meta_class: ClassVar[Type] = JSONResponseMeta
    meta: JSONResponseMeta

    def _get_response_field(self, attr_name: str) -> Any:
        """Gets the value of a field that was returned in response.

        Raises:
            AttributeError: When trying to get a value of a field that was
                not returned in response.
        """
        if attr_name not in self._response_fields:
            raise AttributeError(
                f"Field '{attr_name}' was not returned in API response. "
            )

        return getattr(self, f"_{attr_name}")
