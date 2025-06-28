from bookland.domain.entities.series import Series
from bookland.domain.repositories.series_repository import SeriesRepository


class SoftDeleteSeriesUseCase:
    def __init__(self, repository: SeriesRepository):
        self._repository = repository

    async def execute(self, series_id: str) -> None:
        await self._repository.soft_delete(series_id)
