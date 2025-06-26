from bookland.domain.entities.series import Series
from bookland.domain.repositories.series_repository import SeriesRepository


class GetSeriesByIdUseCase:
    def __init__(self, repository: SeriesRepository):
        self._repository = repository

    def execute(self, series_id: str) -> Series:
        return self._repository.get_by_id(series_id)
