from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository


class SearchUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, search_term: str) -> User | None:
        return self._repository.search(search_term)
