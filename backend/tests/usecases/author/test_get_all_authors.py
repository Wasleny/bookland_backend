from bookland.infra.repositories.in_memory_author_repository import (
    InMemoryAuthorRepository,
)
from bookland.usecases.author.get_all_authors import GetAllAuthorsUseCase
from tests.factories.author_factory import create_author


def test_get_all_authors_returns_all_authors():
    repository = InMemoryAuthorRepository()
    usecase = GetAllAuthorsUseCase(repository)

    author1 = create_author()
    author2 = create_author()
    repository.create(author1)
    repository.create(author2)

    authors = usecase.execute()

    assert len(authors) == 2
    assert author1 in authors
    assert author2 in authors
