from bookland.infra.repositories.in_memory_book_repository import InMemoryBookRepository
from bookland.usecases.book.soft_delete_book import SoftDeleteBookUseCase
from tests.factories.book_factory import create_book


def test_soft_delete_book_removes_book():
    repository = InMemoryBookRepository()
    usecase = SoftDeleteBookUseCase(repository)

    book = create_book()
    repository.create(book)

    usecase.execute(book.id)

    assert repository.get_by_id(book.id) is None
