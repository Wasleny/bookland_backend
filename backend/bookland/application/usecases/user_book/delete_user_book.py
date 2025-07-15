from bookland.domain.repositories import UserBookRepository
from bookland.domain.entities import UserBook


class DeleteUserBookUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    async def execute(self, user_book_id: str) -> UserBook | None:
        return await self._repository.delete(user_book_id)
