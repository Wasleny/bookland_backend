from bookland.infra.repositories.in_memory_reading_in_progress_repository import (
    InMemoryReadingInProgressRepository,
)
from bookland.usecases.reading_in_progress.create_reading_in_progress import (
    CreateReadingInProgressUseCase,
)
from tests.factories.reading_in_progress_factory import create_reading_in_progress


def test_create_reading_in_progress_creates_reading_in_progress_successfully():
    repository = InMemoryReadingInProgressRepository()
    usecase = CreateReadingInProgressUseCase(repository)
    reading_in_progress = create_reading_in_progress()

    usecase.execute(reading_in_progress)

    assert repository.get_by_id(reading_in_progress.id) == reading_in_progress
