from bookland.infra.repositories.in_memory_user_book_repository import (
    InMemoryUserBookRepository,
)
from bookland.usecases.user_book.get_user_book_by_id import GetUserBookByIdUseCase
from tests.factories.user_book_factory import create_user_book


def test_get_user_book_by_id_returns_user_book():
    repository = InMemoryUserBookRepository()
    usecase = GetUserBookByIdUseCase(repository)

    user_book = create_user_book()
    repository.create(user_book)

    user_book_found = usecase.execute(user_book.id)

    assert user_book_found == user_book


def test_get_user_book_by_id_returns_none_when_not_found():
    repository = InMemoryUserBookRepository()
    usecase = GetUserBookByIdUseCase(repository)

    user_book = create_user_book()
    repository.create(user_book)

    user_book_found = usecase.execute("invalid-id")

    assert user_book_found is None
