from bookland.infra.repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.usecases.review.get_review_by_id import GetReviewByIdUseCase
from tests.factories.review_factory import create_review


def test_get_review_by_id_returns_review():
    repository = InMemoryReviewRepository()
    usecase = GetReviewByIdUseCase(repository)

    review = create_review()
    repository.create(review)

    review_found = usecase.execute(review.id)

    assert review_found == review


def test_get_review_by_id_returns_none_when_not_found():
    repository = InMemoryReviewRepository()
    usecase = GetReviewByIdUseCase(repository)

    review = create_review()
    repository.create(review)

    review_found = usecase.execute("invalid-id")

    assert review_found is None
