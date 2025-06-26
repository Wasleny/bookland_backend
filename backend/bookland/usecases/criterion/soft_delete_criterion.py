from bookland.domain.repositories.criterion_repository import CriterionRepository


class SoftDeleteCriterionUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    def execute(self, criterion_id: str) -> None:
        self._repository.soft_delete(criterion_id)
