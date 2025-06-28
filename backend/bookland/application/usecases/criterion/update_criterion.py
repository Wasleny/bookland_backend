from bookland.domain.entities.criterion import Criterion
from bookland.domain.repositories.criterion_repository import CriterionRepository


class UpdateCriterionUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    async def execute(self, criterion: Criterion) -> Criterion | None:
        return await self._repository.update(criterion)
