from bookland.infra.repositories.inmemory_repositories.in_memory_reading_in_progress_repository import (
    InMemoryReadingInProgressRepository,
)
from bookland.application.usecases.reading_in_progress.delete_reading_in_progress import (
    DeleteReadingInProgressUseCase,
)
from tests.factories.reading_in_progress_factory import create_reading_in_progress


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_delete_reading_in_progress_removes_reading_in_progress():
    repository = InMemoryReadingInProgressRepository()
    usecase = DeleteReadingInProgressUseCase(repository)

    reading_in_progress = create_reading_in_progress()
    await repository.create(reading_in_progress)

    retrieved_reading_in_progress = await usecase.execute(reading_in_progress.id)

    assert retrieved_reading_in_progress is None
