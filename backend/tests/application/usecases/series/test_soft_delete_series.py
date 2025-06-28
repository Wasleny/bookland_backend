from bookland.infra.repositories.inmemory_repositories.in_memory_series_repository import (
    InMemorySeriesRepository,
)
from bookland.application.usecases.series.soft_delete_series import (
    SoftDeleteSeriesUseCase,
)
from tests.factories.series_factory import create_series

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_soft_delete_series_removes_series():
    repository = InMemorySeriesRepository()
    usecase = SoftDeleteSeriesUseCase(repository)

    series = create_series()
    await repository.create(series)

    await usecase.execute(series.id)

    assert series.is_deleted is True
