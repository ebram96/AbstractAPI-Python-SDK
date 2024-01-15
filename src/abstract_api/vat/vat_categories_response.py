from functools import cached_property
from typing import Any, Optional

import requests

from ..core.bases import JSONResponse
from ._response_fields.categories import CATEGORIES_RESPONSE_FIELDS


class Category:
    """Country entity in VAT categories response."""

    def __init__(
        self,
        country_code: str,
        rate: str,
        category: str,
        description: str
    ) -> None:
        """Initializes a new Category."""
        self._country_code = country_code
        self._rate = rate
        self._category = category
        self._description = description

    @property
    def country_code(self) -> str:
        """Country's ISO 3166-1 alpha-2 code.

        The code of the country in which the transaction takes place, which
        is returned from the request.
        """
        return self._country_code

    @property
    def rate(self) -> str:
        """The VAT rate for this specific category."""
        return self._rate

    @property
    def category(self) -> str:
        """The name of the category."""
        return self._category

    @property
    def description(self) -> str:
        """A description about the category."""
        return self._description


class VATCategoriesResponse(JSONResponse):
    """VAT categories service response."""

    def _init_response_field(
        self,
        field: str,
        value: list[dict[str, Any]]
    ) -> None:
        """Sets a response field's value during instance initialization.

        This should be used in/as a part of __init__ method.

        Args:
            field: Field name.
            value: Value to be set. The value is parsed to a nested entity
                if the field is a nested entity.
        """
        categories: list[Category] = []
        for c in value:
            categories.append(Category(**c))
        super()._init_response_field(field, tuple(categories))

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new VATCategoriesResponse."""
        super().__init__(
            response,
            CATEGORIES_RESPONSE_FIELDS,
            list_response=True
        )

    @cached_property
    def categories(self) -> Optional[tuple[Category, ...]]:
        """The returned VAT categories."""
        return self._get_response_field("categories")
