from bookland.infra.repositories import InMemoryBookRepository
from bookland.application.usecases.book.get_all_books import GetAllBooksUseCase
from tests.factories.book_factory import create_book


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_all_books_returns_all_books():
    repository = InMemoryBookRepository()
    usecase = GetAllBooksUseCase(repository)

    book1 = create_book()
    book2 = create_book()
    await repository.create(book1)
    await repository.create(book2)

    books = await usecase.execute()

    assert len(books) == 2
    assert book1 in books
    assert book2 in books
