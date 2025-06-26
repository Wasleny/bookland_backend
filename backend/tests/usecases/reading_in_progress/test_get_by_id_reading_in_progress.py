from bookland.infra.repositories.in_memory_reading_in_progress_repository import (
    InMemoryReadingInProgressRepository,
)
from bookland.usecases.reading_in_progress.get_reading_in_progress_by_id import (
    GetReadingInProgressByIdUseCase,
)
from tests.factories.reading_in_progress_factory import create_reading_in_progress


def test_get_reading_in_progress_by_id_returns_reading_in_progress_when_found():
    repository = InMemoryReadingInProgressRepository()
    usecase = GetReadingInProgressByIdUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    repository.create(reading_in_progress)

    reading_in_progress_found = usecase.execute(reading_in_progress.id)

    assert reading_in_progress == reading_in_progress_found


def test_get_reading_in_progress_by_id_returns_none_when_not_found():
    repository = InMemoryReadingInProgressRepository()
    usecase = GetReadingInProgressByIdUseCase(repository)

    reading_in_progress_found = usecase.execute("invalid-id")

    assert reading_in_progress_found is None
