from bookland.infra.repositories.in_memory_series_repository import (
    InMemorySeriesRepository,
)
from bookland.usecases.series.update_series import UpdateSeriesUseCase
from tests.factories.series_factory import create_series
from bookland.domain.value_objects.name_vo import Name


def test_update_series_updates_series_data():
    repository = InMemorySeriesRepository()
    usecase = UpdateSeriesUseCase(repository)

    series = create_series()
    repository.create(series)

    updated_data = create_series(id=series.id, name=Name("Throne of Glass"))

    usecase.execute(updated_data)

    updated_series = repository.get_by_id(series.id)

    assert updated_series.name.value == "Throne of Glass"
