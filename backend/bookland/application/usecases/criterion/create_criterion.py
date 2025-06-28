from bookland.domain.entities.criterion import Criterion
from bookland.domain.repositories.criterion_repository import CriterionRepository


class CreateCriterionUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    async def execute(self, criterion: Criterion) -> Criterion:
        return await self._repository.create(criterion)
