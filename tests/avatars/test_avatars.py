import pytest
import requests

from abstract_api import Avatars
from abstract_api.avatars import AvatarsResponse
from abstract_api.core.exceptions import ClientRequestError


class TestAvatars:
    """Avatars service tests."""
    @pytest.fixture
    def service(self) -> Avatars:
        return Avatars("no-api-key")

    @pytest.mark.parametrize(
        ("image_size", "font_size", "char_limit", "image_format"),
        [[0, 0, 0, "jpeg"], [5, 0.05, 0.5, "bmp"], [800, 3, 3, "gif"]]
    )
    def test__validate_params(
        self, service, image_size, font_size, char_limit, image_format, mocker
    ):
        # Given
        mocked__validate_params = mocker.patch.object(
            service,
            "_validate_params",
            wraps=service._validate_params
        )

        # Then
        with pytest.raises(ClientRequestError):
            # When
            service.create("", image_size=image_size)
        assert mocked__validate_params.call_count == 1

        # Then
        with pytest.raises(ClientRequestError):
            # When
            service.create("", font_size=font_size)
        assert mocked__validate_params.call_count == 2

        # Then
        with pytest.raises(ClientRequestError):
            # When
            service.create("", char_limit=char_limit)
        assert mocked__validate_params.call_count == 3

        # Then
        with pytest.raises(ClientRequestError):
            # When
            service.create("", image_format=image_format)
        assert mocked__validate_params.call_count == 4

    def test_create(self, service, base_url, requests_mock):
        # Given
        url = base_url.format(subdomain=Avatars._subdomain)
        content = b'some-john-doe-avatar-content'
        name = "John Doe"
        requests_mock.get(url, content=content)

        # When
        response = service.create(name=name)

        # Then
        assert isinstance(response, AvatarsResponse)
        assert response.content == content
        assert response.meta.body == content
        assert response.meta.http_status == requests.codes.OK
