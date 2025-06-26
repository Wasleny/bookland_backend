import pytest
from bookland.domain.entities.reading_in_progress import ReadingInProgress
from bookland.domain.exceptions.reading_in_progress_exception import (
    InvalidReadingInProgressException,
)


def test_valid_reading_in_progress_should_be_created():
    reading_in_progress = ReadingInProgress("1", "1", "1", 50)

    assert reading_in_progress.id == "1"
    assert reading_in_progress.book_id == "1"
    assert reading_in_progress.user_id == "1"
    assert reading_in_progress.progress == 50


def test_invalid_user_id_should_raise_invalid_reading_in_progress_exception():
    with pytest.raises(InvalidReadingInProgressException):
        ReadingInProgress("1", "1", 1, 50)


def test_empty_user_id_should_raise_invalid_reading_in_progress_exception():
    with pytest.raises(InvalidReadingInProgressException):
        ReadingInProgress("1", "1", "", 50)


def test_invalid_book_id_should_raise_invalid_reading_in_progress_exception():
    with pytest.raises(InvalidReadingInProgressException):
        ReadingInProgress("1", 1, "1", 50)


def test_empty_book_id_should_raise_invalid_reading_in_progress_exception():
    with pytest.raises(InvalidReadingInProgressException):
        ReadingInProgress("1", "", "1", 50)


def test_invalid_progress_should_raise_invalid_reading_in_progress_exception():
    with pytest.raises(InvalidReadingInProgressException):
        ReadingInProgress("1", "1", "1", "50")


def test_out_of_range_progress_should_raise_invalid_reading_in_progress_exception():
    with pytest.raises(InvalidReadingInProgressException):
        ReadingInProgress("1", "1", "1", 101)
