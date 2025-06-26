import pytest
from bookland.domain.value_objects.name_vo import Name


def test_valid_name_should_be_accepted():
    name = Name("User")

    assert name.value == "User"


def test_invalid_name_should_raise_value_error():
    with pytest.raises(ValueError):
        Name("User4")


def test_names_with_same_value_should_be_equal():
    name1 = Name("User")
    name2 = Name("User")

    assert name1 == name2


def test_str_should_return_name_value():
    name = Name("User")
    assert str(name) == "User"
