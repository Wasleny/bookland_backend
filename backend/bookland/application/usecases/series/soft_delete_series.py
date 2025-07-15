from bookland.domain.entities import Series
from bookland.domain.repositories import SeriesRepository


class SoftDeleteSeriesUseCase:
    def __init__(self, repository: SeriesRepository):
        self._repository = repository

    async def execute(self, series_id: str) -> Series | None:
        return await self._repository.soft_delete(series_id)
