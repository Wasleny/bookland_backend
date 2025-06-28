from bookland.infra.repositories.inmemory_repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.application.usecases.review.delete_all_reviews_for_user_and_book import (
    DeleteAllReviewsForUserAndBookUseCase,
)
from tests.factories.review_factory import create_review


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_delete_all_reviews_for_user_and_book_removes_reviews():
    repository = InMemoryReviewRepository()
    usecase = DeleteAllReviewsForUserAndBookUseCase(repository)

    review = create_review()
    await repository.create(review)

    await usecase.execute(review.user_id, review.book_id)

    reviews = await repository.get_by_user_and_book(review.user_id, review.book_id)

    assert len(reviews) == 0
