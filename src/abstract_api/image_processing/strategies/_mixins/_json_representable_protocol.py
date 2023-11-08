from typing import Protocol


class JSONRepresentableProtocol(Protocol):
    """MyPy protocol to indicate a class having .json() method."""
    def json(self) -> dict[str, int | str]:  # noqa: D102
        ...
