from bookland.infra.repositories.inmemory_repositories.in_memory_author_repository import (
    InMemoryAuthorRepository,
)
from bookland.application.usecases.author.update_author import UpdateAuthorUseCase
from tests.factories.author_factory import create_author


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_update_author_updates_author_data():
    repository = InMemoryAuthorRepository()
    usecase = UpdateAuthorUseCase(repository)

    author = create_author()
    await repository.create(author)

    updated_data = create_author(
        id=author.id, name=author.name, nationality="Estados Unidos"
    )

    updated_author = await usecase.execute(updated_data)

    assert updated_author.nationality == "Estados Unidos"
    assert updated_author.name.value == author.name.value


@pytest.mark.asyncio
async def test_update_author_not_updates_when_not_found():
    repository = InMemoryAuthorRepository()
    usecase = UpdateAuthorUseCase(repository)

    author = create_author()
    await repository.create(author)

    updated_data = create_author()

    updated_author = await usecase.execute(updated_data)

    assert updated_author is None
