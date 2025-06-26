import pytest
from bookland.domain.value_objects.label_vo import Label


def test_valid_label_should_be_accepted():
    label = Label("quero ler")

    assert label.value == "Quero Ler"


def test_empty_label_name_should_raise_value_error():
    with pytest.raises(ValueError):
        Label("")


def test_invalid_label_should_raise_value_error():
    with pytest.raises(ValueError):
        Label("quero.ler")


def test_label_exceeding_max_length_should_raise_value_error():
    with pytest.raises(ValueError):
        Label("A" * 51)


def test_labels_with_same_value_should_be_equal():
    label1 = Label("quero ler")
    label2 = Label("Quero Ler")

    assert label1 == label2


def test_str_should_return_label_name_value():
    label = Label("Quero Ler")
    assert str(label) == "Quero Ler"
