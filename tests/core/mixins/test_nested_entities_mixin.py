from abstract_api.core.bases import JSONResponse
from abstract_api.core.mixins import NestedEntitiesMixin
from tests.utils import generate_response


class NestedEntity:
    def __init__(self, some_field):
        self._some_field = some_field

    @property
    def some_field(self):
        return self._some_field


class ConcreteExample(NestedEntitiesMixin, JSONResponse):
    _nested_entities = {"nested_entity": NestedEntity}


class TestNestedEntitiesMixin:
    def test__init_response_field(self):
        response = generate_response({"nested_entity": {"some_field": "value"}})

        instance = ConcreteExample(
            response, response_fields=frozenset(["nested_entity"])
        )

        assert isinstance(instance._nested_entity, NestedEntity)
