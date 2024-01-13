from typing import Protocol, Union


class JSONRepresentableProtocol(Protocol):
    """MyPy protocol to indicate a class having .json() method."""
    def json(self) -> dict[str, Union[int, str]]:  # noqa: D102
        ...  # pragma: no cover
