from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository


class RegisterUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, user: User) -> User:
        return self._repository.register(user)
