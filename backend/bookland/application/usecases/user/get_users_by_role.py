from bookland.domain.entities import User
from bookland.domain.repositories import UserRepository
from bookland.domain.enums import UserRole


class GetUsersByRoleUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self, role: UserRole) -> list[User]:
        return await self._repository.get_by_role(role)
