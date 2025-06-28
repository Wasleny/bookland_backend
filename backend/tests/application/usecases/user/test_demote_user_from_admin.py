from bookland.infra.repositories.inmemory_repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from bookland.application.usecases.user.demote_user_from_admin import (
    DemoteUserFromAdminUseCase,
)
from tests.factories.user_factory import create_user
from bookland.domain.enums.user_role import UserRole


import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_demote_user_to_admin_successfully():
    repository = InMemoryUserRepository()
    usecase = DemoteUserFromAdminUseCase(repository)

    user = create_user(role=UserRole.ADMIN)
    await repository.register(user)
    retrieved_user = await usecase.execute(user)

    assert retrieved_user.role == UserRole.USER


@pytest.mark.asyncio
async def test_demote_user_to_admin_returns_none_when_not_found():
    repository = InMemoryUserRepository()
    usecase = DemoteUserFromAdminUseCase(repository)

    user = create_user(role=UserRole.ADMIN)
    retrieved_user = await usecase.execute(user)

    assert retrieved_user is None
