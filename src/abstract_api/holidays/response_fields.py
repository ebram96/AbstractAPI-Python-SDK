"""Response fields of holidays service endpoint."""


# The response body does not contain 'holidays' field. This is just to be
# able to initialize and use the response in a Pythonic way and conform with
# other parts of the code.
RESPONSE_FIELDS: frozenset[str] = frozenset({
    "holidays"
})
