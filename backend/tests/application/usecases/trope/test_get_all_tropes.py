from bookland.infra.repositories import InMemoryTropeRepository
from bookland.application.usecases import GetAllTropesUseCase


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_all_tropes_returns_all_tropes():
    repository = InMemoryTropeRepository()
    usecase = GetAllTropesUseCase(repository)

    tropes = await usecase.execute()

    assert len(tropes) == 0
