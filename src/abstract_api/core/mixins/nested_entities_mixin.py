from typing import TYPE_CHECKING, Any, ClassVar, Protocol, Type


class _ResponseFieldProtocol(Protocol):
    def _init_response_field(self, field: str, value: Any) -> None:
        ...  # pragma: no cover


if TYPE_CHECKING:
    _Base = _ResponseFieldProtocol
else:
    _Base = object


class NestedEntitiesMixin(_Base):
    """Nested entities mixin for responses that have nested entities."""
    _nested_entities: ClassVar[dict[str, Type]]

    def _init_response_field(self, field: str, value: Any) -> None:
        """Sets a response field's value during instance initialization.

        This should be used in/as a part of __init__ method.

        Args:
            field: Field name.
            value: Value to be set. The value is parsed to a nested entity
                if the field is a nested entity.
        """
        if field in self._nested_entities:
            value = self._nested_entities[field](**value)
        super()._init_response_field(field, value)
