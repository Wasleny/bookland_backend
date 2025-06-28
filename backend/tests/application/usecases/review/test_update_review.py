from bookland.infra.repositories.inmemory_repositories.in_memory_review_repository import (
    InMemoryReviewRepository,
)
from bookland.application.usecases.review.update_review import UpdateReviewUseCase
from tests.factories.review_factory import create_review


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_update_review_updates_review_data():
    repository = InMemoryReviewRepository()
    usecase = UpdateReviewUseCase(repository)

    review = create_review()
    await repository.create(review)

    updated_data = create_review(id=review.id, rating=4)

    updated_review = await usecase.execute(updated_data)

    assert updated_review.body == "Esse livro transformou a minha vida"
    assert updated_review.rating == 4


@pytest.mark.asyncio
async def test_update_review_not_updates_when_not_found():
    repository = InMemoryReviewRepository()
    usecase = UpdateReviewUseCase(repository)

    review = create_review()
    await repository.create(review)

    updated_data = create_review()

    updated_review = await usecase.execute(updated_data)

    assert updated_review is None
