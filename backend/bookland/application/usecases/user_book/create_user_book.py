from bookland.domain.entities import UserBook
from bookland.domain.repositories import UserBookRepository


class CreateUserBookUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    async def execute(self, user_book: UserBook) -> UserBook:
        return await self._repository.create(user_book)
