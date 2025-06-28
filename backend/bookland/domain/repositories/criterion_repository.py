from abc import ABC, abstractmethod
from bookland.domain.entities.criterion import Criterion


class CriterionRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Criterion]: ...

    @abstractmethod
    async def get_by_id(self, criterion_id: str) -> Criterion | None: ...

    @abstractmethod
    async def create(self, criterion: Criterion) -> Criterion: ...

    @abstractmethod
    async def update(self, criterion: Criterion) -> Criterion | None: ...

    @abstractmethod
    async def soft_delete(self, criterion_id: str) -> None: ...

    @abstractmethod
    async def search(self, search_term: str) -> list[Criterion]: ...
