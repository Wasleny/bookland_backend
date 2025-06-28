from bookland.domain.entities.user_book import UserBook
from bookland.domain.repositories.user_book_repository import UserBookRepository


class CreateUserBookUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    async def execute(self, user_book: UserBook) -> UserBook:
        return await self._repository.create(user_book)
