from bookland.infra.repositories.inmemory_repositories.in_memory_criterion_repository import (
    InMemoryCriterionRepository,
)
from bookland.application.usecases.criterion.soft_delete_criterion import (
    SoftDeleteCriterionUseCase,
)
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
