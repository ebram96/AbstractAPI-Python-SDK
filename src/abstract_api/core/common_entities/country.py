class Country:
    """Country entity."""

    def __init__(self, code: str, name: str) -> None:
        """Initializes a new Country."""
        self._code = code
        self._name = name

    @property
    def code(self) -> str | None:
        """The country's two-letter ISO 3166-1 alpha-2 code."""
        return self._code

    @property
    def name(self) -> str | None:
        """The name of the country."""
        return self._name
