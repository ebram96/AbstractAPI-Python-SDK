from abstract_api.core.mixins import NestedEntitiesMixin


class NestedEntity:
    def __init__(self, some_field):
        self._some_field = some_field

    @property
    def some_field(self):
        return self._some_field


class ConcreteExample(NestedEntitiesMixin):
    _nested_entities = {"nested_entity": NestedEntity}


class TestNestedEntitiesMixin:
    def test__init_response_field(self):
        instance = ConcreteExample()

        instance._init_response_field(
            "nested_entity",
            {"some_field": "value"}
        )

        assert isinstance(instance._nested_entity, NestedEntity)
