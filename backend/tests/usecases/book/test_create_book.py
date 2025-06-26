from bookland.infra.repositories.in_memory_book_repository import InMemoryBookRepository
from bookland.usecases.book.create_book import CreateBookUseCase
from tests.factories.book_factory import create_book


def test_create_book_creates_book_successfully():
    repository = InMemoryBookRepository()
    usecase = CreateBookUseCase(repository)
    book = create_book()

    usecase.execute(book)

    assert repository.get_by_id(book.id) == book
