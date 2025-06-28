from bookland.infra.repositories.inmemory_repositories.in_memory_user_book_repository import (
    InMemoryUserBookRepository,
)
from bookland.application.usecases.user_book.create_user_book import (
    CreateUserBookUseCase,
)
from tests.factories.user_book_factory import create_user_book

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_create_user_book_creates_user_book_successfully():
    repository = InMemoryUserBookRepository()
    usecase = CreateUserBookUseCase(repository)
    user_book = create_user_book()

    retrieved_user_book = await usecase.execute(user_book)

    assert retrieved_user_book == user_book
