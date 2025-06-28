from bookland.infra.repositories.inmemory_repositories.in_memory_user_book_repository import (
    InMemoryUserBookRepository,
)
from bookland.application.usecases.user_book.delete_user_book import (
    DeleteUserBookUseCase,
)
from tests.factories.user_book_factory import create_user_book


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_delete_user_book_removes_user_book():
    repository = InMemoryUserBookRepository()
    usecase = DeleteUserBookUseCase(repository)

    user_book = create_user_book()
    await repository.create(user_book)

    await usecase.execute(user_book.id)

    retrieved_user_book = await repository.get_by_id(user_book.id)

    assert retrieved_user_book is None
