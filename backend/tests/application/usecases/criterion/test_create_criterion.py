from bookland.infra.repositories.inmemory_repositories.in_memory_criterion_repository import (
    InMemoryCriterionRepository,
)
from bookland.application.usecases.criterion.create_criterion import (
    CreateCriterionUseCase,
)
from tests.factories.criterion_factory import create_criterion


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_create_criterion_creates_criterion_successfully():
    repository = InMemoryCriterionRepository()
    usecase = CreateCriterionUseCase(repository)
    criterion = create_criterion()

    retrieved_criterion = await usecase.execute(criterion)

    assert retrieved_criterion == criterion
