from bookland.domain.repositories.book_repository import BookRepository
from bookland.domain.entities.book import Book


class SearchBooksUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    async def execute(self, search_term: str) -> list[Book]:
        return await self._repository.search(search_term)
