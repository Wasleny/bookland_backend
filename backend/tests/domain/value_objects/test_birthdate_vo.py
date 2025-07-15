import pytest
from datetime import date

from bookland.domain.value_objects import BirthDate
from bookland.domain.exceptions import InvalidBirthDateException


def test_valid_date_should_be_accepted():
    birthdate = BirthDate(date(2002, 6, 20))

    assert birthdate.value == date(2002, 6, 20)


def test_invalid_date_should_be_raise_invalid_birthdate_exception():
    with pytest.raises(InvalidBirthDateException):
        BirthDate(date(2026, 6, 20))


def test_age_under_twelve_should_be_raise_invalid_birthdate_exception():
    with pytest.raises(InvalidBirthDateException):
        BirthDate(date(2014, 6, 20))


def test_age_over_one_hundred_and_thirty_should_be_raise_invalid_birthdate_exception():
    with pytest.raises(InvalidBirthDateException):
        BirthDate(date(1894, 6, 20))


def test_age_should_return_right_age():
    birthdate1 = BirthDate(date(2002, 4, 29))
    birthdate2 = BirthDate(date(2002, 8, 29))

    assert birthdate1.age() == 23
    assert birthdate2.age() == 22
