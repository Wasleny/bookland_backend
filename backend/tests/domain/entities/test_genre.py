import pytest

from bookland.domain.entities import Genre
from bookland.domain.value_objects import Label, Slug
from bookland.domain.exceptions import InvalidGenreException


def test_valid_genre_should_be_created():
    genre = Genre("1", Label("Non fiction"), Label("Não ficção"), Slug("non-fiction"))

    assert genre.id == "1"
    assert genre.name.value == "Non Fiction"
    assert genre.name_pt_br.value == "Não Ficção"
    assert genre.slug.value == "non-fiction"
    assert genre.is_deleted == False
    assert genre.deleted_at is None


def test_invalid_id_should_raise_invalid_genre_exception():
    with pytest.raises(InvalidGenreException):
        Genre(1, Label("Fantasy"), Label("Fantasia"), Slug("fantasy"))


def test_invalid_name_should_raise_invalid_genre_exception():
    with pytest.raises(InvalidGenreException):
        Genre("1", "Fantasy", Label("Fantasia"), Slug("fantasy"))


def test_invalid_name_pt_br_should_raise_invalid_genre_exception():
    with pytest.raises(InvalidGenreException):
        Genre("1", Label("Fantasy"), "Fantasia", Slug("fantasy"))


def test_invalid_slug_should_raise_invalid_genre_exception():
    with pytest.raises(InvalidGenreException):
        Genre("1", Label("Fantasy"), Label("Fantasia"), "fantasy")


def test_soft_delete_marks_genre_as_deleted():
    genre = Genre("1", Label("Non fiction"), Label("Não ficção"), Slug("non-fiction"))
    genre.soft_delete()

    assert genre.is_deleted is True
    assert genre.deleted_at is not None
