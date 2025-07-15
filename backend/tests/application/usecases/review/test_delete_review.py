from bookland.infra.repositories import InMemoryReviewRepository
from bookland.application.usecases import DeleteReviewUseCase
from tests.factories.review_factory import create_review


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_delete_review_removes_review():
    repository = InMemoryReviewRepository()
    usecase = DeleteReviewUseCase(repository)

    review = create_review()
    await repository.create(review)

    deleted_review = await usecase.execute(review.id)

    assert deleted_review is not None


@pytest.mark.asyncio
async def test_delete_review_not_find_review_returns_none():
    repository = InMemoryReviewRepository()
    usecase = DeleteReviewUseCase(repository)

    deleted_review = await usecase.execute(1)

    assert deleted_review is None
