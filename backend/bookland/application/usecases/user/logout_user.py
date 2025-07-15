from bookland.domain.repositories import UserRepository


class LogoutUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self) -> None:
        return await self._repository.logout()
