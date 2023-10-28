from typing import TYPE_CHECKING

import requests

from abstract_api.bases import JSONResponse

from .response_fields.categories import CATEGORIES_RESPONSE_FIELDS


class Category:
    """Country entity in VAT categories response."""

    def __init__(
        self,
        country_code: str,
        rate: str,
        category: str,
        description: str
    ) -> None:
        """Initializes a new Country."""
        self._country_code = country_code
        self._rate = rate
        self._category = category
        self._description = description

    @property
    def country_code(self) -> str:
        """Country’s ISO 3166-1 alpha-2 code.

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

    def __init__(self, response: requests.models.Response) -> None:
        """Initializes a new VATValidationResponse."""
        super().__init__(response)
        self._response_fields = CATEGORIES_RESPONSE_FIELDS

        if self.meta.body_json:
            categories = []
            for c in self.meta.body_json:
                if TYPE_CHECKING:
                    assert isinstance(c, dict)
                categories.append(Category(**c))
            self._categories = frozenset(categories)

    @property
    def categories(self) -> frozenset[Category] | None:
        """The returned VAT categories."""
        return self._get_response_field("categories")
