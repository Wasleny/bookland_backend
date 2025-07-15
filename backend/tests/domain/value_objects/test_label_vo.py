import pytest

from bookland.domain.value_objects import Label
from bookland.domain.exceptions import InvalidLabelException


def test_valid_label_should_be_accepted():
    label = Label("quero ler")

    assert label.value == "Quero Ler"


def test_empty_label_name_should_raise_invalid_label_exception():
    with pytest.raises(InvalidLabelException):
        Label("")


def test_invalid_label_should_raise_invalid_label_exception():
    with pytest.raises(InvalidLabelException):
        Label("quero.ler")


def test_label_exceeding_max_length_should_raise_invalid_label_exception():
    with pytest.raises(InvalidLabelException):
        Label("A" * 51)


def test_label_not_string_should_raise_invalid_label_exception():
    with pytest.raises(InvalidLabelException):
        Label(None)


def test_labels_with_same_value_should_be_equal():
    label1 = Label("quero ler")
    label2 = Label("Quero Ler")

    assert label1 == label2


def test_str_should_return_label_name_value():
    label = Label("Quero Ler")

    assert str(label) == "Quero Ler"
