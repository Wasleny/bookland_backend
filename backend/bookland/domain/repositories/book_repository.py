from abc import ABC, abstractmethod
from bookland.domain.entities.book import Book


class BookRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Book]: ...

    @abstractmethod
    def get_by_id(self, book_id: str) -> Book | None: ...

    @abstractmethod
    def search(self, search_term: str) -> list[Book]: ...

    @abstractmethod
    def create(self, book: Book) -> None: ...

    @abstractmethod
    def update(self, book: Book) -> None: ...

    @abstractmethod
    def soft_delete(self, book_id: str) -> None: ...
