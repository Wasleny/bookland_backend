from bookland.infra.repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.usecases.review.update_review import UpdateReviewUseCase
from tests.factories.review_factory import create_review


def test_update_review_updates_review_data():
    repository = InMemoryReviewRepository()
    usecase = UpdateReviewUseCase(repository)

    review = create_review()
    repository.create(review)

    updated_data = create_review(id=review.id, rating=4)

    usecase.execute(updated_data)

    updated_review = repository.get_by_id(review.id)

    assert updated_review.body == "Esse livro transformou a minha vida"
    assert updated_review.rating == 4
