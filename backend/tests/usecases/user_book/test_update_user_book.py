from bookland.infra.repositories.in_memory_user_book_repository import (
    InMemoryUserBookRepository,
)
from bookland.usecases.user_book.update_user_book import UpdateUserBookUseCase
from tests.factories.user_book_factory import create_user_book
from bookland.domain.value_objects.label_vo import Label


def test_update_user_book_updates_user_book_data():
    repository = InMemoryUserBookRepository()
    usecase = UpdateUserBookUseCase(repository)

    user_book = create_user_book()
    repository.create(user_book)

    updated_data = create_user_book(
        id=user_book.id, default_bookshelf=Label("Quero ler")
    )

    usecase.execute(updated_data)

    updated_user_book = repository.get_by_id(user_book.id)

    assert updated_user_book.default_bookshelf.value == "Quero Ler"
