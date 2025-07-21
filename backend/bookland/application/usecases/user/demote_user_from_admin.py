from bookland.domain.entities import User
from bookland.domain.repositories import UserRepository


class DemoteUserFromAdminUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self, user_id: str) -> User | None:
        return await self._repository.demote_from_admin(user_id)
