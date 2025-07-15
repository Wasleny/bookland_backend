from bookland.domain.entities import Criterion
from bookland.domain.repositories import CriterionRepository
from bookland.utils.text_utils import normalize_text


class InMemoryCriterionRepository(CriterionRepository):
    def __init__(self) -> None:
        self._criteria: dict[str, Criterion] = {}

    async def get_all(self, user_id: str) -> list[Criterion]:
        return [
            criterion
            for criterion in self._criteria.values()
            if not criterion.is_deleted and criterion.user_id == user_id
        ]

    async def get_by_id(self, criterion_id: str) -> Criterion | None:
        for criterion in self._criteria.values():
            if not criterion.is_deleted and criterion.id == criterion_id:
                return criterion

        return None

    async def create(self, criterion: Criterion) -> Criterion:
        self._criteria[criterion.id] = criterion

        return criterion

    async def update(self, criterion: Criterion) -> Criterion | None:
        if criterion.id in self._criteria:
            self._criteria[criterion.id] = criterion
            return criterion

        return None

    async def soft_delete(self, criterion_id: str) -> Criterion | None:
        criterion = self._criteria.get(criterion_id)

        if criterion:
            criterion.soft_delete()
            return criterion

        return None

    async def search(self, search_term: str, user_id: str) -> list[Criterion]:
        normalized_search = normalize_text(search_term)

        return [
            criterion
            for criterion in self._criteria.values()
            if not criterion.is_deleted
            and criterion.user_id == user_id
            and normalized_search in normalize_text(criterion.name.value)
        ]
