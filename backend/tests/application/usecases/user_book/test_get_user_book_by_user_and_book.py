from bookland.infra.repositories import InMemoryUserBookRepository
from bookland.application.usecases import GetUserBookByUserAndBookUseCase
from tests.factories.user_book_factory import create_user_book

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_user_book_by_user_and_book_returns_user_book():
    repository = InMemoryUserBookRepository()
    usecase = GetUserBookByUserAndBookUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    user_book_found = await usecase.execute(user_book.user_id, user_book.book_id)

    assert user_book == user_book_found


@pytest.mark.asyncio
async def test_get_user_book_by_user_and_book_returns_none_when_not_found():
    repository = InMemoryUserBookRepository()
    usecase = GetUserBookByUserAndBookUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    user_book_found = await usecase.execute("invalid-id", user_book.book_id)

    assert user_book_found is None
