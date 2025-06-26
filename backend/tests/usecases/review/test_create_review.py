from bookland.infra.repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.usecases.review.create_review import CreateReviewUseCase
from tests.factories.review_factory import create_review


def test_create_review_creates_review_successfully():
    repository = InMemoryReviewRepository()
    usecase = CreateReviewUseCase(repository)
    review = create_review()

    usecase.execute(review)

    assert repository.get_by_id(review.id) == review
