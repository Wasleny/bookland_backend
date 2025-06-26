import pytest
from datetime import date
from bookland.domain.value_objects.birthday_vo import Birthday


def test_valid_date_should_be_accepted():
    birthday = Birthday(date(2025, 6, 20))

    assert birthday.value == date(2025, 6, 20)


def test_invalid_date_should_be_raise_type_error():
    with pytest.raises(ValueError):
        Birthday(date(2026, 6, 20))


def test_age_should_return_right_age():
    birthday1 = Birthday(date(2002, 4, 29))
    birthday2 = Birthday(date(2002, 8, 29))

    assert birthday1.age() == 23
    assert birthday2.age() == 22
