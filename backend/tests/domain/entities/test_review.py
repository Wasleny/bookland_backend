import pytest
from datetime import date

from bookland.domain.exceptions import InvalidReviewException
from bookland.domain.value_objects import ReadingCriteria, Date, Label, Rating
from bookland.domain.entities import Review


def make_review_data(**overrides):
    base = {
        "id": "1",
        "user_id": "1",
        "book_id": "1",
        "rating": Rating(5),
        "body": "Esse livro transformou a minha vida",
        "spoiler": False,
        "start_date": Date(date(2025, 6, 20)),
        "end_date": Date(date(2025, 6, 20)),
        "most_recent_reading": False,
        "rating_composition_criteria": [
            ReadingCriteria(Label("Enredo"), Rating(5)),
            ReadingCriteria(Label("Escrita"), Rating(5)),
        ],
        "independent_rating_criteria": [
            ReadingCriteria(Label("Impacto Emocional"), Rating(5))
        ],
    }
    base.update(overrides)

    return base


def test_valid_review_should_be_accepted():
    review_data = make_review_data()
    review = Review(**review_data)

    assert review.id == review_data["id"]
    assert review.user_id == review_data["user_id"]
    assert review.book_id == review_data["book_id"]
    assert review.rating == review_data["rating"]
    assert review.body == review_data["body"]
    assert review.spoiler == review_data["spoiler"]
    assert review.start_date == review_data["start_date"]
    assert review.end_date == review_data["end_date"]
    assert review.most_recent_reading == review_data["most_recent_reading"]
    assert (
        review.rating_composition_criteria == review_data["rating_composition_criteria"]
    )
    assert (
        review.independent_rating_criteria == review_data["independent_rating_criteria"]
    )


def test_invalid_user_id_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(user_id=None))


def test_invalid_book_id_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(book_id=None))


def test_valid_review_without_rating_should_be_accepted():
    Review(**make_review_data(rating=Rating(None)))


def test_invalid_rating_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(rating=6))


def test_invalid_id_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(id=6))


def test_valid_review_without_body_should_be_accepted():
    Review(**make_review_data(body=None))


def test_invalid_body_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(body=""))


def test_invalid_spoiler_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(spoiler=""))


def test_valid_review_without_start_date_should_be_accepted():
    Review(**make_review_data(start_date=None))


def test_invalid_start_date_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(start_date="2025-06-20"))


def test_valid_review_without_end_date_should_be_accepted():
    Review(**make_review_data(end_date=None))


def test_invalid_end_date_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(end_date="2025-06-20"))


def test_invalid_most_recent_reading_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(most_recent_reading=""))


def test_valid_review_without_rating_composition_criteria_should_be_accepted():
    Review(**make_review_data(rating_composition_criteria=None))


def test_invalid_type_rating_composition_criteria_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(rating_composition_criteria=""))


def test_invalid_size_rating_composition_criteria_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(rating_composition_criteria=[]))


def test_invalid_item_rating_composition_criteria_should_raise_invalid_review_exception():
    with pytest.raises(InvalidReviewException):
        Review(**make_review_data(rating_composition_criteria=["teste"]))
