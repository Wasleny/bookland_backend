from abc import ABC, abstractmethod
from bookland.domain.entities.reading_in_progress import ReadingInProgress


class ReadingInProgressRepository(ABC):
    @abstractmethod
    async def get_by_user(self, user_id: str) -> list[ReadingInProgress]: ...

    @abstractmethod
    async def get_by_user_and_book(
        self, user_id: str, book_id: str
    ) -> ReadingInProgress | None: ...

    @abstractmethod
    async def get_by_id(
        self, reading_in_progress_id: str
    ) -> ReadingInProgress | None: ...

    @abstractmethod
    async def create(
        self, reading_in_progress: ReadingInProgress
    ) -> ReadingInProgress: ...

    @abstractmethod
    async def update(
        self, reading_in_progress: ReadingInProgress
    ) -> ReadingInProgress | None: ...

    @abstractmethod
    async def delete(self, reading_in_progress_id: str) -> None: ...
