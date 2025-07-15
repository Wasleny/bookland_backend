from abc import ABC, abstractmethod

from bookland.domain.entities import Bookshelf


class BookshelfRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Bookshelf]: ...
