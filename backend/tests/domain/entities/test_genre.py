import pytest
from bookland.domain.entities.genre import Genre
from bookland.domain.value_objects.label_vo import Label
from bookland.domain.value_objects.slug_vo import Slug
from bookland.domain.exceptions.genre_exception import InvalidGenreException


def test_valid_genre_should_be_created():
    genre = Genre("1", Label("Não ficção"), Slug("nao-ficcao"))

    assert genre.id == "1"
    assert genre.name.value == "Não Ficção"
    assert genre.slug.value == "nao-ficcao"
    assert genre.is_deleted == False
    assert genre.deleted_at is None


def test_invalid_name_should_raise_invalid_genre_exception():
    with pytest.raises(InvalidGenreException):
        Genre("1", "Fantasia", Slug("fantasia"))


def test_invalid_slug_should_raise_invalid_genre_exception():
    with pytest.raises(InvalidGenreException):
        Genre("1", Label("Fantasia"), "fantasia")


def test_soft_delete_marks_genre_as_deleted():
    genre = Genre("1", Label("Não ficção"), Slug("nao-ficcao"))
    genre.soft_delete()

    assert genre.is_deleted is True
    assert genre.deleted_at is not None
