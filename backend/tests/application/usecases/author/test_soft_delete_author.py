from bookland.infra.repositories.inmemory_repositories.in_memory_author_repository import (
    InMemoryAuthorRepository,
)
from bookland.application.usecases.author.soft_delete_author import (
    SoftDeleteAuthorUseCase,
)
from tests.factories.author_factory import create_author


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_soft_delete_author_removes_author():
    repository = InMemoryAuthorRepository()
    usecase = SoftDeleteAuthorUseCase(repository)

    author = create_author()
    await repository.create(author)

    await usecase.execute(author.id)

    assert author.is_deleted is True
