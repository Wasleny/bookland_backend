from bookland.infra.repositories.inmemory_repositories.in_memory_reading_in_progress_repository import (
    InMemoryReadingInProgressRepository,
)
from bookland.application.usecases.reading_in_progress.create_reading_in_progress import (
    CreateReadingInProgressUseCase,
)
from tests.factories.reading_in_progress_factory import create_reading_in_progress


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_create_reading_in_progress_creates_reading_in_progress_successfully():
    repository = InMemoryReadingInProgressRepository()
    usecase = CreateReadingInProgressUseCase(repository)
    reading_in_progress = create_reading_in_progress()

    retrieved_reading_in_progress = await usecase.execute(reading_in_progress)

    assert retrieved_reading_in_progress == reading_in_progress
