from bookland.domain.repositories import BookRepository
from bookland.domain.entities import Book


class GetAllBooksUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    async def execute(self) -> list[Book]:
        return await self._repository.get_all()
