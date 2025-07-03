from bookland.infra.repositories.inmemory_repositories.in_memory_criterion_repository import (
    InMemoryCriterionRepository,
)
from bookland.application.usecases.criterion.get_all_criteria import (
    GetAllCriteriaUseCase,
)
from tests.factories.criterion_factory import create_criterion


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_all_criteria_returns_all_criteria():
    repository = InMemoryCriterionRepository()
    usecase = GetAllCriteriaUseCase(repository)

    criterion1 = create_criterion()
    criterion2 = create_criterion(user_id=criterion1.user_id)
    await repository.create(criterion1)
    await repository.create(criterion2)

    criteria = await usecase.execute(criterion1.user_id)

    assert len(criteria) == 2
    assert criterion1 in criteria
    assert criterion2 in criteria
