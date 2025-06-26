from bookland.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from bookland.usecases.user.demote_user_from_admin import DemoteUserFromAdminUseCase
from tests.factories.user_factory import create_user
from bookland.domain.enums.user_role import UserRole


def test_demote_user_to_admin_successfully():
    repository = InMemoryUserRepository()
    usecase = DemoteUserFromAdminUseCase(repository)

    user = create_user(role=UserRole.ADMIN)
    repository.register(user)
    usecase.execute(user)

    assert repository.get_by_id(user.id).role == UserRole.USER
