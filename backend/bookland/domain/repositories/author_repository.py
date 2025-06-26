from abc import ABC, abstractmethod
from bookland.domain.entities.author import Author


class AuthorRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Author]: ...

    @abstractmethod
    def get_by_id(self, author_id: str) -> Author | None: ...

    @abstractmethod
    def create(self, author: Author) -> None: ...

    @abstractmethod
    def update(self, author: Author) -> None: ...

    @abstractmethod
    def soft_delete(self, author_id: str) -> None: ...
