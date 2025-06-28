from bookland.domain.entities.user import User
from bookland.domain.repositories.user_repository import UserRepository


class SetCurrentUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self, user_id: str) -> None:
        await self._repository.set_current_user(user_id)
