from bookland.infra.repositories import InMemorySeriesRepository
from bookland.application.usecases import GetAllSeriesUseCase
from tests.factories.series_factory import create_series


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_all_series_returns_all_series():
    repository = InMemorySeriesRepository()
    usecase = GetAllSeriesUseCase(repository)

    series1 = create_series()
    series2 = create_series()
    await repository.create(series1)
    await repository.create(series2)

    series_found = await usecase.execute()

    assert len(series_found) == 2
    assert series1 in series_found
    assert series2 in series_found
