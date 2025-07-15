from bookland.domain.entities import UserBook
from bookland.domain.repositories import UserBookRepository


class GetUserBookByUserUseCase:
    def __init__(self, repository: UserBookRepository):
        self._repository = repository

    async def execute(self, user_id: str) -> list[UserBook]:
        return await self._repository.get_by_user(user_id)
