from bookland.infra.repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.usecases.review.get_review_by_user_and_book import (
    GetReviewsByUserAndBookUseCase,
)
from tests.factories.review_factory import create_review


def test_get_reviews_by_user_and_book_returns_review():
    repository = InMemoryReviewRepository()
    usecase = GetReviewsByUserAndBookUseCase(repository)

    review = create_review()
    repository.create(review)

    reviews = usecase.execute(review.user_id, review.book_id)

    assert len(reviews) == 1


def test_get_reviews_by_user_and_book_returns_none_when_not_found():
    repository = InMemoryReviewRepository()
    usecase = GetReviewsByUserAndBookUseCase(repository)

    review = create_review()
    repository.create(review)

    reviews = usecase.execute('invalid-id', review.book_id)

    assert len(reviews) == 0