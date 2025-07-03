from abc import ABC, abstractmethod
from bookland.domain.entities import Genre


class GenreRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Genre]: ...
