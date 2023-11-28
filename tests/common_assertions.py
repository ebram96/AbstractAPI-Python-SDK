import pytest


def assert_unchangeable_fields(instance, fields):
    for field in fields:
        with pytest.raises(AttributeError):
            setattr(instance, field, "changed")
