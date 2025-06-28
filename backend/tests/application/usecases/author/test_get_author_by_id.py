from bookland.infra.repositories.inmemory_repositories.in_memory_author_repository import (
    InMemoryAuthorRepository,
)
from bookland.application.usecases.author.get_author_by_id import GetAuthorByIdUseCase
from tests.factories.author_factory import create_author


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_author_by_id_returns_author_when_found():
    repository = InMemoryAuthorRepository()
    usecase = GetAuthorByIdUseCase(repository)

    author1 = create_author()
    await repository.create(author1)

    author_found = await usecase.execute(author1.id)

    assert author1 == author_found


@pytest.mark.asyncio
async def test_get_author_by_id_returns_none_when_not_found():
    repository = InMemoryAuthorRepository()
    usecase = GetAuthorByIdUseCase(repository)

    author_found = await usecase.execute("invalid-id")

    assert author_found is None
