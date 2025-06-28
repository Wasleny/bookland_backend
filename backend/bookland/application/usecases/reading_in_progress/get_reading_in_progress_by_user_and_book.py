from bookland.domain.entities.reading_in_progress import ReadingInProgress
from bookland.domain.repositories.reading_in_progress_repository import (
    ReadingInProgressRepository,
)


class GetReadingInProgressByUserAndBookUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    async def execute(self, user_id: str, book_id: str) -> ReadingInProgress | None:
        return await self._repository.get_by_user_and_book(user_id, book_id)
