from bookland.infra.repositories.inmemory_repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.application.usecases.review.create_review import CreateReviewUseCase
from tests.factories.review_factory import create_review


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_create_review_creates_review_successfully():
    repository = InMemoryReviewRepository()
    usecase = CreateReviewUseCase(repository)
    review = create_review()

    retrieved_review = await usecase.execute(review)

    assert retrieved_review == review
