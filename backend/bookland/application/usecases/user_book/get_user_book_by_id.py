from bookland.domain.entities import UserBook
from bookland.domain.repositories import UserBookRepository


class GetUserBookByIdUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    async def execute(self, user_book_id: str) -> UserBook | None:
        return await self._repository.get_by_id(user_book_id)
