import pytest
from bookland.domain.entities.user_book import UserBook
from bookland.domain.exceptions.user_book_exception import InvalidUserBookException
from bookland.domain.value_objects.label_vo import Label


def test_valid_user_book_should_be_created():
    user_book = UserBook("1", "1", "1", Label("Lidos"))

    assert user_book.id == "1"
    assert user_book.book_id == "1"
    assert user_book.user_id == "1"
    assert user_book.default_bookshelf == Label("Lidos")


def test_invalid_user_id_should_raise_invalid_user_book_exception():
    with pytest.raises(InvalidUserBookException):
        UserBook("1", "1", 1, Label("Lidos"))


def test_invalid_book_id_should_raise_invalid_user_book_exception():
    with pytest.raises(InvalidUserBookException):
        UserBook("1", 1, "1", Label("Lidos"))


def test_invalid_default_bookshelf_should_raise_invalid_user_book_exception():
    with pytest.raises(InvalidUserBookException):
        UserBook("1", "1", "1", "Lidos")
