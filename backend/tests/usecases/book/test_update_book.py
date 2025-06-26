from bookland.infra.repositories.in_memory_book_repository import InMemoryBookRepository
from bookland.usecases.book.update_book import UpdateBookUseCase
from tests.factories.book_factory import create_book


def test_update_book_updates_book_data():
    repository = InMemoryBookRepository()
    usecase = UpdateBookUseCase(repository)

    book = create_book()
    repository.create(book)

    updated_data = create_book(id=book.id, pages=400)

    usecase.execute(updated_data)

    updated_book = repository.get_by_id(book.id)

    assert updated_book.pages == 400
    assert updated_book.title == "Trono de Vidro"
