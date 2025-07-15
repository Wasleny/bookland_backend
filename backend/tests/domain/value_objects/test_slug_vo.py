import pytest

from bookland.domain.value_objects import Slug
from bookland.domain.exceptions import InvalidSlugException


def test_valid_slug_should_be_accepted():
    slug = Slug("science-fiction")

    assert slug.value == "science-fiction"


def test_invalid_slug_should_raise_invalid_slug_exception():
    with pytest.raises(InvalidSlugException):
        Slug("Science-fiction")


def test_slug_not_string_should_raise_invalid_slug_exception():
    with pytest.raises(InvalidSlugException):
        Slug(1)


def test_slug_exceeding_max_length_should_raise_invalid_slug_exception():
    with pytest.raises(InvalidSlugException):
        Slug("a" * 51)


def test_str_should_return_slug_value():
    slug = Slug("science-fiction")
    assert str(slug) == "science-fiction"
