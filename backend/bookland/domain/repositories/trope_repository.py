from abc import ABC, abstractmethod
from bookland.domain.entities import Trope


class TropeRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Trope]: ...
