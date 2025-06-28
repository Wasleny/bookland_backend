from bookland.infra.repositories.inmemory_repositories.in_memory_user_book_repository import (
    InMemoryUserBookRepository,
)
from bookland.application.usecases.user_book.update_user_book import (
    UpdateUserBookUseCase,
)
from tests.factories.user_book_factory import create_user_book
from bookland.domain.value_objects.label_vo import Label


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_update_user_book_updates_user_book_data():
    repository = InMemoryUserBookRepository()
    usecase = UpdateUserBookUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    updated_data = create_user_book(
        id=user_book.id, default_bookshelf=Label("Quero ler")
    )

    updated_user_book = await usecase.execute(updated_data)

    assert updated_user_book.default_bookshelf.value == "Quero Ler"


@pytest.mark.asyncio
async def test_update_user_book_not_updates_when_not_found():
    repository = InMemoryUserBookRepository()
    usecase = UpdateUserBookUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    updated_data = create_user_book()

    updated_user_book = await usecase.execute(updated_data)

    assert updated_user_book is None
