from bookland.domain.repositories.criterion_repository import CriterionRepository


class SoftDeleteCriterionUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    async def execute(self, criterion_id: str) -> None:
        await self._repository.soft_delete(criterion_id)
