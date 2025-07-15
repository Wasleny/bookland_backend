from bookland.domain.value_objects import Email, Password
from bookland.domain.entities import User
from bookland.domain.repositories import UserRepository


class LoginUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self, email: Email, password: Password) -> User | None:
        return await self._repository.login(email, password)
