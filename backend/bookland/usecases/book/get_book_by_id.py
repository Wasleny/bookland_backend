from bookland.domain.repositories.book_repository import BookRepository
from bookland.domain.entities.book import Book


class GetBookByIdUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    def execute(self, book_id: str) -> Book | None:
        return self._repository.get_by_id(book_id)
