from bookland.domain.entities.user_book import UserBook
from bookland.domain.repositories.user_book_repository import UserBookRepository


class DeleteUserBookUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    def execute(self, user_book_id: str) -> None:
        self._repository.delete(user_book_id)
