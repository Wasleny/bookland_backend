from bookland.domain.entities import ReadingInProgress
from bookland.domain.repositories import ReadingInProgressRepository


class CreateReadingInProgressUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    async def execute(
        self, reading_in_progress: ReadingInProgress
    ) -> ReadingInProgress:
        return await self._repository.create(reading_in_progress)
