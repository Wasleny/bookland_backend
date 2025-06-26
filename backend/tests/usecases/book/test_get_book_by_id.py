from bookland.infra.repositories.in_memory_book_repository import InMemoryBookRepository
from bookland.usecases.book.get_book_by_id import GetBookByIdUseCase
from tests.factories.book_factory import create_book


def test_get_book_by_id_returns_book_when_found():
    repository = InMemoryBookRepository()
    usecase = GetBookByIdUseCase(repository)

    book = create_book()
    repository.create(book)

    book_found = usecase.execute(book.id)

    assert book == book_found


def test_get_book_by_id_returns_none_when_not_found():
    repository = InMemoryBookRepository()
    usecase = GetBookByIdUseCase(repository)

    book_found = usecase.execute("invalid-id")

    assert book_found is None
