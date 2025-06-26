import pytest
from bookland.domain.entities.trope import Trope
from bookland.domain.value_objects.label_vo import Label
from bookland.domain.value_objects.slug_vo import Slug
from bookland.domain.exceptions.trope_exception import InvalidTropeException


def test_valid_trope_should_be_created():
    trope = Trope("1", Label("found family"), Slug("found-family"))

    assert trope.id == "1"
    assert trope.name.value == "Found Family"
    assert trope.slug.value == "found-family"
    assert trope.is_deleted == False
    assert trope.deleted_at is None


def test_invalid_name_should_raise_invalid_trope_exception():
    with pytest.raises(InvalidTropeException):
        Trope("1", "Found Family", Slug("found-family"))


def test_invalid_slug_should_raise_invalid_trope_exception():
    with pytest.raises(InvalidTropeException):
        Trope("1", Label("Found Family"), "found-family")

def test_soft_delete_marks_trope_as_deleted():
    trope = Trope("1", Label("found family"), Slug("found-family"))
    trope.soft_delete()

    assert trope.is_deleted is True
    assert trope.deleted_at is not None