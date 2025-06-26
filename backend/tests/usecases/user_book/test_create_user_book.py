from bookland.infra.repositories.in_memory_user_book_repository import InMemoryUserBookRepository
from bookland.usecases.user_book.create_user_book import CreateUserBookUseCase
from tests.factories.user_book_factory import create_user_book

def test_create_user_book_creates_user_book_successfully():
    repository = InMemoryUserBookRepository()
    usecase = CreateUserBookUseCase(repository)
    user_book = create_user_book()

    usecase.execute(user_book)

    assert repository.get_by_id(user_book.id) == user_book
