import pytest

from bookland.domain.value_objects import Name
from bookland.domain.exceptions import InvalidNameException


def test_valid_name_should_be_accepted():
    name = Name("User")

    assert name.value == "User"


def test_invalid_name_should_raise_invalid_name_exception():
    with pytest.raises(InvalidNameException):
        Name("User4")


def test_name_not_string_should_raise_invalid_name_exception():
    with pytest.raises(InvalidNameException):
        Name(4)


def test_names_with_same_value_should_be_equal():
    name1 = Name("User")
    name2 = Name("User")

    assert name1 == name2


def test_str_should_return_name_value():
    name = Name("User")

    assert str(name) == "User"
