from typing import Iterable

from ..exceptions import ClientRequestError


class ResponseFieldsMixin:
    """Response fields mixin.

    For services that support selecting response fields.
    """
    _response_fields: frozenset[str]

    def __init__(
        self,
        *,
        response_fields: Iterable[str] | None = None,
        **kwargs
    ) -> None:
        """Initializes a new instance.

        Args:
            response_fields: Selected response fields.
        """
        super().__init__(**kwargs)
        if response_fields is not None:
            self.response_fields = frozenset(response_fields)

    def _validate_response_fields(
        self,
        response_fields: Iterable[str]
    ) -> None:
        """Validates whether all the given fields are acceptable.

        Args:
            response_fields: Selected response fields.
        """
        for field in response_fields:
            if field not in self.response_fields:
                raise ClientRequestError(
                    f"Field '{field}' is not a valid response field"
                )

    @property
    def response_fields(self) -> frozenset[str]:
        """Gets selected response fields."""
        return self._response_fields

    @response_fields.setter
    def response_fields(self, fields: Iterable[str]) -> None:
        """Sets selected response fields."""
        self._validate_response_fields(fields)
        self._response_fields = frozenset(fields)

    @staticmethod
    def _response_fields_as_param(response_fields: Iterable[str]) -> str:
        """Builds 'fields' URL query parameter.

         Builds a string that contains selected response fields to be used
         as a URL query parameter.

        Args:
            response_fields: Selected response fields.

        Returns:
            Comma-separated string with all selected response fields.
        """
        return ",".join(response_fields)

    def _prepare_selected_fields(
        self,
        fields: Iterable[str] | None = None
    ) -> frozenset[str]:
        """Prepares selected fields to be used in service call.

        Args:
            fields: Selected response fields (optional).

        Returns:
            Valid selected fields as a frozenset.
        """
        if fields:
            self._validate_response_fields(fields)
            return frozenset(fields)

        return self.response_fields
