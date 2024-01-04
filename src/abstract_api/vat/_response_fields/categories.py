"""Response fields of VAT categories service endpoint."""


# The response body does not contain 'categories' field. This is just to be
# able to initialize and use the response in a Pythonic way and conform with
# other parts of the code.
CATEGORIES_RESPONSE_FIELDS: frozenset[str] = frozenset({
    "categories"
})
