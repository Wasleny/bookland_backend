from bookland.domain.repositories import BookRepository
from bookland.domain.entities import Book


class SearchBooksUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    async def execute(self, search_terms: dict) -> list[Book]:
        return await self._repository.search(search_terms)
