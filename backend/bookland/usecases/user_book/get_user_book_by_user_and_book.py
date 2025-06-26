from bookland.domain.entities.user_book import UserBook
from bookland.domain.repositories.user_book_repository import UserBookRepository


class GetUserBookByUserAndBookUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    def execute(self, user_id: str, book_id: str) -> UserBook:
        return self._repository.get_by_user_and_book(user_id, book_id)
