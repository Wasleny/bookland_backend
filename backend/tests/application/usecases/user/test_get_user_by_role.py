from bookland.infra.repositories import InMemoryUserRepository
from bookland.application.usecases import GetUserByRoleUseCase
from tests.factories.user_factory import create_user
from bookland.domain.enums import UserRole

import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_get_user_by_id_returns_user():
    repository = InMemoryUserRepository()
    usecase = GetUserByRoleUseCase(repository)

    user = create_user()
    await repository.register(user)

    users = await usecase.execute(UserRole.USER)

    assert len(users) == 1
