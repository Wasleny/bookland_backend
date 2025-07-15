from bookland.infra.repositories import InMemoryUserBookRepository
from bookland.application.usecases import GetUserBookByUserUseCase
from tests.factories.user_book_factory import create_user_book

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_user_book_by_user_returns_user_book():
    repository = InMemoryUserBookRepository()
    usecase = GetUserBookByUserUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    user_book_found = await usecase.execute(user_book.user_id)

    assert len(user_book_found) == 1


@pytest.mark.asyncio
async def test_get_user_book_by_user_returns_none_when_not_found():
    repository = InMemoryUserBookRepository()
    usecase = GetUserBookByUserUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    user_book_found = await usecase.execute("invalid-id")

    assert len(user_book_found) == 0
