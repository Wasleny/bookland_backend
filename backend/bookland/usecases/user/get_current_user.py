from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository


class GetCurrentUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self) -> User | None:
        return self._repository.get_current_user()
 