from bookland.infra.repositories.in_memory_book_repository import InMemoryBookRepository
from bookland.usecases.book.get_all_books import GetAllBooksUseCase
from tests.factories.book_factory import create_book


def test_get_all_books_returns_all_books():
    repository = InMemoryBookRepository()
    usecase = GetAllBooksUseCase(repository)

    book1 = create_book()
    book2 = create_book()
    repository.create(book1)
    repository.create(book2)

    books = usecase.execute()

    assert len(books) == 2
    assert book1 in books
    assert book2 in books
