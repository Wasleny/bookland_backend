from bookland.infra.repositories import InMemoryCriterionRepository
from bookland.application.usecases import UpdateCriterionUseCase
from tests.factories.criterion_factory import create_criterion

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_update_criterion_updates_criterion_data():
    repository = InMemoryCriterionRepository()
    usecase = UpdateCriterionUseCase(repository)

    criterion = create_criterion()
    await repository.create(criterion)

    updated_data = create_criterion(id=criterion.id, user_id="2")

    updated_criterion = await usecase.execute(updated_data)

    assert updated_criterion.user_id == "2"
    assert updated_criterion.name.value == "Ritmo"


@pytest.mark.asyncio
async def test_update_criterion_not_updates_when_not_found():
    repository = InMemoryCriterionRepository()
    usecase = UpdateCriterionUseCase(repository)

    criterion = create_criterion()
    await repository.create(criterion)

    updated_data = create_criterion()

    updated_criterion = await usecase.execute(updated_data)

    assert updated_criterion is None
