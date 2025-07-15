from bookland.infra.repositories import InMemoryUserRepository
from bookland.application.usecases import GetCurrentUserUseCase
from tests.factories.user_factory import create_user


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_current_user_successfully():
    repository = InMemoryUserRepository()
    usecase = GetCurrentUserUseCase(repository)

    user = create_user()
    await repository.register(user)

    retrieved_user = await usecase.execute()

    assert retrieved_user == user
