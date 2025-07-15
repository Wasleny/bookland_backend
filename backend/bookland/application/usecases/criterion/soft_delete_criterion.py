from bookland.domain.repositories import CriterionRepository
from bookland.domain.entities import Criterion


class SoftDeleteCriterionUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    async def execute(self, criterion_id: str) -> Criterion | None:
        return await self._repository.soft_delete(criterion_id)
