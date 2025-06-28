import pytest
from bookland.domain.value_objects.email_vo import Email


def test_valid_email_should_be_accepted():
    email = Email("user@example.com")

    assert email.value == "user@example.com"


def test_invalid_email_should_raise_value_error():
    with pytest.raises(ValueError):
        Email("invalid-email")


def test_emails_with_same_value_should_be_equal():
    email1 = Email("user@example.com")
    email2 = Email("user@example.com")

    assert email1 == email2


def test_str_should_return_email_value():
    email = Email("user@example.com")
    assert str(email) == "user@example.com"
