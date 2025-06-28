from bookland.domain.entities.book import Book
from bookland.domain.repositories.book_repository import BookRepository


class UpdateBookUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    async def execute(self, book: Book) -> Book | None:
        return await self._repository.update(book)
