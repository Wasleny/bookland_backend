from bookland.infra.repositories.in_memory_reading_in_progress_repository import (
    InMemoryReadingInProgressRepository,
)
from bookland.usecases.reading_in_progress.delete_reading_in_progress import (
    DeleteReadingInProgressUseCase,
)
from tests.factories.reading_in_progress_factory import create_reading_in_progress


def test_delete_reading_in_progress_removes_reading_in_progress():
    repository = InMemoryReadingInProgressRepository()
    usecase = DeleteReadingInProgressUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    repository.create(reading_in_progress)

    usecase.execute(reading_in_progress.id)

    assert repository.get_by_id(reading_in_progress.id) is None
