import pytest

from bookland.domain.value_objects import Isbn
from bookland.domain.exceptions import InvalidIsbnException


def test_valid_isbn10_should_be_accepted():
    isbn = Isbn("0-306-40615-2")

    assert isbn.value == "0-306-40615-2"


def test_valid_isbn10_with_check_digit_X():
    isbn = Isbn("0-8044-2957-X")

    assert isbn.value == "0-8044-2957-X"


def test_invalid_isbn10_should_raise_invalid_isbn_exception():
    with pytest.raises(InvalidIsbnException):
        Isbn("0-306-40615-5")


def test_valid_isbn13_should_be_accepted():
    isbn = Isbn("978-0-306-40615-7")

    assert isbn.value == "978-0-306-40615-7"


def test_invalid_isbn13_should_raise_invalid_isbn_exception():
    with pytest.raises(InvalidIsbnException):
        Isbn("978-0-306-40615-3")


def test_isbns_with_same_value_should_be_equal():
    isbn1 = Isbn("978-0-306-40615-7")
    isbn2 = Isbn("978-0-306-40615-7")

    assert isbn1 == isbn2


def test_str_should_return_isbn_value():
    isbn = Isbn("978-0-306-40615-7")

    assert str(isbn) == "978-0-306-40615-7"
