from abc import ABC, abstractmethod
from bookland.domain.entities.criterion import Criterion


class CriterionRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Criterion]: ...

    @abstractmethod
    def get_by_id(self, criterion_id: str) -> Criterion | None: ...

    @abstractmethod
    def create(self, criterion: Criterion) -> None: ...

    @abstractmethod
    def update(self, criterion: Criterion) -> None: ...

    @abstractmethod
    def soft_delete(self, criterion_id: str) -> None: ...

    @abstractmethod
    def search(self, search_term: str) -> list[Criterion]: ...
