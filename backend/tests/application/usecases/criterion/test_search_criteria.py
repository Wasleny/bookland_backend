from bookland.infra.repositories import InMemoryCriterionRepository
from bookland.application.usecases import SearchCriteriaUseCase
from tests.factories.criterion_factory import create_criterion


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_search_criteria_matches_search():
    repository = InMemoryCriterionRepository()
    usecase = SearchCriteriaUseCase(repository)

    criterion = create_criterion()
    await repository.create(criterion)

    criteria_found = await usecase.execute("Ritmo", criterion.user_id)

    assert len(criteria_found) == 1


@pytest.mark.asyncio
async def test_search_criteria_returns_empty_when_no_match():
    repository = InMemoryCriterionRepository()
    usecase = SearchCriteriaUseCase(repository)

    criterion = create_criterion()
    await repository.create(criterion)

    criteria_found = await usecase.execute("Test", criterion.user_id)

    assert len(criteria_found) == 0
