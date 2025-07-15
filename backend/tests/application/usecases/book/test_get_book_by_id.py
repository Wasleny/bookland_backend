from bookland.infra.repositories import InMemoryBookRepository
from bookland.application.usecases import GetBookByIdUseCase
from tests.factories.book_factory import create_book


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_book_by_id_returns_book_when_found():
    repository = InMemoryBookRepository()
    usecase = GetBookByIdUseCase(repository)

    book = create_book()
    await repository.create(book)

    book_found = await usecase.execute(book.id)

    assert book == book_found


@pytest.mark.asyncio
async def test_get_book_by_id_returns_none_when_not_found():
    repository = InMemoryBookRepository()
    usecase = GetBookByIdUseCase(repository)

    book_found = await usecase.execute("invalid-id")

    assert book_found is None
