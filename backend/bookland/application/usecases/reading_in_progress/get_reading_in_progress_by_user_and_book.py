from bookland.domain.entities import ReadingInProgress
from bookland.domain.repositories import ReadingInProgressRepository


class GetReadingInProgressByUserAndBookUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    async def execute(self, user_id: str, book_id: str) -> ReadingInProgress | None:
        return await self._repository.get_by_user_and_book(user_id, book_id)
