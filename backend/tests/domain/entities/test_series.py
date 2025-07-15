import pytest
from bookland.domain.entities import Series
from bookland.domain.value_objects import Title, Slug
from bookland.domain.exceptions import InvalidSeriesException


def test_valid_series_should_be_created():
    series = Series(
        "1",
        Title("Trono de Vidro"),
        Slug("trono-de-vidro"),
        "Série sobre uma assassina que participa de um torneio para se tornar a campeã do rei.",
    )

    assert series.id == "1"
    assert series.name.value == "Trono de Vidro"
    assert series.slug.value == "trono-de-vidro"
    assert (
        series.description
        == "Série sobre uma assassina que participa de um torneio para se tornar a campeã do rei."
    )
    assert series.is_deleted == False
    assert series.deleted_at is None


def test_invalid_name_should_raise_invalid_series_exception():
    with pytest.raises(InvalidSeriesException):
        Series(
            "1",
            "Trono de Vidro",
            Slug("trono-de-vidro"),
            "Série sobre uma assassina que participa de um torneio para se tornar a campeã do rei.",
        )


def test_invalid_slug_should_raise_invalid_series_exception():
    with pytest.raises(InvalidSeriesException):
        Series(
            "1",
            Title("Trono de Vidro"),
            "trono-de-vidro",
            "Série sobre uma assassina que participa de um torneio para se tornar a campeã do rei.",
        )


def test_invalid_id_should_raise_invalid_series_exception():
    with pytest.raises(InvalidSeriesException):
        Series(
            1,
            Title("Trono de Vidro"),
            Slug("trono-de-vidro"),
            "Série sobre uma assassina que participa de um torneio para se tornar a campeã do rei.",
        )


def test_invalid_description_should_raise_invalid_series_exception():
    with pytest.raises(InvalidSeriesException):
        Series(
            "1",
            Title("Trono de Vidro"),
            Slug("trono-de-vidro"),
            1,
        )


def test_soft_delete_marks_series_as_deleted():
    series = Series(
        "1",
        Title("Trono de Vidro"),
        Slug("trono-de-vidro"),
        "Série sobre uma assassina que participa de um torneio para se tornar a campeã do rei.",
    )
    series.soft_delete()

    assert series.is_deleted is True
    assert series.deleted_at is not None
