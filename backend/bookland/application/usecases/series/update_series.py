from bookland.domain.entities import Series
from bookland.domain.repositories import SeriesRepository


class UpdateSeriesUseCase:
    def __init__(self, repository: SeriesRepository):
        self._repository = repository

    async def execute(self, series: Series) -> Series | None:
        return await self._repository.update(series)
