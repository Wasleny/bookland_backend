from bookland.infra.repositories import InMemorySeriesRepository
from bookland.application.usecases import GetSeriesByIdUseCase
from tests.factories.series_factory import create_series


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_series_by_id_returns_series():
    repository = InMemorySeriesRepository()
    usecase = GetSeriesByIdUseCase(repository)

    series = create_series()
    await repository.create(series)

    series_found = await usecase.execute(series.id)

    assert series_found == series


@pytest.mark.asyncio
async def test_get_series_by_id_returns_none_when_not_found():
    repository = InMemorySeriesRepository()
    usecase = GetSeriesByIdUseCase(repository)

    series = create_series()
    await repository.create(series)

    series_found = await usecase.execute("invalid-id")

    assert series_found is None
