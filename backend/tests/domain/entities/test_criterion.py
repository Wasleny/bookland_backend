import pytest
from bookland.domain.entities.criterion import Criterion
from bookland.domain.value_objects.label_vo import Label
from bookland.domain.exceptions.entities.criterion_exception import (
    InvalidCriterionException,
)


def test_valid_criterion_should_be_created():
    criterion = Criterion(
        "1",
        Label("Ritmo"),
        "Avalia o ritmo da história, se é muito lenta, se é muito acelerada ou se tem um ritmo balanceado",
        "1",
    )

    assert criterion.id == "1"
    assert criterion.name.value == "Ritmo"
    assert (
        criterion.description
        == "Avalia o ritmo da história, se é muito lenta, se é muito acelerada ou se tem um ritmo balanceado"
    )
    assert criterion.user_id == "1"
    assert criterion.is_deleted == False
    assert criterion.deleted_at is None


def test_invalid_name_should_raise_invalid_criterion_exception():
    with pytest.raises(InvalidCriterionException):
        Criterion(
            "1",
            "Ritmo",
            "Avalia o ritmo da história, se é muito lenta, se é muito acelerada ou se tem um ritmo balanceado",
            "1",
        )


def test_invalid_description_should_raise_invalid_criterion_exception():
    with pytest.raises(InvalidCriterionException):
        Criterion("1", Label("Narrativa"), "", "1")


def test_invalid_user_id_should_raise_invalid_criterion_exception():
    with pytest.raises(InvalidCriterionException):
        Criterion("1", Label("Narrativa"), "Avalia a narrativa", "")


def test_invalid_id_should_raise_invalid_criterion_exception():
    with pytest.raises(InvalidCriterionException):
        Criterion(1, Label("Narrativa"), "Avalia a narrativa", "1")


def test_soft_delete_marks_criterion_as_deleted():
    criterion = Criterion(
        "1",
        Label("Ritmo"),
        "Avalia o ritmo da história, se é muito lenta, se é muito acelerada ou se tem um ritmo balanceado",
        "1",
    )
    criterion.soft_delete()

    assert criterion.is_deleted is True
    assert criterion.deleted_at is not None
