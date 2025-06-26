from bookland.infra.repositories.in_memory_user_book_repository import (
    InMemoryUserBookRepository,
)
from bookland.usecases.user_book.delete_user_book import DeleteUserBookUseCase
from tests.factories.user_book_factory import create_user_book


def test_delete_user_book_removes_user_book():
    repository = InMemoryUserBookRepository()
    usecase = DeleteUserBookUseCase(repository)

    user_book = create_user_book()
    repository.create(user_book)

    usecase.execute(user_book.id)

    assert repository.get_by_id(user_book.id) is None
