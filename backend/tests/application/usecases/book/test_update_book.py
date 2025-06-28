from bookland.infra.repositories.inmemory_repositories.in_memory_book_repository import (
    InMemoryBookRepository,
)
from bookland.application.usecases.book.update_book import UpdateBookUseCase
from tests.factories.book_factory import create_book


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_update_book_updates_book_data():
    repository = InMemoryBookRepository()
    usecase = UpdateBookUseCase(repository)

    book = create_book()
    await repository.create(book)

    updated_data = create_book(id=book.id, pages=400)

    updated_book = await usecase.execute(updated_data)

    assert updated_book.pages == 400
    assert updated_book.title == "Trono de Vidro"


@pytest.mark.asyncio
async def test_update_book_not_updates_when_not_found():
    repository = InMemoryBookRepository()
    usecase = UpdateBookUseCase(repository)

    book = create_book()
    await repository.create(book)

    updated_data = create_book()

    updated_book = await usecase.execute(updated_data)

    assert updated_book is None
