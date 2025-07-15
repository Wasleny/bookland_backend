from bookland.infra.repositories import InMemoryAuthorRepository
from bookland.application.usecases import SoftDeleteAuthorUseCase
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


@pytest.mark.asyncio
async def test_soft_delete_author_not_find_author_returns_none():
    repository = InMemoryAuthorRepository()
    usecase = SoftDeleteAuthorUseCase(repository)

    deleted_author = await usecase.execute("1")

    assert deleted_author is None
