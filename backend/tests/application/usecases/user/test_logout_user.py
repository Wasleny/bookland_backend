from bookland.infra.repositories.inmemory_repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from bookland.application.usecases.user.logout_user import LogoutUserUseCase
from tests.factories.user_factory import create_user


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_logout_user_successfully():
    repository = InMemoryUserRepository()
    usecase = LogoutUserUseCase(repository)

    user = create_user()
    await repository.register(user)
    await usecase.execute()

    retrieved_user = await repository.get_current_user()

    assert retrieved_user is None
