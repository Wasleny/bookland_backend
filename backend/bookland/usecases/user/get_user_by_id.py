from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository


class GetUserByIdUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, user_id: str) -> User | None:
        return self._repository.get_by_id(user_id)
