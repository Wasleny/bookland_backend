import pytest
from bookland.domain.value_objects.title_vo import Title


def test_valid_title_should_be_accepted():
    title = Title("O Senhor dos Anéis: As Duas Torres")

    assert title.value == "O Senhor dos Anéis: As Duas Torres"


def test_title_with_only_whitespace_should_raise_value_error():
    with pytest.raises(ValueError):
        Title(" ")


def test_title_exceeding_max_length_should_raise_value_error():
    with pytest.raises(ValueError):
        Title("A" * 151)


def test_title_with_forbidden_characters_should_raise_value_error():
    with pytest.raises(ValueError):
        Title("Title @")


def test_titles_with_same_value_should_be_equal():
    title1 = Title("O Senhor dos Anéis: As Duas Torres")
    title2 = Title("O Senhor dos Anéis: As Duas Torres")

    assert title1 == title2


def test_str_returns_clean_title_text():
    title = Title("O Hobbit")
    assert str(title) == "O Hobbit"
