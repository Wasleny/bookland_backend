from abc import ABC, abstractmethod
from bookland.domain.entities.user_book import UserBook


class UserBookRepository(ABC):
    @abstractmethod
    def get_by_user(self, user_id: str) -> list[UserBook]: ...

    @abstractmethod
    def get_by_user_and_book(self, user_id: str, book_id: str) -> UserBook | None: ...

    @abstractmethod
    def create(self, user_book: UserBook) -> None: ...

    @abstractmethod
    def update(self, user_book: UserBook) -> None: ...

    @abstractmethod
    def delete(self, user_book_id: str) -> None: ...

    @abstractmethod
    def get_by_id(self, user_book_id: str) -> UserBook | None: ...
