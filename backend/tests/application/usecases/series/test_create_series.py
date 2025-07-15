from bookland.infra.repositories import InMemorySeriesRepository
from bookland.application.usecases import CreateSeriesUseCase
from tests.factories.series_factory import create_series


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_create_series_creates_series_successfully():
    repository = InMemorySeriesRepository()
    usecase = CreateSeriesUseCase(repository)
    series = create_series()

    retrieved_series = await usecase.execute(series)

    assert retrieved_series == series
