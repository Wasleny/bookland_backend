from bookland.domain.repositories.criterion_repository import CriterionRepository
from bookland.domain.entities.criterion import Criterion


class GetAllCriteriaUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    async def execute(self, user_id: str) -> list[Criterion]:
        return await self._repository.get_all(user_id)
