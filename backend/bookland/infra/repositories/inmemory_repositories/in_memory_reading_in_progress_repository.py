from bookland.domain.entities.reading_in_progress import ReadingInProgress
from bookland.domain.repositories.reading_in_progress_repository import (
    ReadingInProgressRepository,
)


class InMemoryReadingInProgressRepository(ReadingInProgressRepository):
    def __init__(self) -> None:
        self._readings_in_progress: dict[str, ReadingInProgress] = {}

    async def get_by_id(self, reading_in_progress_id: str) -> ReadingInProgress | None:
        return self._readings_in_progress.get(reading_in_progress_id)

    async def get_by_user(self, user_id: str) -> list[ReadingInProgress]:
        return [
            reading_in_progress
            for reading_in_progress in self._readings_in_progress.values()
            if reading_in_progress.user_id == user_id
        ]

    async def get_by_user_and_book(
        self, user_id: str, book_id: str
    ) -> ReadingInProgress | None:
        for reading_in_progress in self._readings_in_progress.values():
            if (
                reading_in_progress.book_id == book_id
                and reading_in_progress.user_id == user_id
            ):
                return reading_in_progress

        return None

    async def create(self, reading_in_progress: ReadingInProgress) -> ReadingInProgress:
        self._readings_in_progress[reading_in_progress.id] = reading_in_progress

        return reading_in_progress

    async def update(
        self, reading_in_progress: ReadingInProgress
    ) -> ReadingInProgress | None:
        if reading_in_progress.id in self._readings_in_progress:
            self._readings_in_progress[reading_in_progress.id] = reading_in_progress
            return reading_in_progress

        return None

    async def delete(self, reading_in_progress_id: str) -> None:
        self._readings_in_progress.pop(reading_in_progress_id, None)
