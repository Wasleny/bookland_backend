import pytest
from bookland.domain.entities.series import Series
from bookland.domain.value_objects.name_vo import Name
from bookland.domain.exceptions.series_exception import InvalidSeriesException


def test_valid_series_should_be_created():
    series = Series("1", Name("Trono de Vidro"))

    assert series.id == "1"
    assert series.name.value == "Trono de Vidro"
    assert series.is_deleted == False
    assert series.deleted_at is None


def test_invalid_name_should_raise_invalid_series_exception():
    with pytest.raises(InvalidSeriesException):
        Series("1", "Trono de Vidro")


def test_soft_delete_marks_series_as_deleted():
    series = Series("1", Name("Trono de Vidro"))
    series.soft_delete()

    assert series.is_deleted is True
    assert series.deleted_at is not None
