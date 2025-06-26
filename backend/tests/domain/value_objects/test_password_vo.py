import pytest
from bookland.domain.value_objects.password_vo import Password


def test_valid_email_should_be_accepted():
    password = Password("user1234")

    assert password.value == "user1234"


def test_invalid_password_should_raise_value_error():
    with pytest.raises(ValueError):
        Password("invalid-password")


def test_passwords_with_same_value_should_be_equal():
    password1 = Password("user1234")
    password2 = Password("user1234")

    assert password1 == password2


def test_str_should_return_password_value():
    password = Password("user1234")
    assert str(password) == "*" * 8