from abc import ABC, abstractmethod

from bookland.domain.entities import Author


class AuthorRepository(ABC):
    @abstractmethod
    async def create(self, author: Author) -> Author: ...

    @abstractmethod
    async def get_by_id(self, author_id: str) -> Author | None: ...

    @abstractmethod
    async def get_all(self) -> list[Author]: ...

    @abstractmethod
    async def update(self, author: Author) -> Author | None: ...

    @abstractmethod
    async def soft_delete(self, author_id: str) -> Author | None: ...
