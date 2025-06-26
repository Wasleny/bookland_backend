import pytest
from bookland.domain.entities.author import Author
from bookland.domain.value_objects.name_vo import Name
from bookland.domain.exceptions.author_exception import InvalidAuthorException


def test_valid_author_should_be_created():
    author = Author("1", Name("Sarah J. Maas"), "Estados Unidos")

    assert author.id == "1"
    assert author.name.value == "Sarah J. Maas"
    assert author.nationality == "Estados Unidos"
    assert author.is_deleted == False
    assert author.deleted_at is None


def test_invalid_name_should_raise_invalid_author_exception():
    with pytest.raises(InvalidAuthorException):
        Author("1", "Sarah J. Maas", "Estados Unidos")


def test_soft_delete_marks_author_as_deleted():
    author = Author("1", Name("Sarah J. Maas"), "Estados Unidos")
    author.soft_delete()

    assert author.is_deleted is True
    assert author.deleted_at is not None
