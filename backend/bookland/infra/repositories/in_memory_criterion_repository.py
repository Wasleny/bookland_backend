from bookland.domain.entities.criterion import Criterion
from bookland.domain.repositories.criterion_repository import CriterionRepository
from bookland.utils.text_utils import normalize_text


class InMemoryCriterionRepository(CriterionRepository):
    def __init__(self):
        self._criteria: dict[str, Criterion] = {}

    def get_all(self) -> list[Criterion]:
        return [
            criterion
            for criterion in self._criteria.values()
            if not criterion.is_deleted
        ]

    def get_by_id(self, criterion_id: str) -> Criterion | None:
        for criterion in self._criteria.values():
            if not criterion.is_deleted and criterion.id == criterion_id:
                return criterion

        return None

    def create(self, criterion: Criterion) -> None:
        self._criteria[criterion.id] = criterion

    def update(self, criterion: Criterion) -> None:
        if criterion.id in self._criteria:
            self._criteria[criterion.id] = criterion

    def soft_delete(self, criterion_id: str) -> None:
        criterion = self._criteria.get(criterion_id)

        if criterion:
            criterion.soft_delete()

    def search(self, search_term: str) -> list[Criterion]:
        normalized_search = normalize_text(search_term)

        return [
            criterion
            for criterion in self._criteria.values()
            if not criterion.is_deleted
            and normalized_search in normalize_text(criterion.name.value)
        ]
