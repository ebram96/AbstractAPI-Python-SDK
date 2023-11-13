from typing import Any

from abstract_api.core.exceptions import ClientRequestError


def between(
    param: str,
    value: Any,
    start: int | float,
    end: int | float
) -> None:
    """Validate a value to be in a range (inclusive).

    Args:
        param: Parameter name.
        value: Parameter value.
        start: Beginning of the range.
        end: End of the range.

    Raises:
        ClientRequestError if the given value is not in the range (inclusive).
    """
    if value is None:
        return

    if not (start <= value <= end):
        raise ClientRequestError(
            f"'{param}' must be in range from {start} to {end} (inclusive)"
        )


def greater_or_equal(
    param: str,
    value: Any,
    threshold: int | float
) -> None:
    """Validate a value to be in a range (inclusive).

    Args:
        param: Parameter name.
        value: Parameter value.
        threshold: Threshold that the given value must be greater than.

    Raises:
        ClientRequestError if the given value is less than given threshold.
    """
    if value is None:
        return

    if value < threshold:
        raise ClientRequestError(
            f"'{param}' must be greater than or equal to {threshold}"
        )
