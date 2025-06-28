from bookland.domain.entities.series import Series
from bookland.domain.repositories.series_repository import SeriesRepository


class UpdateSeriesUseCase:
    def __init__(self, repository: SeriesRepository):
        self._repository = repository

    async def execute(self, series: Series) -> Series | None:
        return await self._repository.update(series)
