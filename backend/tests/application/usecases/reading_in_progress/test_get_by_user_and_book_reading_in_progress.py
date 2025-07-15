from bookland.infra.repositories import InMemoryReadingInProgressRepository
from bookland.application.usecases import GetReadingInProgressByUserAndBookUseCase
from tests.factories.reading_in_progress_factory import create_reading_in_progress


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_reading_in_progress_by_user_and_book_returns_book_when_found():
    repository = InMemoryReadingInProgressRepository()
    usecase = GetReadingInProgressByUserAndBookUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    await repository.create(reading_in_progress)

    reading_in_progress_found = await usecase.execute(
        reading_in_progress.user_id, reading_in_progress.book_id
    )

    assert reading_in_progress == reading_in_progress_found


@pytest.mark.asyncio
async def test_get_reading_in_progress_by_user_and_book_returns_none_when_not_found():
    repository = InMemoryReadingInProgressRepository()
    usecase = GetReadingInProgressByUserAndBookUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    await repository.create(reading_in_progress)

    reading_in_progress_found = await usecase.execute(
        "invalid-id", reading_in_progress.book_id
    )

    assert reading_in_progress_found is None
