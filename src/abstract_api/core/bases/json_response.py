from typing import TYPE_CHECKING, Any, ClassVar, Type

import requests

from ._base_response import BaseResponse, BaseResponseMeta


class JSONResponseMeta(BaseResponseMeta):
    """Metadata about a JSON-based API response."""

    def __init__(self, response: requests.models.Response) -> None:
        """Initialize a new JSONResponseMeta."""
        super().__init__(response)
        if response.status_code == requests.codes.NO_CONTENT:
            self._body_json = None
        else:
            self._body_json = response.json()

    @property
    def body_json(self) -> dict[str, Any] | list[dict[str, Any]] | None:
        """JSON representation of response body returned from API request."""
        return self._body_json


class JSONResponse(BaseResponse):
    """JSON-based API response."""
    _response_fields: frozenset[str]
    _meta_class: ClassVar[Type[JSONResponseMeta]] = JSONResponseMeta
    meta: JSONResponseMeta

    def __setattr__(self, key: str, value: Any) -> None:
        """Sets a property only if it is not a response field.

        The main reason for customizing the original method is that we use
        functools.cached_property, and it allows setting a property value after
        it is cached, even if it has no setter.
        """
        response_fields_attr = "_response_fields"
        if key == response_fields_attr:
            if response_fields_attr in self.__dict__:
                raise AttributeError(
                    f"'{response_fields_attr}' should not be changed"
                )
        elif key in self._response_fields:
            raise AttributeError(
                f"value of response field '{key}' should not be changed"
            )
        return super().__setattr__(key, value)

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
        self._response_fields = response_fields  # Must be set first.

        super().__init__(response)

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
