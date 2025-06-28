from bookland.infra.repositories.inmemory_repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from bookland.application.usecases.user.register_user import RegisterUserUseCase
from tests.factories.user_factory import create_user

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_register_user_succeeds_with_valid_credentials():
    repository = InMemoryUserRepository()
    usecase = RegisterUserUseCase(repository)

    user = create_user()
    current_user = await usecase.execute(user)

    retrieved_user = await repository.get_current_user()

    assert user == current_user
    assert retrieved_user == user
