import pytest
from bookland.domain.value_objects.reading_criteria_vo import ReadingCriteria


def test_valid_reading_criteria_should_be_accepted():
    reading_criteria = ReadingCriteria("Enredo", 4)

    assert reading_criteria.criterion == "Enredo"
    assert reading_criteria.rating == 4
    assert reading_criteria.to_dict() == {"criterion": "Enredo", "rating": 4}


def test_reading_criteria_with_same_value_should_be_equal():
    reading_criteria1 = ReadingCriteria("Enredo", 4)
    reading_criteria2 = ReadingCriteria("Enredo", 4)

    assert reading_criteria1 == reading_criteria2


def test_str_should_return_reading_criteria_value():
    reading_criteria = ReadingCriteria("Enredo", 4)
    assert str(reading_criteria) == "Enredo: 4"


def test_invalid_criterion_should_raise_value_error():
    with pytest.raises(ValueError):
        ReadingCriteria("", 4)


def test_invalid_rating_should_raise_value_error():
    with pytest.raises(ValueError):
        ReadingCriteria("Enredo", 6)
