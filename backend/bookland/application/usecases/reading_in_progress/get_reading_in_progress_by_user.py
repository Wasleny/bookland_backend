from bookland.domain.entities import ReadingInProgress
from bookland.domain.repositories import ReadingInProgressRepository


class GetReadingInProgressByUserUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    async def execute(self, user_id: str) -> list[ReadingInProgress]:
        return await self._repository.get_by_user(user_id)
