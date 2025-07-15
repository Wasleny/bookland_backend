from bookland.domain.entities import Series
from bookland.domain.repositories import SeriesRepository


class GetAllSeriesUseCase:
    def __init__(self, repository: SeriesRepository):
        self._repository = repository

    async def execute(self) -> list[Series]:
        return await self._repository.get_all()
