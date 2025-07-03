from bookland.domain.repositories.trope_repository import TropeRepository
from bookland.domain.entities import Trope


class GetAllTropesUseCase:
    def __init__(self, repository: TropeRepository):
        self._repository = repository

    async def execute(self) -> list[Trope]:
        return await self._repository.get_all()
