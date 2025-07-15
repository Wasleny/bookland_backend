import pytest

from bookland.domain.entities import UserBook
from bookland.domain.exceptions import InvalidUserBookException


def test_valid_user_book_should_be_created():
    user_book = UserBook("1", "1", "1", "1")

    assert user_book.id == "1"
    assert user_book.book_id == "1"
    assert user_book.user_id == "1"
    assert user_book.default_bookshelf_id == "1"


def test_invalid_user_id_should_raise_invalid_user_book_exception():
    with pytest.raises(InvalidUserBookException):
        UserBook("1", "1", 1, "1")


def test_invalid_book_id_should_raise_invalid_user_book_exception():
    with pytest.raises(InvalidUserBookException):
        UserBook("1", 1, "1", "1")


def test_invalid_default_bookshelf_should_raise_invalid_user_book_exception():
    with pytest.raises(InvalidUserBookException):
        UserBook("1", "1", "1", 1)


def test_invalid_id_should_raise_invalid_user_book_exception():
    with pytest.raises(InvalidUserBookException):
        UserBook(1, "1", "1", "1")
