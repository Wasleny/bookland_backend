from bookland.domain.entities import User
from bookland.domain.repositories import UserRepository


class GetUserByIdUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self, user_id: str) -> User | None:
        return await self._repository.get_by_id(user_id)
