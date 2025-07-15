import pytest

from bookland.domain.value_objects import Nickname
from bookland.domain.exceptions import InvalidNicknameException


def test_valid_nickname_should_be_accepted():
    nickname = Nickname("user_test")

    assert nickname.value == "user_test"


def test_invalid_nickname_should_raise_invalid_nickname_exception():
    with pytest.raises(InvalidNicknameException):
        Nickname("user-Test")


def test_nickname_not_string_should_raise_invalid_nickname_exception():
    with pytest.raises(InvalidNicknameException):
        Nickname(4)


def test_nicknames_with_same_value_should_be_equal():
    nickname1 = Nickname("user_test")
    nickname2 = Nickname("user_test")

    assert nickname1 == nickname2


def test_str_should_return_nickname_value():
    nickname = Nickname("user_test")

    assert str(nickname) == "user_test"
