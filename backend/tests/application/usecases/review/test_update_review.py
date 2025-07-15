from bookland.infra.repositories import InMemoryReviewRepository
from bookland.application.usecases import UpdateReviewUseCase
from tests.factories.review_factory import create_review
from bookland.domain.value_objects import Rating


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_update_review_updates_review_data():
    repository = InMemoryReviewRepository()
    usecase = UpdateReviewUseCase(repository)

    review = create_review()
    await repository.create(review)

    updated_data = create_review(id=review.id, rating=Rating(4))

    updated_review = await usecase.execute(updated_data)

    assert updated_review.body == "Esse livro transformou a minha vida"
    assert updated_review.rating.value == 4


@pytest.mark.asyncio
async def test_update_review_not_updates_when_not_found():
    repository = InMemoryReviewRepository()
    usecase = UpdateReviewUseCase(repository)

    review = create_review()
    await repository.create(review)

    updated_data = create_review()

    updated_review = await usecase.execute(updated_data)

    assert updated_review is None
