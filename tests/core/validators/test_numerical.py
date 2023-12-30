import pytest

from abstract_api.core.exceptions import ClientRequestError
from abstract_api.core.validators.numerical import between, greater_or_equal


class TestNumerical:
    def test_between(self):
        start = 1
        end = 10
        with pytest.raises(ClientRequestError):
            between("example", start - 1, start, end)
            between("example", start - 0.01, start, end)
            between("example", start, start, end + 1)
            between("example", start, start, end + 0.01)

    def test_greater_or_equal(self):
        with pytest.raises(ClientRequestError):
            threshold = 10
            greater_or_equal("example", threshold - 1, threshold)
            greater_or_equal("example", threshold - 0.1, threshold)
