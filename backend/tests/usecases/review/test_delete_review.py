from bookland.infra.repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.usecases.review.delete_review import DeleteReviewUseCase
from tests.factories.review_factory import create_review


def test_delete_review_removes_review():
    repository = InMemoryReviewRepository()
    usecase = DeleteReviewUseCase(repository)

    review = create_review()
    repository.create(review)

    usecase.execute(review.id)

    assert repository.get_by_id(review.id) is None
