from bookland.domain.entities import Criterion
from bookland.domain.repositories import CriterionRepository


class CreateCriterionUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    async def execute(self, criterion: Criterion) -> Criterion:
        return await self._repository.create(criterion)
