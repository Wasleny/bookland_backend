from bookland.infra.repositories.inmemory_repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from bookland.application.usecases.user.get_user_by_id import GetUserByIdUseCase
from tests.factories.user_factory import create_user

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_user_by_id_returns_user():
    repository = InMemoryUserRepository()
    usecase = GetUserByIdUseCase(repository)

    user = create_user()
    await repository.register(user)

    retrieved_user = await usecase.execute(user.id)

    assert retrieved_user == user


@pytest.mark.asyncio
async def test_get_user_by_id_returns_none_when_not_found():
    repository = InMemoryUserRepository()
    usecase = GetUserByIdUseCase(repository)

    user = create_user()
    await repository.register(user)

    retrieved_user = await usecase.execute("invalid-id")

    assert retrieved_user is None
