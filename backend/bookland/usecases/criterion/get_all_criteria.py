from bookland.domain.repositories.criterion_repository import CriterionRepository
from bookland.domain.entities.criterion import Criterion


class GetAllCriteriaUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    def execute(self) -> list[Criterion]:
        return self._repository.get_all()
