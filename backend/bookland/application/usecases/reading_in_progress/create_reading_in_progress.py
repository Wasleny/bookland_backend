from bookland.domain.entities.reading_in_progress import ReadingInProgress
from bookland.domain.repositories.reading_in_progress_repository import (
    ReadingInProgressRepository,
)


class CreateReadingInProgressUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    async def execute(
        self, reading_in_progress: ReadingInProgress
    ) -> ReadingInProgress:
        return await self._repository.create(reading_in_progress)
