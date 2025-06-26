from bookland.infra.repositories.in_memory_author_repository import (
    InMemoryAuthorRepository,
)
from bookland.usecases.author.update_author import UpdateAuthorUseCase
from tests.factories.author_factory import create_author


def test_update_author_updates_author_data():
    repository = InMemoryAuthorRepository()
    usecase = UpdateAuthorUseCase(repository)

    author = create_author()
    repository.create(author)

    updated_data = create_author(
        id=author.id, name=author.name, nationality="Estados Unidos"
    )

    usecase.execute(updated_data)

    updated_author = repository.get_by_id(author.id)

    assert updated_author.nationality == "Estados Unidos"
    assert updated_author.name.value == author.name.value
