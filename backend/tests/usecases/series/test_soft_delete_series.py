from bookland.infra.repositories.in_memory_series_repository import InMemorySeriesRepository
from bookland.usecases.series.soft_delete_series import SoftDeleteSeriesUseCase
from tests.factories.series_factory import create_series

def test_soft_delete_series_removes_series():
    repository = InMemorySeriesRepository()
    usecase = SoftDeleteSeriesUseCase(repository)

    series = create_series()
    repository.create(series)

    usecase.execute(series.id)

    assert repository.get_by_id(series.id) is None
