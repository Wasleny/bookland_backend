from bookland.domain.entities import User
from bookland.domain.repositories import UserRepository


class GetUserByEmailUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self, email: str) -> User | None:
        return await self._repository.get_by_email(email)
