from bookland.domain.repositories.criterion_repository import CriterionRepository
from bookland.domain.entities.criterion import Criterion


class SearchCriteriaUseCase:
    def __init__(self, repository: CriterionRepository):
        self._repository = repository

    async def execute(self, search_term: str, user_id: str) -> list[Criterion]:
        return await self._repository.search(search_term, user_id)
