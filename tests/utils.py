import json
from io import BytesIO

import requests


def generate_response(data, status_code=requests.codes.OK):
    """Generates a response with the given data and status code.

    The default value for status_code if it is omitted is OK.
    """
    r = requests.Response()
    if isinstance(data, (dict, list)):
        data = json.dumps(data)
    if isinstance(data, str):
        data = BytesIO(data.encode())
    elif isinstance(data, bytes):
        data = BytesIO(data)
    r.raw = data
    r.status_code = status_code
    return r
