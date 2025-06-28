from bookland.infra.repositories.inmemory_repositories.in_memory_book_repository import (
    InMemoryBookRepository,
)
from bookland.application.usecases.book.soft_delete_book import SoftDeleteBookUseCase
from tests.factories.book_factory import create_book


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_soft_delete_book_removes_book():
    repository = InMemoryBookRepository()
    usecase = SoftDeleteBookUseCase(repository)

    book = create_book()
    await repository.create(book)

    await usecase.execute(book.id)

    assert book.is_deleted is True
