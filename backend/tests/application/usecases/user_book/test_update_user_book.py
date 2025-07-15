from bookland.infra.repositories import InMemoryUserBookRepository
from bookland.application.usecases import UpdateUserBookUseCase
from tests.factories.user_book_factory import create_user_book
from bookland.domain.value_objects import Label

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_update_user_book_updates_user_book_data():
    repository = InMemoryUserBookRepository()
    usecase = UpdateUserBookUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    updated_data = create_user_book(id=user_book.id, default_bookshelf_id="2")

    updated_user_book = await usecase.execute(updated_data)

    assert updated_user_book.default_bookshelf_id == "2"


@pytest.mark.asyncio
async def test_update_user_book_not_updates_when_not_found():
    repository = InMemoryUserBookRepository()
    usecase = UpdateUserBookUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    updated_data = create_user_book()

    updated_user_book = await usecase.execute(updated_data)

    assert updated_user_book is None
