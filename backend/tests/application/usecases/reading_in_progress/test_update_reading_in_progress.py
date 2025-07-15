from bookland.infra.repositories import InMemoryReadingInProgressRepository
from bookland.application.usecases import UpdateReadingInProgressUseCase
from tests.factories.reading_in_progress_factory import create_reading_in_progress


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_update_reading_in_progress_updates_reading_in_progress_data():
    repository = InMemoryReadingInProgressRepository()
    usecase = UpdateReadingInProgressUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    await repository.create(reading_in_progress)

    updated_data = create_reading_in_progress(id=reading_in_progress.id, progress=60)

    updated_reading_in_progress = await usecase.execute(updated_data)

    assert updated_reading_in_progress.progress == 60


@pytest.mark.asyncio
async def test_update_reading_in_progress_not_updates_when_not_found():
    repository = InMemoryReadingInProgressRepository()
    usecase = UpdateReadingInProgressUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    await repository.create(reading_in_progress)

    updated_data = create_reading_in_progress()

    updated_reading_in_progress = await usecase.execute(updated_data)

    assert updated_reading_in_progress is None
