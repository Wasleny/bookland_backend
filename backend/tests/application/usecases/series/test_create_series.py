from bookland.infra.repositories.inmemory_repositories.in_memory_series_repository import (
    InMemorySeriesRepository,
)
from bookland.application.usecases.series.create_series import CreateSeriesUseCase
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
