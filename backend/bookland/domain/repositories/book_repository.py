from abc import ABC, abstractmethod
from bookland.domain.entities.book import Book


class BookRepository(ABC):
    @abstractmethod
    async def get_all(self) -> list[Book]: ...

    @abstractmethod
    async def get_by_id(self, book_id: str) -> Book | None: ...

    @abstractmethod
    async def search(self, search_term: str) -> list[Book]: ...

    @abstractmethod
    async def create(self, book: Book) -> Book: ...

    @abstractmethod
    async def update(self, book: Book) -> Book | None: ...

    @abstractmethod
    async def soft_delete(self, book_id: str) -> None: ...
