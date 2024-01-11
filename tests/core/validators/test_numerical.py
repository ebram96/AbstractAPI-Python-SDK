import pytest

from abstract_api.core.exceptions import ClientRequestError
from abstract_api.core.validators.numerical import between, greater_or_equal


class TestNumerical:
    def test_between(self):
        # Given
        start = 1
        end = 10

        # Then
        with pytest.raises(ClientRequestError):
            # When
            between("example", start - 1, start, end)
            between("example", start - 0.01, start, end)
            between("example", start, start, end + 1)
            between("example", start, start, end + 0.01)

    def test_greater_or_equal(self):
        # Then
        with pytest.raises(ClientRequestError):
            # Given
            threshold = 10
            # When
            greater_or_equal("example", threshold - 1, threshold)
            greater_or_equal("example", threshold - 0.1, threshold)

    def test_greater_or_equal_with_none(self):
        # Given
        value = None
        threshold = 0

        # Then
        # Does not raise exception.
        # If execution continue, an exception will be raised because None can
        # not be compared with '<' operator.
        greater_or_equal("example", value, threshold)
