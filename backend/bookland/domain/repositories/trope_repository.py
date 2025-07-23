from abc import ABC, abstractmethod
from bookland.domain.entities import Trope


class TropeRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Trope]: ...

    @abstractmethod
    async def get_many_by_id(self, tropes_id: list[str]) -> list[Trope]: ...
