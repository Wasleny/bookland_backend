from bookland.domain.entities.reading_in_progress import ReadingInProgress
from bookland.domain.repositories.reading_in_progress_repository import (
    ReadingInProgressRepository,
)


class GetReadingInProgressByUserUseCase:
    def __init__(self, repository: ReadingInProgressRepository):
        self._repository = repository

    def execute(self, user_id: str) -> list[ReadingInProgress]:
        return self._repository.get_by_user(user_id)
