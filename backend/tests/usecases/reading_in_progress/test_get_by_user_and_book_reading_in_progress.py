from bookland.infra.repositories.in_memory_reading_in_progress_repository import (
    InMemoryReadingInProgressRepository,
)
from bookland.usecases.reading_in_progress.get_reading_in_progress_by_user_and_book import (
    GetReadingInProgressByUserAndBookUseCase,
)
from tests.factories.reading_in_progress_factory import create_reading_in_progress


def test_get_reading_in_progress_by_user_and_book_returns_book_when_found():
    repository = InMemoryReadingInProgressRepository()
    usecase = GetReadingInProgressByUserAndBookUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    repository.create(reading_in_progress)

    reading_in_progress_found = usecase.execute(reading_in_progress.user_id, reading_in_progress.book_id)

    assert reading_in_progress == reading_in_progress_found


def test_get_reading_in_progress_by_user_and_book_returns_none_when_not_found():
    repository = InMemoryReadingInProgressRepository()
    usecase = GetReadingInProgressByUserAndBookUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    repository.create(reading_in_progress)
    
    reading_in_progress_found = usecase.execute("invalid-id", reading_in_progress.book_id)

    assert reading_in_progress_found is None
