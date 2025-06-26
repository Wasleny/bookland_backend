from bookland.domain.entities.user_book import UserBook
from bookland.domain.repositories.user_book_repository import UserBookRepository


class GetUserBookByUserUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    def execute(self, user_id: str) -> list[UserBook]:
        return self._repository.get_by_user(user_id)
