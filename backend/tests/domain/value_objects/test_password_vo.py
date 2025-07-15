import pytest

from bookland.domain.value_objects import Password
from bookland.domain.exceptions import InvalidPasswordException


def test_valid_email_should_be_accepted():
    password = Password("uSer@1234")

    assert password.value == "uSer@1234"


def test_password_without_lower_letter_should_raise_invalid_password_exception():
    with pytest.raises(InvalidPasswordException):
        Password("USER@1234")


def test_password_without_upper_letter_should_raise_invalid_password_exception():
    with pytest.raises(InvalidPasswordException):
        Password("user@1234")


def test_password_without_digit_should_raise_invalid_password_exception():
    with pytest.raises(InvalidPasswordException):
        Password("uSer@uSer")


def test_password_without_special_character_raise_invalid_password_exception():
    with pytest.raises(InvalidPasswordException):
        Password("uSer1234")


def test_password_with_size_smaller_than_eight_raise_invalid_password_exception():
    with pytest.raises(InvalidPasswordException):
        Password("uSer123")


def test_passwords_with_same_value_should_be_equal():
    password1 = Password("uSer@1234")
    password2 = Password("uSer@1234")

    assert password1 == password2


def test_str_should_return_password_value():
    password = Password("uSer@1234")
    assert str(password) == "*" * 8
