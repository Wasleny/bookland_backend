from bookland.infra.repositories import InMemoryReviewRepository
from bookland.application.usecases import GetReviewsByUserAndBookUseCase
from tests.factories.review_factory import create_review


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_reviews_by_user_and_book_returns_review():
    repository = InMemoryReviewRepository()
    usecase = GetReviewsByUserAndBookUseCase(repository)

    review = create_review()
    await repository.create(review)

    reviews = await usecase.execute(review.user_id, review.book_id)

    assert len(reviews) == 1


@pytest.mark.asyncio
async def test_get_reviews_by_user_and_book_returns_none_when_not_found():
    repository = InMemoryReviewRepository()
    usecase = GetReviewsByUserAndBookUseCase(repository)

    review = create_review()
    await repository.create(review)

    reviews = await usecase.execute("invalid-id", review.book_id)

    assert len(reviews) == 0
