from bookland.infra.repositories import InMemoryCriterionRepository
from bookland.application.usecases import SoftDeleteCriterionUseCase
from tests.factories.criterion_factory import create_criterion


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_soft_delete_criterion_removes_criterion():
    repository = InMemoryCriterionRepository()
    usecase = SoftDeleteCriterionUseCase(repository)

    criterion = create_criterion()
    await repository.create(criterion)

    await usecase.execute(criterion.id)

    assert criterion.is_deleted is True


@pytest.mark.asyncio
async def test_soft_delete_criterion_not_find_criterion_return_none():
    repository = InMemoryCriterionRepository()
    usecase = SoftDeleteCriterionUseCase(repository)

    deleted_criterion = await usecase.execute('1')

    assert deleted_criterion is None
