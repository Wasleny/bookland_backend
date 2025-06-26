from bookland.infra.repositories.in_memory_author_repository import (
    InMemoryAuthorRepository,
)
from bookland.usecases.author.create_author import CreateAuthorUseCase
from tests.factories.author_factory import create_author


def test_create_author_creates_author_successfully():
    repository = InMemoryAuthorRepository()
    usecase = CreateAuthorUseCase(repository)
    author = create_author()

    usecase.execute(author)

    assert repository.get_by_id(author.id) == author
