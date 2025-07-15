import pytest

from bookland.domain.value_objects import Title
from bookland.domain.exceptions import InvalidTitleException


def test_valid_title_should_be_accepted():
    title = Title("O Senhor dos Anéis: As Duas Torres")

    assert title.value == "O Senhor dos Anéis: As Duas Torres"


def test_title_with_only_whitespace_should_raise_invalid_title_exception():
    with pytest.raises(InvalidTitleException):
        Title(" ")


def test_title_not_string_should_raise_invalid_title_exception():
    with pytest.raises(InvalidTitleException):
        Title(6)


def test_title_exceeding_max_length_should_raise_invalid_title_exception():
    with pytest.raises(InvalidTitleException):
        Title("A" * 151)


def test_title_with_forbidden_characters_should_raise_invalid_title_exception():
    with pytest.raises(InvalidTitleException):
        Title("Title @")


def test_titles_with_same_value_should_be_equal():
    title1 = Title("O Senhor dos Anéis: As Duas Torres")
    title2 = Title("O Senhor dos Anéis: As Duas Torres")

    assert title1 == title2


def test_str_returns_clean_title_text():
    title = Title("O Hobbit")
    assert str(title) == "O Hobbit"
