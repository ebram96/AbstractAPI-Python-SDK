import pytest


def assert_unchangeable_fields(instance, fields, ignore=None):
    if ignore is None:
        ignore = []

    for field in fields:
        if field in ignore:
            continue
        with pytest.raises(AttributeError):
            setattr(instance, field, "changed")


def assert_response_fields(response, fields, sample, mocker, ignore=None):
    if ignore is None:
        ignore = []

    mocked__get_response_field = mocker.patch.object(
        response,
        "_get_response_field",
        wraps=response._get_response_field
    )
    for field in fields:
        if field in ignore:
            continue
        assert getattr(response, field) == sample[field]
        mocked__get_response_field.assert_called_with(field)
    assert mocked__get_response_field.call_count == len(fields) - len(ignore)
    assert_unchangeable_fields(response, fields, ignore)
