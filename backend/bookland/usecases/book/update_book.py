from bookland.domain.entities.book import Book
from bookland.domain.repositories.book_repository import BookRepository


class UpdateBookUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    def execute(self, book: Book) -> None:
        self._repository.update(book)
