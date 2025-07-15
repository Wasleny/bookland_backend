from bookland.domain.entities import Book
from bookland.domain.repositories import BookRepository


class CreateBookUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    async def execute(self, book: Book) -> Book:
        return await self._repository.create(book)
