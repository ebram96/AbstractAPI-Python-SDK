import json

import pytest
import requests

from abstract_api.core.exceptions import APIRequestError
from tests.utils import generate_response


class TestAPIRequestError:
    @pytest.fixture
    def error_sample(self):
        return {
            "error": {
                "message": "A validation error occurred.",
                "code": "validation_error",
                "details": {
                    "api_key": ["This is a required argument."]
                }
            }
        }

    @pytest.fixture
    def raised_error_message(self):
        return "API request failed (HTTP status: 401). "\
               "A validation error occurred. Details: "\
               "{'api_key': ['This is a required argument.']}"

    def test__get_error_details(self, error_sample):
        assert APIRequestError._get_error_details(error_sample) == error_sample["error"]

    def test__build_raised_error_message(self, error_sample, raised_error_message):
        error_details = APIRequestError._get_error_details(error_sample)
        error_message = APIRequestError._build_raised_error_message(
            error_details=error_details,
            http_status=requests.codes.UNAUTHORIZED
        )
        assert error_message == raised_error_message

    def test_initialization(self, error_sample, raised_error_message):
        error_details = APIRequestError._get_error_details(error_sample)
        kwargs = error_details | {
            "http_status": requests.codes.UNAUTHORIZED,
            "body": json.dumps(error_sample).encode()
        }
        instance = APIRequestError(
            raised_error_message=raised_error_message,
            **kwargs
        )
        for key in kwargs.keys():
            assert getattr(instance, key) == kwargs[key]

    def test_raise_from_response(self, error_sample, raised_error_message):
        response = generate_response(error_sample, requests.codes.UNAUTHORIZED)
        with pytest.raises(APIRequestError) as exc:
            APIRequestError.raise_from_response(response)
        assert str(exc.value) == raised_error_message
