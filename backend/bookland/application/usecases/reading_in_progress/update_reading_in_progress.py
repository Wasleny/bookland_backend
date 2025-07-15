from bookland.domain.entities import ReadingInProgress
from bookland.domain.repositories import ReadingInProgressRepository


class UpdateReadingInProgressUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    async def execute(
        self, reading_in_progress: ReadingInProgress
    ) -> ReadingInProgress | None:
        return await self._repository.update(reading_in_progress)
