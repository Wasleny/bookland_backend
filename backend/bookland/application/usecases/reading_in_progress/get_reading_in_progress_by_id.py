from bookland.domain.entities import ReadingInProgress
from bookland.domain.repositories import ReadingInProgressRepository


class GetReadingInProgressByIdUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    async def execute(self, reading_in_progress_id: str) -> ReadingInProgress | None:
        return await self._repository.get_by_id(reading_in_progress_id)
