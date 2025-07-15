from bookland.infra.repositories import InMemorySeriesRepository
from bookland.application.usecases import SoftDeleteSeriesUseCase
from tests.factories.series_factory import create_series

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_soft_delete_series_removes_series():
    repository = InMemorySeriesRepository()
    usecase = SoftDeleteSeriesUseCase(repository)

    series = create_series()
    await repository.create(series)

    deleted_series = await usecase.execute(series.id)

    assert deleted_series is not None


@pytest.mark.asyncio
async def test_soft_delete_series_not_find_removes_none():
    repository = InMemorySeriesRepository()
    usecase = SoftDeleteSeriesUseCase(repository)

    deleted_series = await usecase.execute('1')

    assert deleted_series is None
