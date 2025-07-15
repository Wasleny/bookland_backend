from bookland.domain.entities import User
from bookland.domain.repositories import UserRepository


class GetCurrentUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self) -> User | None:
        return await self._repository.get_current_user()
