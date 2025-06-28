from bookland.infra.repositories.inmemory_repositories.in_memory_book_repository import (
    InMemoryBookRepository,
)
from bookland.application.usecases.book.search_books import SearchBooksUseCase
from tests.factories.book_factory import create_book


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_search_books_matches_search():
    repository = InMemoryBookRepository()
    usecase = SearchBooksUseCase(repository)

    book = create_book()
    await repository.create(book)

    books_found = await usecase.execute("Trono")

    assert len(books_found) == 1


@pytest.mark.asyncio
async def test_search_books_returns_empty_when_no_match():
    repository = InMemoryBookRepository()
    usecase = SearchBooksUseCase(repository)

    book = create_book()
    await repository.create(book)

    books_found = await usecase.execute("Test")

    assert len(books_found) == 0
