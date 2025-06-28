from abc import ABC, abstractmethod
from bookland.domain.entities.review import Review


class ReviewRepository(ABC):
    @abstractmethod
    async def get_by_id(self, review_id: str) -> Review | None: ...

    @abstractmethod
    async def get_by_book(self, book_id: str) -> list[Review]: ...

    @abstractmethod
    async def get_by_user_and_book(self, user_id: str, book_id: str) -> list[Review]: ...

    @abstractmethod
    async def get_most_recent_reading(self, user_id: str, book_id: str) -> Review | None: ...

    @abstractmethod
    async def create(self, review: Review) -> Review: ...

    @abstractmethod
    async def update(self, review: Review) -> Review | None: ...

    @abstractmethod
    async def delete(self, review_id: str) -> None: ...

    @abstractmethod
    async def delete_all_for_user_and_book(self, user_id: str, book_id: str) -> None: ...
