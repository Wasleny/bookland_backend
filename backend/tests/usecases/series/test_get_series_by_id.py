from bookland.infra.repositories.in_memory_series_repository import (
    InMemorySeriesRepository,
)
from bookland.usecases.series.get_series_by_id import GetSeriesByIdUseCase
from tests.factories.series_factory import create_series


def test_get_series_by_id_returns_series():
    repository = InMemorySeriesRepository()
    usecase = GetSeriesByIdUseCase(repository)

    series = create_series()
    repository.create(series)

    series_found = usecase.execute(series.id)

    assert series_found == series


def test_get_series_by_id_returns_none_when_not_found():
    repository = InMemorySeriesRepository()
    usecase = GetSeriesByIdUseCase(repository)

    series = create_series()
    repository.create(series)

    series_found = usecase.execute("invalid-id")

    assert series_found is None
