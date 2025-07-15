from bookland.infra.repositories import InMemoryBookshelfRepository
from bookland.application.usecases import GetAllBookshelvesUseCase


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_all_bookshelves_returns_all_bookshelves():
    repository = InMemoryBookshelfRepository()
    usecase = GetAllBookshelvesUseCase(repository)

    bookshelves = await usecase.execute()

    assert len(bookshelves) == 2
