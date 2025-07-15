from bookland.infra.repositories import InMemoryGenreRepository
from bookland.application.usecases import GetAllGenresUseCase


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_all_genres_returns_all_genres():
    repository = InMemoryGenreRepository()
    usecase = GetAllGenresUseCase(repository)

    genres = await usecase.execute()

    assert len(genres) == 0
