from bookland.infra.repositories.inmemory_repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from bookland.application.usecases.user.search_user import SearchUserUseCase
from tests.factories.user_factory import create_user


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_search_user_returns_user():
    repository = InMemoryUserRepository()
    usecase = SearchUserUseCase(repository)

    user = create_user()
    await repository.register(user)

    retrieved_user = await usecase.execute(user.email.value)

    assert retrieved_user == user


@pytest.mark.asyncio
async def test_search_user_returns_none_when_not_found():
    repository = InMemoryUserRepository()
    usecase = SearchUserUseCase(repository)

    user = create_user()
    await repository.register(user)

    retrieved_user = await usecase.execute("invalid-email")

    assert retrieved_user is None
