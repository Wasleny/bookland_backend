from bookland.domain.repositories.criterion_repository import CriterionRepository
from bookland.domain.entities.criterion import Criterion


class SearchCriteriaUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    def execute(self, search_term: str) -> list[Criterion]:
        return self._repository.search(search_term)
