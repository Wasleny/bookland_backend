from bookland.domain.entities.series import Series
from bookland.domain.repositories.series_repository import SeriesRepository


class GetAllSeriesUseCase:
    def __init__(self, repository: SeriesRepository):
        self._repository = repository

    async def execute(self) -> list[Series]:
        return await self._repository.get_all()
