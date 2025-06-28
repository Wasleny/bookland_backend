from bookland.infra.repositories.inmemory_repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.application.usecases.review.get_review_by_id import GetReviewByIdUseCase
from tests.factories.review_factory import create_review


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_review_by_id_returns_review():
    repository = InMemoryReviewRepository()
    usecase = GetReviewByIdUseCase(repository)

    review = create_review()
    await repository.create(review)

    review_found = await usecase.execute(review.id)

    assert review_found == review


@pytest.mark.asyncio
async def test_get_review_by_id_returns_none_when_not_found():
    repository = InMemoryReviewRepository()
    usecase = GetReviewByIdUseCase(repository)

    review = create_review()
    await repository.create(review)

    review_found = await usecase.execute("invalid-id")

    assert review_found is None
