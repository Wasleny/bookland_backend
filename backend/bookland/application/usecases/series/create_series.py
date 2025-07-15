from bookland.domain.entities import Series
from bookland.domain.repositories import SeriesRepository


class CreateSeriesUseCase:
    def __init__(self, repository: SeriesRepository):
        self._repository = repository

    async def execute(self, series: Series) -> Series:
        return await self._repository.create(series)
