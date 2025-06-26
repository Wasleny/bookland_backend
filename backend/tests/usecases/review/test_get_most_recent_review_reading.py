from bookland.infra.repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.usecases.review.get_most_recent_review_reading import (
    GetMostRecentReviewReadingUseCase,
)
from tests.factories.review_factory import create_review


def test_get_most_recent_review_reading_returns_review():
    repository = InMemoryReviewRepository()
    usecase = GetMostRecentReviewReadingUseCase(repository)

    review = create_review(most_recent_reading=True)
    repository.create(review)

    most_recente_reading = usecase.execute(review.user_id, review.book_id)

    assert most_recente_reading == review


def test_get_most_recent_review_reading_returns_none_when_not_found():
    repository = InMemoryReviewRepository()
    usecase = GetMostRecentReviewReadingUseCase(repository)

    review = create_review()
    repository.create(review)

    most_recente_reading = usecase.execute(review.user_id, review.book_id)

    assert most_recente_reading is None
