from typing import Any, ClassVar, Type


class NestedEntitiesMixin:
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
        setattr(
            self,
            f"_{field}",
            value if field not in self._nested_entities
            else self._nested_entities[field](**value)
        )
