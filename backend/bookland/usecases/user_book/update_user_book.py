from bookland.domain.entities.user_book import UserBook
from bookland.domain.repositories.user_book_repository import UserBookRepository


class UpdateUserBookUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    def execute(self, user_book: UserBook) -> None:
        self._repository.update(user_book)
