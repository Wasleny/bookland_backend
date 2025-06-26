from bookland.utils.text_utils import title_case, normalize_text
import pytest


def test_title_case_with_replaces_hyphen_false():
    assert title_case("o senhor dos aneis") == "O Senhor dos Aneis"


def test_title_case_with_replaces_hyphen_true():
    assert (
        title_case("o-senhor-dos-aneis", replaces_hyphen=True) == "O Senhor dos Aneis"
    )


def test_title_case_without_small_words():
    assert title_case("o senhor dos aneis", False) == "O Senhor Dos Aneis"


def test_normalize_text_with_replaces_with_none():
    assert normalize_text("J.R.R. Tolkien") == "jrr tolkien"


def test_normalize_text_with_replaces_with_hyphen():
    assert normalize_text("O Senhor dos Aneis", "-") == "o-senhor-dos-aneis"


def test_normalize_text_without_remove_special_chars():
    assert normalize_text("#Ficção", remove_special_chars=False) == "#ficcao"


def test_normalize_text_with_invalid_text_should_raise_type_error():
    with pytest.raises(TypeError):
        normalize_text(1)


def test_normalize_text_with_invalid_replacement_should_raise_type_error():
    with pytest.raises(TypeError):
        normalize_text("texto texto", 1)
