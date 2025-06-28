from bookland.infra.repositories.inmemory_repositories.in_memory_author_repository import (
    InMemoryAuthorRepository,
)
from bookland.application.usecases.author.create_author import CreateAuthorUseCase
from tests.factories.author_factory import create_author

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_create_author_creates_author_successfully():
    repository = InMemoryAuthorRepository()
    usecase = CreateAuthorUseCase(repository)
    author = create_author()

    retrieved_author = await usecase.execute(author)

    assert retrieved_author == author
