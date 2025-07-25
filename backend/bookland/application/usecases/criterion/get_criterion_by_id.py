from bookland.domain.repositories import CriterionRepository
from bookland.domain.entities import Criterion


class GetCriterionByIdUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    async def execute(self, criterion_id: str) -> Criterion | None:
        return await self._repository.get_by_id(criterion_id)
