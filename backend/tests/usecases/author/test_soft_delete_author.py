from bookland.infra.repositories.in_memory_author_repository import (
    InMemoryAuthorRepository,
)
from bookland.usecases.author.soft_delete_author import SoftDeleteAuthorUseCase
from tests.factories.author_factory import create_author


def test_soft_delete_author_removes_author():
    repository = InMemoryAuthorRepository()
    usecase = SoftDeleteAuthorUseCase(repository)

    author = create_author()
    repository.create(author)

    usecase.execute(author.id)

    assert repository.get_by_id(author.id) is None
