from bookland.infra.repositories import InMemoryBookRepository
from bookland.application.usecases import CreateBookUseCase
from tests.factories.book_factory import create_book


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_create_book_creates_book_successfully():
    repository = InMemoryBookRepository()
    usecase = CreateBookUseCase(repository)
    book = create_book()

    retrieved_book = await usecase.execute(book)

    assert retrieved_book == book
