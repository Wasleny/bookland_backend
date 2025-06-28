from bookland.infra.repositories.inmemory_repositories.in_memory_criterion_repository import (
    InMemoryCriterionRepository,
)
from bookland.application.usecases.criterion.get_criterion_by_id import (
    GetCriterionByIdUseCase,
)
from tests.factories.criterion_factory import create_criterion


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_criterion_by_id_returns_criterion_when_found():
    repository = InMemoryCriterionRepository()
    usecase = GetCriterionByIdUseCase(repository)

    criterion = create_criterion()
    await repository.create(criterion)

    criterion_found = await usecase.execute(criterion.id)

    assert criterion == criterion_found


@pytest.mark.asyncio
async def test_get_criterion_by_id_returns_none_when_not_found():
    repository = InMemoryCriterionRepository()
    usecase = GetCriterionByIdUseCase(repository)

    criterion_found = await usecase.execute("invalid-id")

    assert criterion_found is None
