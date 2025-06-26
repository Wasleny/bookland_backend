from bookland.infra.repositories.in_memory_reading_in_progress_repository import (
    InMemoryReadingInProgressRepository,
)
from bookland.usecases.reading_in_progress.update_reading_in_progress import (
    UpdateReadingInProgressUseCase,
)
from tests.factories.reading_in_progress_factory import create_reading_in_progress


def test_update_reading_in_progress_updates_reading_in_progress_data():
    repository = InMemoryReadingInProgressRepository()
    usecase = UpdateReadingInProgressUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    repository.create(reading_in_progress)

    updated_data = create_reading_in_progress(id=reading_in_progress.id, progress=60)

    usecase.execute(updated_data)

    updated_reading_in_progress = repository.get_by_id(reading_in_progress.id)

    assert updated_reading_in_progress.progress == 60
