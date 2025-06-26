from bookland.infra.repositories.in_memory_series_repository import InMemorySeriesRepository
from bookland.usecases.series.create_series import CreateSeriesUseCase
from tests.factories.series_factory import create_series


def test_create_series_creates_series_successfully():
    repository = InMemorySeriesRepository()
    usecase = CreateSeriesUseCase(repository)
    series = create_series()

    usecase.execute(series)

    assert repository.get_by_id(series.id) == series
