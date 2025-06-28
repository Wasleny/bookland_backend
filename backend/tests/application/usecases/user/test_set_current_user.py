from bookland.infra.repositories.inmemory_repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from bookland.application.usecases.user.set_current_user import SetCurrentUserUseCase
from tests.factories.user_factory import create_user


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_set_current_user_successfully():
    repository = InMemoryUserRepository()
    usecase = SetCurrentUserUseCase(repository)

    user = create_user()
    await usecase.execute(user)

    retrieved_user = await repository.get_current_user()

    assert retrieved_user == user
