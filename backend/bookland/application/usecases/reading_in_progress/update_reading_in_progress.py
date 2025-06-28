from bookland.domain.entities.reading_in_progress import ReadingInProgress
from bookland.domain.repositories.reading_in_progress_repository import (
    ReadingInProgressRepository,
)


class UpdateReadingInProgressUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    async def execute(
        self, reading_in_progress: ReadingInProgress
    ) -> ReadingInProgress | None:
        return await self._repository.update(reading_in_progress)
