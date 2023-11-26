import pytest
import requests

from abstract_api.core.bases._base_response import (
    BaseResponse,
    BaseResponseMeta
)


@pytest.fixture
def response(mocker):
    response = mocker.MagicMock()
    response.status_code = requests.codes.OK
    response.content = b'{"example": "example-value"}'
    return response


class TestBaseResponseMeta:
    def test_instance(self, response):
        meta = BaseResponseMeta(response)
        assert meta.http_status == response.status_code
        assert meta.body == response.content


class TestBaseResponse:
    def test_instance(self, response, mocker):
        mocker.patch.object(
            BaseResponse, "_meta_class", BaseResponseMeta, create=True
        )
        base_response = BaseResponse(response)
        assert isinstance(base_response.meta, BaseResponseMeta)
