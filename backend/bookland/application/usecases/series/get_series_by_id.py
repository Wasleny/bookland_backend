from bookland.domain.entities.series import Series
from bookland.domain.repositories.series_repository import SeriesRepository


class GetSeriesByIdUseCase:
    def __init__(self, repository: SeriesRepository):
        self._repository = repository

    async def execute(self, series_id: str) -> Series:
        return await self._repository.get_by_id(series_id)
