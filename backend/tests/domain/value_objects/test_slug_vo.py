import pytest
from bookland.domain.value_objects.slug_vo import Slug


def test_valid_slug_should_be_accepted():
    slug = Slug("science-fiction")

    assert slug.value == "science-fiction"


def test_invalid_slug_should_raise_value_error():
    with pytest.raises(ValueError):
        Slug("Science-fiction")


def test_str_should_return_slug_value():
    slug = Slug("science-fiction")
    assert str(slug) == 'science-fiction'