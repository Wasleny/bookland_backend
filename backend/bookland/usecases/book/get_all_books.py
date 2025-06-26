from bookland.domain.repositories.book_repository import BookRepository
from bookland.domain.entities.book import Book


class GetAllBooksUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    def execute(self) -> list[Book]:
        return self._repository.get_all()
