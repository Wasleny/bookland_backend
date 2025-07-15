from bookland.infra.repositories import InMemoryBookRepository
from bookland.application.usecases import SearchBooksUseCase
from tests.factories.book_factory import create_book


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_search_books_matches_search():
    repository = InMemoryBookRepository()
    usecase = SearchBooksUseCase(repository)

    book = create_book()
    await repository.create(book)

    books_found = await usecase.execute({"title": "Trono", "original_title": "Trono"})

    assert len(books_found) == 1


@pytest.mark.asyncio
async def test_search_books_returns_empty_when_no_match():
    repository = InMemoryBookRepository()
    usecase = SearchBooksUseCase(repository)

    book = create_book()
    await repository.create(book)

    books_found = await usecase.execute({"title": "Test", "original_title": "Test"})

    assert len(books_found) == 0


@pytest.mark.asyncio
async def test_matches_search_ignores_empty_terms():
    repository = InMemoryBookRepository()
    usecase = SearchBooksUseCase(repository)

    book = create_book()
    await repository.create(book)

    search_terms = {
        "title": "",
        "asin": None,
    }

    result = repository._matches_search(book, search_terms)

    assert result is False