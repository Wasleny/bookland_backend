from abc import ABC, abstractmethod
from bookland.domain.entities.review import Review


class ReviewRepository(ABC):
    @abstractmethod
    def get_by_id(self, review_id: str) -> Review | None: ...

    @abstractmethod
    def get_by_book(self, book_id: str) -> list[Review]: ...

    @abstractmethod
    def get_by_user_and_book(self, user_id: str, book_id: str) -> list[Review]: ...

    @abstractmethod
    def get_most_recent_reading(self, user_id: str, book_id: str) -> Review | None: ...

    @abstractmethod
    def create(self, review: Review) -> None: ...

    @abstractmethod
    def update(self, review: Review) -> None: ...

    @abstractmethod
    def delete(self, review_id: str) -> None: ...

    @abstractmethod
    def delete_all_for_user_and_book(self, user_id: str, book_id: str) -> None: ...
