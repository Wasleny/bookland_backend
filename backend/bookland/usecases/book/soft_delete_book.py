from bookland.domain.repositories.book_repository import BookRepository


class SoftDeleteBookUseCase:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    def execute(self, book_id: str) -> None:
        self._repository.soft_delete(book_id)
