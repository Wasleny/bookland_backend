from bookland.domain.repositories import TropeRepository
from bookland.domain.entities import Trope


class GetManyTropesByIdUseCase:
    def __init__(self, repository: TropeRepository):
        self._repository = repository

    async def execute(self, trope_ids: list) -> list[Trope]:
        return await self._repository.get_many_by_id(trope_ids)
