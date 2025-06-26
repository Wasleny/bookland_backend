from bookland.infra.repositories.in_memory_author_repository import (
    InMemoryAuthorRepository,
)
from bookland.usecases.author.get_author_by_id import GetAuthorByIdUseCase
from tests.factories.author_factory import create_author


def test_get_author_by_id_returns_author_when_found():
    repository = InMemoryAuthorRepository()
    usecase = GetAuthorByIdUseCase(repository)

    author1 = create_author()
    repository.create(author1)

    author_found = usecase.execute(author1.id)

    assert author1 == author_found


def test_get_author_by_id_returns_none_when_not_found():
    repository = InMemoryAuthorRepository()
    usecase = GetAuthorByIdUseCase(repository)

    author_found = usecase.execute('invalid-id')

    assert author_found is None
