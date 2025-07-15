from bookland.infra.repositories import InMemoryUserBookRepository
from bookland.application.usecases import DeleteUserBookUseCase
from tests.factories.user_book_factory import create_user_book

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_delete_user_book_removes_user_book():
    repository = InMemoryUserBookRepository()
    usecase = DeleteUserBookUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    await usecase.execute(user_book.id)

    retrieved_user_book = await repository.get_by_id(user_book.id)

    assert retrieved_user_book is None


@pytest.mark.asyncio
async def test_delete_user_book_removes_not_find_returns_none():
    repository = InMemoryUserBookRepository()
    usecase = DeleteUserBookUseCase(repository)

    deleted_user_book = await usecase.execute('1')

    assert deleted_user_book is None
