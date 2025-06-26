from bookland.infra.repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.usecases.review.delete_all_reviews_for_user_and_book import (
    DeleteAllReviewsForUserAndBookUseCase,
)
from tests.factories.review_factory import create_review


def test_delete_all_reviews_for_user_and_book_removes_reviews():
    repository = InMemoryReviewRepository()
    usecase = DeleteAllReviewsForUserAndBookUseCase(repository)

    review = create_review()
    repository.create(review)

    usecase.execute(review.user_id, review.book_id)

    assert len(repository.get_by_user_and_book(review.user_id, review.book_id)) == 0
