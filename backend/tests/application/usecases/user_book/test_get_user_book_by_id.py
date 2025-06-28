from bookland.infra.repositories.inmemory_repositories.in_memory_user_book_repository import (
    InMemoryUserBookRepository,
)
from bookland.application.usecases.user_book.get_user_book_by_id import (
    GetUserBookByIdUseCase,
)
from tests.factories.user_book_factory import create_user_book


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_user_book_by_id_returns_user_book():
    repository = InMemoryUserBookRepository()
    usecase = GetUserBookByIdUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    user_book_found = await usecase.execute(user_book.id)

    assert user_book_found == user_book


@pytest.mark.asyncio
async def test_get_user_book_by_id_returns_none_when_not_found():
    repository = InMemoryUserBookRepository()
    usecase = GetUserBookByIdUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    user_book_found = await usecase.execute("invalid-id")

    assert user_book_found is None
