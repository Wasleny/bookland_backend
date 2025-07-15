from abc import ABC, abstractmethod

from bookland.domain.entities import UserBook


class UserBookRepository(ABC):
    @abstractmethod
    async def get_by_user(self, user_id: str) -> list[UserBook]: ...

    @abstractmethod
    async def get_by_user_and_book(
        self, user_id: str, book_id: str
    ) -> UserBook | None: ...

    @abstractmethod
    async def create(self, user_book: UserBook) -> UserBook: ...

    @abstractmethod
    async def update(self, user_book: UserBook) -> UserBook | None: ...

    @abstractmethod
    async def delete(self, user_book_id: str) -> UserBook | None: ...

    @abstractmethod
    async def get_by_id(self, user_book_id: str) -> UserBook | None: ...
