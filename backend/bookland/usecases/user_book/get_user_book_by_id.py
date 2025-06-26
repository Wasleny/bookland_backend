from bookland.domain.entities.user_book import UserBook
from bookland.domain.repositories.user_book_repository import UserBookRepository


class GetUserBookByIdUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    def execute(self, user_book_id: str) -> UserBook | None:
        return self._repository.get_by_id(user_book_id)
