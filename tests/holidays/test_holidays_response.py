import pytest

from abstract_api.core.bases import JSONResponse
from abstract_api.holidays import HolidaysResponse
from abstract_api.holidays._response_fields import RESPONSE_FIELDS
from abstract_api.holidays.holidays_response import Holiday
from tests.utils import generate_response


class TestHolidaysResponse:
    def test__init_response_field(self, holidays_sample):
        # Given
        response = generate_response(holidays_sample)
        instance = HolidaysResponse(response)

        # When
        instance._init_response_field("holidays", holidays_sample)

        # Then
        assert isinstance(instance.holidays, tuple)
        assert len(instance.holidays) == len(holidays_sample)
        for h in instance.holidays:
            assert isinstance(h, Holiday)

    def test_initialization_super_call(self, blank_response, mocker):
        # Given
        mocked_init = mocker.patch.object(
            JSONResponse,
            "__init__",
            wraps=JSONResponse.__init__
        )
        mocked_init.return_value = None

        # When
        HolidaysResponse(blank_response)

        # Then
        mocked_init.assert_called_once_with(
            blank_response, RESPONSE_FIELDS, list_response=True
        )

    def test_initialization(self, holidays_sample, mocker):
        # Given
        response = generate_response(holidays_sample)

        # When
        instance = HolidaysResponse(response)

        # Then
        mocked__get_response_field = mocker.patch.object(
            instance,
            "_get_response_field",
            wraps=instance._get_response_field
        )
        assert len(instance.holidays) == len(holidays_sample)
        mocked__get_response_field.assert_called_with("holidays")
        assert mocked__get_response_field.call_count == 1
        with pytest.raises(AttributeError):
            setattr(instance, "holidays", "changed")
