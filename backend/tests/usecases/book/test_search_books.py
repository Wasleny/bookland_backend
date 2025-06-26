from bookland.infra.repositories.in_memory_book_repository import InMemoryBookRepository
from bookland.usecases.book.search_books import SearchBooksUseCase
from tests.factories.book_factory import create_book


def test_search_books_matches_search():
    repository = InMemoryBookRepository()
    usecase = SearchBooksUseCase(repository)

    book = create_book()
    repository.create(book)

    books_found = usecase.execute("Trono")

    assert len(books_found) == 1


def test_search_books_returns_empty_when_no_match():
    repository = InMemoryBookRepository()
    usecase = SearchBooksUseCase(repository)

    book = create_book()
    repository.create(book)

    books_found = usecase.execute("Test")

    assert len(books_found) == 0
