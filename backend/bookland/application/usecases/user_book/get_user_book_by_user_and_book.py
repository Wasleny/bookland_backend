from bookland.domain.entities import UserBook
from bookland.domain.repositories import UserBookRepository


class GetUserBookByUserAndBookUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    async def execute(self, user_id: str, book_id: str) -> UserBook | None:
        return await self._repository.get_by_user_and_book(user_id, book_id)
