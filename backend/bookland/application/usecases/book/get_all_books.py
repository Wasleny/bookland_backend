from bookland.domain.repositories.book_repository import BookRepository
from bookland.domain.entities.book import Book


class GetAllBooksUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    async def execute(self) -> list[Book]:
        return await self._repository.get_all()
