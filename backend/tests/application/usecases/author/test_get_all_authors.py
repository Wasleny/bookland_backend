from bookland.infra.repositories import InMemoryAuthorRepository
from bookland.application.usecases import GetAllAuthorsUseCase
from tests.factories.author_factory import create_author

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_all_authors_returns_all_authors():
    repository = InMemoryAuthorRepository()
    usecase = GetAllAuthorsUseCase(repository)

    author1 = create_author()
    author2 = create_author()
    await repository.create(author1)
    await repository.create(author2)

    authors = await usecase.execute()

    assert len(authors) == 2
    assert author1 in authors
    assert author2 in authors
