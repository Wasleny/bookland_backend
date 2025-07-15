from bookland.domain.repositories import ReadingInProgressRepository
from bookland.domain.entities import ReadingInProgress


class DeleteReadingInProgressUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    async def execute(self, reading_in_progress_id: str) -> ReadingInProgress | None:
        return await self._repository.delete(reading_in_progress_id)
