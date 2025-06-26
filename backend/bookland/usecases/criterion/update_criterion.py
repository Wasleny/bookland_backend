from bookland.domain.entities.criterion import Criterion
from bookland.domain.repositories.criterion_repository import CriterionRepository


class UpdateCriterionUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    def execute(self, criterion: Criterion) -> None:
        self._repository.update(criterion)
