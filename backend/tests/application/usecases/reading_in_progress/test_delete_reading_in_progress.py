from bookland.infra.repositories import InMemoryReadingInProgressRepository
from bookland.application.usecases import DeleteReadingInProgressUseCase
from tests.factories.reading_in_progress_factory import create_reading_in_progress


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_delete_reading_in_progress_removes_reading_in_progress():
    repository = InMemoryReadingInProgressRepository()
    usecase = DeleteReadingInProgressUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    await repository.create(reading_in_progress)

    await usecase.execute(reading_in_progress.id)

    retrieved_reading_in_progress = await repository.get_by_id(reading_in_progress.id)

    assert retrieved_reading_in_progress is None


@pytest.mark.asyncio
async def test_delete_reading_in_progress_not_find_reading_in_progress_returns_none():
    repository = InMemoryReadingInProgressRepository()
    usecase = DeleteReadingInProgressUseCase(repository)

    deleted_reading = await usecase.execute("1")

    assert deleted_reading is None
