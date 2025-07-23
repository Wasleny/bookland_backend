from abc import ABC, abstractmethod

from bookland.domain.entities import Genre


class GenreRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Genre]: ...

    @abstractmethod
    async def get_many_by_id(self, genre_ids: list[str]) -> list[Genre]: ...

    @abstractmethod
    async def get_by_id(self, genre_id: str) -> Genre | None: ...
