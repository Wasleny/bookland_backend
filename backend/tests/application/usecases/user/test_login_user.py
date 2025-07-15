from bookland.infra.repositories import InMemoryUserRepository
from bookland.application.usecases import LoginUserUseCase
from tests.factories.user_factory import create_user

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_login_user_succeeds_with_valid_credentials():
    repository = InMemoryUserRepository()
    usecase = LoginUserUseCase(repository)

    user = create_user()
    await repository.register(user)
    current_user = await usecase.execute(user.email, user.password)

    assert user == current_user


@pytest.mark.asyncio
async def test_login_user_fails_with_invalid_credentials():
    repository = InMemoryUserRepository()
    usecase = LoginUserUseCase(repository)

    user = create_user()
    current_user = await usecase.execute(user.email, user.password)

    retrieved_user = await repository.get_current_user()

    assert current_user is None
    assert retrieved_user is None
