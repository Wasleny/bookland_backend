from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository


class RegisterUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self, user: User) -> User:
        return await self._repository.register(user)
