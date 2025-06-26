import pytest
from datetime import date
from bookland.domain.value_objects.date_vo import Date


def test_valid_date_should_be_accepted():
    valid_date = Date(date(2025, 6, 20))

    assert valid_date.value == date(2025, 6, 20)


def test_invalid_date_should_be_raise_type_error():
    with pytest.raises(TypeError):
        Date("2025-05-20")


def test_future_date_is_future_returns_true():
    valid_date = Date(date(2200, 6, 22))

    assert valid_date.is_future() == True


def test_dates_with_same_value_should_be_equal():
    date1 = Date(date(2025, 6, 22))
    date2 = Date(date(2025, 6, 22))
    date3 = date(2025, 6, 22)
    date4 = "2025-06-20"

    assert date1 == date2
    assert date1 == date3
    assert date1 == date3
    assert date1 != date4


def test_str_should_return_formatted_date():
    valid_date = Date(date(2025, 6, 20))
    assert str(valid_date) == "2025-06-20"
