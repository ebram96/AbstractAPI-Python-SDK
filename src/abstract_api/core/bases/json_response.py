from typing import TYPE_CHECKING, Any, ClassVar, Type

import requests

from ._base_response import BaseResponse, BaseResponseMeta


class JSONResponseMeta(BaseResponseMeta):
    """Metadata about a JSON-based API response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initialize a new JSONResponseMeta."""
        super().__init__(response)
        try:
            self._body_json = response.json()
        except:  # noqa: E722
            self._body_json = None

    @property
    def body_json(self) -> dict[str, Any] | list[dict[str, Any]]:
        """JSON representation of response body returned from API request."""
        return self._body_json


class JSONResponse(BaseResponse):
    """JSON-based API response."""
    _response_fields: frozenset[str]
    _meta_class: ClassVar[Type[JSONResponseMeta]] = JSONResponseMeta
    meta: JSONResponseMeta

    def _init_response_field(self, field: str, value: Any) -> None:
        """Sets a response field's value during instance initialization.

        This should be used in/as a part of __init__ method.

        Args:
            field: Field name.
            value: Value to be set. The value is parsed to a nested entity
                if the field is a nested entity.
        """
        setattr(self, f"_{field}", value)

    def __init__(
        self,
        response: requests.models.Response,
        response_fields: frozenset[str],
        list_response: bool = False
    ) -> None:
        """Initialize a new JSONResponse."""
        super().__init__(response)
        self._response_fields = response_fields

        if self.meta.body_json is None:
            return

        if TYPE_CHECKING:
            assert isinstance(self.meta.body_json, dict)

        not_in_response = object()
        for field in response_fields:
            value = (
                self.meta.body_json.get(field, not_in_response)
                if not list_response
                else self.meta.body_json
            )
            # Initialize property only if field was returned
            if value is not not_in_response:
                self._init_response_field(field, value)

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
