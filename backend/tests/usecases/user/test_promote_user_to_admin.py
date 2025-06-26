from bookland.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from bookland.usecases.user.promote_user_to_admin import PromoteUserToAdminUseCase
from tests.factories.user_factory import create_user
from bookland.domain.enums.user_role import UserRole


def test_promote_user_to_admin_successfully():
    repository = InMemoryUserRepository()
    usecase = PromoteUserToAdminUseCase(repository)

    user = create_user()
    repository.register(user)
    usecase.execute(user)

    assert repository.get_by_id(user.id).role == UserRole.ADMIN
