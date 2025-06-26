from bookland.infra.repositories.in_memory_series_repository import (
    InMemorySeriesRepository,
)
from bookland.usecases.series.get_all_series import GetAllSeriesUseCase
from tests.factories.series_factory import create_series


def test_get_all_series_returns_all_series():
    repository = InMemorySeriesRepository()
    usecase = GetAllSeriesUseCase(repository)

    series1 = create_series()
    series2 = create_series()
    repository.create(series1)
    repository.create(series2)

    series_found = usecase.execute()

    assert len(series_found) == 2
    assert series1 in series_found
    assert series2 in series_found
