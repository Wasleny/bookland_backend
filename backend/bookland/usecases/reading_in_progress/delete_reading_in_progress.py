from bookland.domain.repositories.reading_in_progress_repository import (
    ReadingInProgressRepository,
)


class DeleteReadingInProgressUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    def execute(self, reading_in_progress_id: str) -> None:
        self._repository.delete(reading_in_progress_id)
