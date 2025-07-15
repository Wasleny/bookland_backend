from bookland.domain.repositories import BookRepository
from bookland.domain.entities import Book


class GetBookByIdUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    async def execute(self, book_id: str) -> Book | None:
        return await self._repository.get_by_id(book_id)
