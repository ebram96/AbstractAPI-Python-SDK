import os
from io import BytesIO

import pytest
import requests

from abstract_api.core.bases import BaseService
from abstract_api.core.bases._base_response import (
    BaseResponse,
    BaseResponseMeta
)
from abstract_api.core.exceptions import (
    APIRequestError,
    ClientRequestError,
    ResponseParseError
)


class _ChildService(BaseService):
    _subdomain = "dummy"
    _service_name_env_var = "DUMMY"


class _ChildServiceResponse(BaseResponse):
    _meta_class = BaseResponseMeta


class TestBaseService:
    @pytest.fixture
    def child_service(self):
        return _ChildService("no-api-key")

    @pytest.fixture
    def child_service_url(self, child_service):
        return child_service._BaseService__service_url()

    def test__read_api_key_from_env(self, child_service, mocker):
        env_key = "ABSTRACTAPI_{service_name}_API_KEY".format(
            service_name=child_service._service_name_env_var
        )
        value = "some-api-key"
        mocker.patch.dict(os.environ, {env_key: value})
        assert child_service._read_api_key_from_env() == value

    def test_init_without_api_key(self, mocker):
        mocked_read = mocker.patch.object(
            _ChildService,
            "_read_api_key_from_env",
            wraps=_ChildService._read_api_key_from_env
        )

        with pytest.raises(ValueError):
            _ChildService()
        mocked_read.assert_called_once()

    def test___service_url(self, base_url, mocker):
        service = "test"
        action = "testing"
        mocker.patch.object(BaseService, "_subdomain", service, create=True)
        assert BaseService._BaseService__service_url(self=BaseService) == base_url.format(subdomain=service)
        assert BaseService._BaseService__service_url(self=BaseService, action=action) == base_url.format(subdomain=service) + action

    @pytest.mark.parametrize("method", ["PUT", "PATCH", "DELETE"])
    def test__service_request_with_invalid_method(
        self, method, child_service,
    ):
        with pytest.raises(ClientRequestError):
            child_service._service_request(
                _response_class=_ChildServiceResponse,
                _method=method
            )

    def test__service_request_get(
        self,
        child_service,
        child_service_url,
        requests_mock,
        mocker
    ):
        service_params = {"param1": "value", "param2": None}
        requests_mock.get(child_service_url, status_code=requests.codes.OK)
        mocked_request = mocker.patch.object(
            requests, "request", wraps=requests.request
        )

        child_service._service_request(
            _ChildServiceResponse, **service_params
        )

        mocked_request.assert_called_once_with(
            method="GET",
            url=child_service_url,
            params={
                "api_key": child_service._api_key,
                "param1": service_params["param1"]
            }
        )

    @pytest.mark.parametrize(
        ["body", "files"],
        [
            ({"key1": "value", "key2": None}, {"file": BytesIO(b"some-content")}),
            (None, {"file": BytesIO(b"some-content")}),
            ({"key1": "value", "key2": None}, None)
        ]
    )
    def test__service_request_post(
        self,
        body,
        files,
        child_service,
        child_service_url,
        requests_mock,
        mocker
    ):
        requests_mock.post(child_service_url, content=b"")
        mocked_request = mocker.patch.object(
            requests, "request", wraps=requests.request
        )

        request_kwargs = {
            "_response_class": _ChildServiceResponse,
            "_method": "POST",
        }
        if files is not None:
            request_kwargs["_files"] = files
        if body is not None:
            request_kwargs["_body"] = body
        child_service._service_request(**request_kwargs)

        call_kwargs = {"method": "POST", "url": child_service_url}
        if files is not None:
            call_kwargs["files"] = files
        if body is not None:
            call_kwargs["json"] = body
        mocked_request.assert_called_once_with(**call_kwargs)

    @pytest.mark.parametrize(
        "status_code", [201, 202, 203, 400, 403, 405]
    )
    def test__service_request_unaccepted_status_code(
        self,
        status_code,
        child_service,
        child_service_url,
        requests_mock
    ):
        requests_mock.get(
            child_service_url, status_code=status_code
        )
        with pytest.raises(APIRequestError):
            child_service._service_request(_ChildServiceResponse)

    def test__service_request_parsing_error(
        self,
        child_service,
        ok_response,
        mocker
    ):
        mocked_request = mocker.patch.object(requests, "request")
        mocked_request.return_value = ok_response

        with pytest.raises(ResponseParseError):
            child_service._service_request(
                _ChildServiceResponse,
                _response_class_kwargs={"key": "unexpected"}
            )
