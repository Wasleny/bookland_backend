from bookland.infra.repositories.inmemory_repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.application.usecases.review.delete_review import DeleteReviewUseCase
from tests.factories.review_factory import create_review


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_delete_review_removes_review():
    repository = InMemoryReviewRepository()
    usecase = DeleteReviewUseCase(repository)

    review = create_review()
    await repository.create(review)

    await usecase.execute(review.id)

    retrieved_review = await repository.get_by_id(review.id)

    assert retrieved_review is None
