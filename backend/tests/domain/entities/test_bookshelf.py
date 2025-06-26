import pytest
from bookland.domain.entities.bookshelf import Bookshelf
from bookland.domain.value_objects.label_vo import Label
from bookland.domain.value_objects.slug_vo import Slug
from bookland.domain.exceptions.bookshelf_exception import InvalidBookshelfException


def test_valid_bookshelf_should_be_created():
    bookshelf = Bookshelf("1", Label("quero ler"), Slug("quero-ler"))

    assert bookshelf.id == "1"
    assert bookshelf.name.value == "Quero Ler"
    assert bookshelf.slug.value == "quero-ler"


def test_invalid_name_should_raise_invalid_bookshelf_exception():
    with pytest.raises(InvalidBookshelfException):
        Bookshelf("1", "quero ler", Slug("quero-ler"))


def test_invalid_slug_should_raise_invalid_bookshelf_exception():
    with pytest.raises(InvalidBookshelfException):
        Bookshelf("1", Label("quero ler"), "quero-ler")
