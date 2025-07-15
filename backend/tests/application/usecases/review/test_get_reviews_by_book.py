from bookland.infra.repositories import InMemoryReviewRepository
from bookland.application.usecases import GetReviewsByBookUseCase
from tests.factories.review_factory import create_review

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_reviews_by_book_returns_reviews():
    repository = InMemoryReviewRepository()
    usecase = GetReviewsByBookUseCase(repository)

    review1 = create_review()
    review2 = create_review(book_id=review1.book_id, most_recent_reading=True)
    await repository.create(review1)
    await repository.create(review2)

    reviews = await usecase.execute(review1.book_id)

    assert len(reviews) == 2
