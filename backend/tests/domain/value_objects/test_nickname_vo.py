import pytest
from bookland.domain.value_objects.nickname_vo import Nickname


def test_valid_nickname_should_be_accepted():
    nickname = Nickname("user_test")

    assert nickname.value == "user_test"


def test_invalid_nickname_should_raise_value_error():
    with pytest.raises(ValueError):
        Nickname("user-Test")

def test_nicknames_with_same_value_should_be_equal():
    nickname1 = Nickname("user_test")
    nickname2 = Nickname("user_test")

    assert nickname1 == nickname2


def test_str_should_return_nickname_value():
    nickname = Nickname("user_test")
    assert str(nickname) == "user_test"
