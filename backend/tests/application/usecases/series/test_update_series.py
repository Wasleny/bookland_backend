from bookland.infra.repositories.inmemory_repositories.in_memory_series_repository import (
    InMemorySeriesRepository,
)
from bookland.application.usecases.series.update_series import UpdateSeriesUseCase
from tests.factories.series_factory import create_series
from bookland.domain.value_objects.name_vo import Name


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_update_series_updates_series_data():
    repository = InMemorySeriesRepository()
    usecase = UpdateSeriesUseCase(repository)

    series = create_series()
    await repository.create(series)

    updated_data = create_series(id=series.id, name=Name("Throne of Glass"))

    updated_series = await usecase.execute(updated_data)

    assert updated_series.name.value == "Throne of Glass"


@pytest.mark.asyncio
async def test_update_series_not_updates_when_not_found():
    repository = InMemorySeriesRepository()
    usecase = UpdateSeriesUseCase(repository)

    series = create_series()
    await repository.create(series)

    updated_data = create_series()

    updated_series = await usecase.execute(updated_data)

    assert updated_series is None
