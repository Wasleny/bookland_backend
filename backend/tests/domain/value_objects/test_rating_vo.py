import pytest

from bookland.domain.value_objects import Rating
from bookland.domain.exceptions import InvalidRatingException


def test_valid_integer_rating_should_be_accepted():
    rating = Rating(4)

    assert rating.value == 4


def test_invalid_integer_rating_should_raise_invalid_rating_exception():
    with pytest.raises(InvalidRatingException):
        Rating(6)


def test_valid_float_rating_with_flag_should_be_accepted():
    rating = Rating(4.5, True)

    assert rating.value == 4.5


def test_valid_floating_rating_without_flag_should_raise_invalid_rating_exception():
    with pytest.raises(InvalidRatingException):
        Rating(4.5)


def test_invalid_floating_rating_should_raise_invalid_rating_exception():
    with pytest.raises(InvalidRatingException):
        Rating(6.5, True)


def test_invalid_float_with_average_true_should_raise_invalid_rating_exception():
    with pytest.raises(InvalidRatingException):
        Rating(6, True)


def test_empty_rating_is_empty_returns_true():
    rating = Rating()
    assert rating.is_empty() is True


def test_str_should_return_rating_value():
    rating = Rating(4)
    assert str(rating) == "4"
